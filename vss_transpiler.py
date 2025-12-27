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
    if len(sys.argv) != 2:
        print("Usage: python vss_transpiler.py file.vss")
        sys.exit(1)

    src_path = Path(sys.argv[1])
    if not src_path.exists():
        print(f"File not found: {src_path}")
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
