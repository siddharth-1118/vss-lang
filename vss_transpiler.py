import sys
from pathlib import Path

# VSS → Python keywords
KEYWORD_MAP = {
    # Functions
    "lekka": "def",
    "tirugu": "return",

    # Conditionals
    "aithe": "if",
    "inkaa": "elif",
    "lekapothe": "else",

    # Loops
    "sarlu": "for",
    "varaku": "while",

    # Logic
    "mariyu": "and",
    "leka": "or",
    "kaadu": "not",

    # Booleans
    "nijam": "True",
    "abaddam": "False",

    # Exceptions
    "prayatnam": "try",
    "tappina": "except",
    "inkaa_tappina": "except",
    "ledante": "else",
    "chivariki": "finally",
        
    # Loop Control
    "aagu": "break",
    "kaalipoyedu": "continue",
    "viduchu": "pass",
    
    # Other Keywords
    "etthu": "raise",
    "emitiko": "None",
    "undi": "in",
    "atade": "is",
    "anthe": "as",
    "theeseyi": "del",
    "parisheelana": "assert",
    "tho": "with",
    "lopo": "lambda",
    "ivvu": "yield",
    "anni_chota": "global",
    "bayata": "nonlocal",

    # Classes
    "taragati": "class",
    "aatani": "self",

    # Imports (simple case)
    "teesuku_ravu": "import",
}

def translate_line(line: str) -> str:
    stripped = line.lstrip()
    indent = line[: len(line) - len(stripped)]

    # Special handling: "nunchi X teesuku Y" → "from X import Y"
    if stripped.startswith("nunchi "):
        parts = stripped.split()
        # Expected: ["nunchi", module, "teesuku", name]
        if len(parts) >= 4 and parts[2] == "teesuku":
            module = parts[1]
            name = " ".join(parts[3:])
            stripped = f"from {module} import {name}"

    # 1) Keywords at start of line (def, if, for, while, class, try, except, etc.)
    for vss_kw, py_kw in KEYWORD_MAP.items():
        if stripped.startswith(vss_kw + " "):
            stripped = stripped.replace(vss_kw, py_kw, 1)
        elif stripped.startswith(vss_kw + ":"):
            stripped = stripped.replace(vss_kw, py_kw, 1)

    # 2) Inline boolean / logic words (and, or, not, True, False)
    for vss_kw, py_kw in [
        ("mariyu", "and"),
        ("leka", "or"),
        ("kaadu", "not"),
        ("nijam", "True"),
        ("abaddam", "False"),
                ("emitiko", "None"),
        ("undi", "in"),
        ("atade", "is"),
        ("anthe", "as"),
    ]:
        stripped = stripped.replace(" " + vss_kw + " ", " " + py_kw + " ")

    # 3) Function-like keywords
    stripped = stripped.replace("mudinchu(", "print(")   # print
    stripped = stripped.replace("teesuko(", "input(")    # input

    return indent + stripped

def vss_to_python(src: str) -> str:
    lines = src.splitlines()
    out_lines = [translate_line(line) for line in lines]
    return "\n".join(out_lines)

def main():
    """Main entry point for VSS"""
    if len(sys.argv) < 2:
        print("VSS Programming Language v2.0")
        print("Usage: vss <file.vss>")
        print("       vss --help")
        print("       vss --version")
        sys.exit(0)
    
    arg = sys.argv[1]
    
    if arg in ['--help', '-h']:
        print("VSS Programming Language v2.0")
        print("")
        print("Usage: vss <file.vss>")
        print("")
        print("Options:")
        print("  --help, -h       Show this help message")
        print("  --version, -v    Show version information")
        print("")
        print("Examples:")
        print("  vss myprogram.vss")
        print("  vss examples/hello.vss")
        print("")
        print("GitHub: https://github.com/siddharth-1118/vss-lang")
        sys.exit(0)
    
    if arg in ['--version', '-v']:
        print("VSS Programming Language v2.0")
        print("Python-like language with Telugu-style English keywords")
        print("GitHub: https://github.com/siddharth-1118/vss-lang")
        sys.exit(0)
    
    # Run VSS file
    src_path = Path(sys.argv[1])
    
    if not src_path.exists():
        print(f"Error: File '{sys.argv[1]}' not found")
        print("")
        print("Usage: vss <file.vss>")
        print("Try: vss --help")
        sys.exit(1)
    
    code = src_path.read_text(encoding="utf-8")
    py_code = vss_to_python(code)
    
    # Save generated Python (for debugging)
    tmp = src_path.with_suffix(".vss.py")
    tmp.write_text(py_code, encoding="utf-8")
    
    # Run generated Python
    exec(compile(py_code, str(tmp), "exec"), {})

if __name__ == "__main__":
    main()
