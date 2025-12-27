# VSS Programming Language

**VSS** is a Python-like programming language with Telugu-style English keywords. It transpiles to Python, making it easy to learn programming with familiar words while leveraging Python's powerful ecosystem.

## Features

- 🎯 **Telugu-English Keywords**: Uses Telugu-inspired English words (`lekka`, `mudinchu`, `aithe`)
- 🐍 **Python Compatible**: Transpiles to Python 3, works with all Python libraries
- 📦 **Full Feature Set**: Functions, classes, exceptions, imports, and more
- 🚀 **Easy to Learn**: Simple syntax perfect for beginners
- ⚡ **Fast Development**: Leverage existing Python ecosystem

## Installation

1. Clone this repository:
```bash
git clone https://github.com/siddharth-1118/vss-lang.git
cd vss-lang
```

2. Ensure you have Python 3.7+ installed:
```bash
python --version
```

## Quick Start

1. Create a file `hello.vss`:
```vss
mudinchu("Hello from VSS!")
```

2. Run it:
```bash
python vss_transpiler.py hello.vss
```

## VSS Keywords

### Functions
- `lekka` → `def` (define function)
- `tirugu` → `return`

### Conditionals
- `aithe` → `if`
- `inkaa` → `elif`
- `lekapothe` → `else`

### Loops
- `sarlu` → `for`
- `varaku` → `while`

### Logic & Booleans
- `mariyu` → `and`
- `leka` → `or`
- `kaadu` → `not`
- `nijam` → `True`
- `abaddam` → `False`

### Exceptions
- `prayatnam` → `try`
- `tappina` → `except`
- `chivariki` → `finally`
- `ledante` → `else` (try-else)

### Classes & Objects
- `taragati` → `class`
- `aatani` → `self`

### Imports
- `teesuku_ravu` → `import`
- `nunchi ... teesuku ...` → `from ... import ...`

### I/O
- `mudinchu(...)` → `print(...)`
- `teesuko(...)` → `input(...)`

## Example Programs

### Hello World
```vss
mudinchu("Hello, World!")
```

### Functions
```vss
lekka add(a, b):
    tirugu a + b

result = add(5, 3)
mudinchu(result)
```

### Conditions
```vss
age = 20

aithe age >= 18:
    mudinchu("Adult")
lekapothe:
    mudinchu("Minor")
```

### Loops
```vss
# For loop
sarlu i in range(5):
    mudinchu(i)

# While loop
x = 0
varaku x < 5:
    mudinchu(x)
    x = x + 1
```

### Classes
```vss
taragati Student:
    lekka __init__(aatani, name, marks):
        aatani.name = name
        aatani.marks = marks
    
    lekka display(aatani):
        mudinchu("Name: " + aatani.name)
        mudinchu("Marks: " + str(aatani.marks))

s = Student("Sai", 95)
s.display()
```

### Exception Handling
```vss
lekka divide(a, b):
    prayatnam:
        result = a / b
        tirugu result
    tappina ZeroDivisionError:
        mudinchu("Cannot divide by zero")
        tirugu None
    chivariki:
        mudinchu("Division attempt complete")

mudinchu(divide(10, 2))
mudinchu(divide(10, 0))
```

### Using Python Libraries
```vss
teesuku_ravu math
nunchi random teesuku randint

mudinchu("Pi value: " + str(math.pi))
mudinchu("Random number: " + str(randint(1, 100)))
```

## How It Works

VSS is a **transpiler** (source-to-source compiler):

1. Reads `.vss` source files
2. Translates VSS keywords to Python keywords
3. Generates equivalent Python code
4. Executes the Python code

This means you get:
- ✅ All Python features and libraries
- ✅ Python's performance
- ✅ Familiar syntax for Telugu speakers
- ✅ Easy debugging (can check generated `.vss.py` files)

## File Structure

```
vss-lang/
├── vss_transpiler.py   # Main transpiler
├── examples/           # Example VSS programs
│   ├── hello.vss
│   ├── calculator.vss
│   └── full_demo.vss
├── README.md
└── LICENSE
```

## Contributing

Contributions are welcome! Here are some ways you can help:

- Add more example programs
- Improve error messages
- Add syntax highlighting for editors
- Write documentation
- Report bugs

## Roadmap

- [ ] Better error messages with line numbers
- [ ] VSCode extension for syntax highlighting
- [ ] Interactive REPL (Read-Eval-Print Loop)
- [ ] Standard library with common VSS functions
- [ ] Debugger integration
- [ ] Package manager integration

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

Created by [Siddharth](https://github.com/siddharth-1118)

## Acknowledgments

- Inspired by Python's simplicity
- Built for Telugu-speaking developers and learners
- Thanks to the open-source community

---

**Happy coding in VSS! 🚀**
