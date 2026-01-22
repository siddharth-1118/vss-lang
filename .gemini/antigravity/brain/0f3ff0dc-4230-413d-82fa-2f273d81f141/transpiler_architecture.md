# TelPy Transpiler Architecture

## Overview
The Transpiler ("TelPy Compiler") converts TelPy source code (`.tel`) into valid Python 3 Source Code.

**Flow:** `Source Code` -> `Tokenizer` -> `Parser` -> `AST` -> `Transformer` -> `Code Generator` -> `Python Code`

## Components

### 1. Tokenizer (Lexer)
- **Role**: Breaks raw text into tokens.
- **Specification**:
    - Must support UTF-8 (future proofing).
    - **Tokens**:
        - `KEYWORD`: `okavela`, `lekapothe`, `pani`, etc.
        - `OPERATOR`: `kanna_pedda` (>), `mariyu` (and).
        - `IDENTIFIER`: Variables, function names.
        - `INDENT/DEDENT`: Crucial for block structure.
        - `STRING`: Quotes with support for Telugu chars if needed.

### 2. Parser
- **Role**: Analyzes the token stream against the TelPy Grammar to build an Abstract Syntax Tree (AST).
- **Tool Recommendation**: **ANTLR4** or **Lark** (Python).
- **Grammar Strategy**:
    - Define a formal EBNF grammar.
    - **SOV Handling**: The grammar must account for Subject-Object-Verb structures.
        - *Example Rule*: `if_stmt: 'okavela' expr 'ayithe' block`
        - *Expression Rule*: `expr: term (OPERATOR term)*` where operator can be `kanna_pedda`.

### 3. AST (Abstract Syntax Tree)
- The Parser produces a Parse Tree. We should map this to a custom **TelPy AST** or directly to **Python's AST**.
- **Recommendation**: Build a TelPy-specific intermediate representation (IR) to handle the structural differences easier before flattening to Python.

### 4. Code Generator (Emitter)
- **Role**: Walks the AST and prints Python code.
- **Translation Logic**:
    - `okavela x 5 kanna_pedda ayithe:` -> `if x > 5:`
    - `pani foo():` -> `def foo():`
    - `print(x)` -> `chupinchu(x)` (Reverse? No, TelPy source `chupinchu` -> Python `print`).
    - **Reordering**:
        - Source: `x 5 kanna_pedda`
        - AST: `BinaryOp(left=x, op=GT, right=5)`
        - Output: `x > 5`

## Tech Stack
- **Language**: Python 3.10+
- **Parser Library**: `Lark` (for ease of use and Earley parser support which handles ambiguous grammars well).
- **CLI Tool**: `telpy` command.
    - `telpy run main.tel` (Transpiles and runs in memory).
    - `telpy build main.tel` (Outputs `main.py`).

## Challenges & Mitigations
- **Homophones/Ambiguity**: Romanized Telugu can be ambiguous. `kooda` (also) vs `kooda` (add).
    - *Mitigation*: Context-sensitive parsing. Use `koodu` for add vs `kooda` for also? Or strict keywords.
- **Line Numbers**: Source maps are essential for debugging so `SyntaxError` points to `.tel` line, not `.py` line.
