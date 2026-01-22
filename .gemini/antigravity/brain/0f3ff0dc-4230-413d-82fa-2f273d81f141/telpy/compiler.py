import sys
from lark import Lark, Transformer, v_args
from lark.indenter import Indenter

class TelPyIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

class TelPyToPython(Transformer):
    def start(self, items):
        return "\n".join(items)

    def stmt(self, items):
        return items[0]
    
    def simple_stmt(self, items):
        return items[0]
    
    def expr_stmt(self, items):
        return items[0]
    
    def assign_stmt(self, items):
        name, value = items[0], items[1]
        return f"{name} = {value}"
    
    def return_stmt(self, items):
        if not items:
            return "return"
        # Item 0 could be expr or "phalam_ivvu". 
        # Grammar: expr "phalam_ivvu" | "phalam_ivvu" expr
        # Filter out the keyword
        exprs = [x for x in items if x.type != 'KEYWORD' and str(x) != 'phalam_ivvu']
        if exprs:
            return f"return {exprs[0]}"
        return "return"

    def function_call_expr(self, items):
        # Handle buitlins translation
        name = items[0]
        args = items[1] if len(items) > 1 else ""
        
        # Builtin Map
        from .lexicon import BUILTINS
        if name in BUILTINS:
            name = BUILTINS[name]
            
        return f"{name}({args})"
    
    def funccall(self, items):
        func = items[0]
        args = items[1] if len(items) > 1 else ""
        if func == "chupinchu": func = "print"
        if func == "adugu": func = "input"
        return f"{func}({args})"

    def arguments(self, items):
        return ", ".join(items)
    
    def argvalue(self, items):
        return items[0]
    
    def var(self, items):
        return str(items[0])
    
    def string(self, items):
        return str(items[0])
    
    def number(self, items):
        return str(items[0])

    def const_none(self, items): return "None"
    def const_true(self, items): return "True"
    def const_false(self, items): return "False"

    # Postfix Comparison: expr expr op -> expr op expr
    def comparison(self, items):
        if len(items) == 1:
            return items[0]
        left, right, op = items[0], items[1], items[2]
        return f"({left} {op} {right})"
    
    # Operators
    def op_gt(self, i): return ">"
    def op_lt(self, i): return "<"
    def op_eq(self, i): return "=="
    def op_neq(self, i): return "!="
    def op_ge(self, i): return ">="
    def op_le(self, i): return "<="
    
    def op_add(self, i): return "+"
    def op_sub(self, i): return "-"
    def op_mul(self, i): return "*"
    def op_div(self, i): return "/"
    def op_mod(self, i): return "%"

    # Math Infix
    def expr(self, items):
        return " ".join(items)
    def term(self, items):
        return " ".join(items)
    def factor(self, items):
        return " ".join(items)

    def if_stmt(self, items):
        # items: 'okavela' test 'ayithe' suite ...
        # Filter keywords out or iterate
        # Structure: if condition: block ...
        # Simplified handling:
        # First 3 items are always: "okavela" test "ayithe" suite?
        # No, keywords are string tokens.
        
        # Just capturing logic:
        # 0: test, 1: suite. 
        # If elif exists: 2: test, 3: suite...
        # If else exists: last item is suite
        
        code = []
        
        # First If
        condition = items[0]
        block = items[1]
        code.append(f"if {condition}{block}")
        
        idx = 2
        while idx < len(items):
            # Check if it's elif (pair of test, suite) or else (suite)
            # Grammar: ("lekapothe_okavela" test "ayithe" suite)* ("lekapothe" suite)?
            # The tokens "lekapothe_okavela" etc might appear in items if implicit?
            # Lark filters unnamed tokens usually, but strict match strings are dropped?
            # It depends on if they are terminals or not.
            # In my grammar they are string literals, so they might NOT be in items unless aliased.
            # Grammar: "okavela" test "ayithe" suite ...
            # Items will be [test, suite, test, suite, suite] (if elif else)
            
            remaining = len(items) - idx
            if remaining >= 2:
                # Elif
                cond = items[idx]
                blk = items[idx+1]
                code.append(f"elif {cond}{blk}")
                idx += 2
            else:
                # Else
                blk = items[idx]
                code.append(f"else{blk}")
                idx += 1
        return "\n".join(code)

    def suite(self, items):
        # items are stmt list
        lines = "\n    ".join(items)
        return f":\n    {lines}" # Indentation handled naively

    def func_def(self, items):
        name = items[0]
        params = items[1] if isinstance(items[1], str) else "" 
        # Wait, if params absent, items[1] might be suite.
        # Grammar: "pani" NAME "(" [params] ")" "nirvachinchu" suite
        # If params empty, items = [name, suite]
        # If params present, items = [name, params_str, suite]
        
        if len(items) == 2:
            body = items[1]
            return f"def {name}(){body}"
        else:
            args = items[1]
            body = items[2]
            return f"def {name}({args}){body}"

    def params(self, items):
        return ", ".join(items)
        
    def param(self, items):
        return str(items[0])

def compile_telpy(source):
    # Load Grammar
    import os
    grammar_path = os.path.join(os.path.dirname(__file__), 'telpy.lark')
    with open(grammar_path, 'r') as f:
        grammar = f.read()
        
    parser = Lark(grammar, parser='lalr', lexer='callbacks', postlex=TelPyIndenter())
    tree = parser.parse(source)
    
    return TelPyToPython().transform(tree)
