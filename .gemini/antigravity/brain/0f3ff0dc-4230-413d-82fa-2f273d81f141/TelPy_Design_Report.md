# TelPy: A Vernacular Programming Language for Telugu Speakers
**Design Report & Specification**
**Author:** Dr. Arjun Reddy
**Date:** January 2026

## 1. Executive Summary & Philosophy
TelPy is a proposed domain-specific language designed to lower the barrier to entry for Telugu-speaking programmers. By harmonizing Python's powerful ecosystem with Telugu's cognitive and grammatical structures (Subject-Object-Verb), TelPy offers a "native" coding experience without sacrificing professional applicability. It is not merely a dictionary translation of Python; it is a syntactic adaptation that respects the linguistic intuition of its users.

**Core Principles:**
*   **Cognitive Resonance**: Syntax follows Telugu grammar (SOV) where natural.
*   **Readability**: Uses a modified ISO 15919 Romanization scheme for clarity.
*   **Interoperability**: Transpiles 1:1 to standard Python 3, ensuring access to the entire PyPI ecosystem.

## 2. Core Language Specification

### Lexicon & Glossary
The keyword set prioritizes action-oriented verbs and colloquial clarity over formal Sanskrit terms.

| Category | Python Keyword | TelPy Keyword | Meaning / Etymology |
| :--- | :--- | :--- | :--- |
| **Control** | `if` | `okavela` | Suppose / If |
| | `else` | `lekapothe` | Otherwise |
| | `elif` | `lekapothe_okavela` | Otherwise if |
| | `for` | `prathi` | Each / Every |
| | `while` | `varaku` | Until / As long as |
| | `return` | `phalam_ivvu` | Result give |
| | `break` | `aapu` | Stop |
| **Logic** | `and` | `mariyu` | And |
| | `or` | `leka` | Or |
| | `not` | `kaadu` | Not |
| | `is`| `undi` | Is/Exists |
| **Def** | `def` | `pani` ... `nirvachinchu` | Work ... Define |
| | `class` | `thargathi` | Class |
| **Values**| `None` | `emiledu` | Nothing |
| | `True` | `nizam` | Truth |
| | `False` | `abaddham` | False/Lie |

### Syntactic Structures
**SOV Adaptation**: TelPy adopts a hybrid structure where the subject and object often precede the verb/operator, mirroring Telugu sentence construction.

*   **Logic**: `x > 5` becomes `x 5 kanna_pedda`.
*   **Loops**: `for i in list` becomes `prathi i, list lo` (Each i, list in).

## 3. Example Code Comparisons

### Example A: Hello World & Input
**Python**:
```python
name = input("Enter name: ")
print("Hello " + name)
```

**TelPy**:
```telpy
name = "Peru cheppu: " adugu()
"Namaskaram " + name chupinchu()
```
*Note: `adugu` (ask) wraps the prompt. `chupinchu` (show) handles output.*

### Example B: Conditional Logic (Even/Odd)
**Python**:
```python
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**TelPy**:
```telpy
num = 10
okavela num % 2 == 0 ayithe:
    "Sari Sankhya" chupinchu()
lekapothe:
    "Besi Sankhya" chupinchu()
```
*Design Note*: `ayithe` (then) acts as the block initiator (`:`).

### Example C: Function Definition
**Python**:
```python
def add(a, b):
    return a + b
```

**TelPy**:
```telpy
pani add(a, b) nirvachinchu:
    a + b phalam_ivvu
```

## 4. Technical Implementation Roadmap

### Architecture
The TelPy generic transpiler consists of three stages:
1.  **Tokenizer**: Recognizes romanized Telugu keywords and literals. Handles specific multi-char tokens like `kanna_pedda`.
2.  **Parser (ANTLR4)**: Consumes tokens and builds an Abstract Syntax Tree (AST). The grammar is defined in EBNF, supporting SOV constructs like `expr OPERATOR keyword` structures.
3.  **Code Generator (Transformer)**: Walks the TelPy AST and emits valid Python 3 code. It handles reordering (SOV -> SVO) and keyword translation.

### Stack
*   **Language**: Python 3.10+
*   **Parser**: Lark or ANTLR4
*   **Output**: Standard `.py` files compatible with CPython.

## 5. Considerations for Developers

### Risks & Mitigations
*   **Homophones**: Telugu has many words that sound similar. Romanization must be distinct. *Mitigation*: Strict linter and distinct spelling rules in the glossary.
*   **Errors**: Python runtime errors will point to generated Python lines. *Mitigation*: The transpiler must generate a "Source Map" to map Python error lines back to TelPy source lines for friendly debugging.
*   **Adoption**: "Why not just learn Python?". *Strategy*: Market TelPy as a bridge. Provide a "Eject to Python" command that converts the project to Python once the learner is confident.

### Next Steps
1.  Develop the `telpy` CLI tool.
2.  Build a VS Code Extension with syntax highlighting for `.tel` files.
3.  Pilot with a small group of Telugu-medium students.
