# TelPy Syntax & Semantics

## Design Philosophy
Adapt Python's structure to Telugu's SOV (Subject-Object-Verb) word order where natural, while preserving the indentation-based block structure.

## Control Flow

### Conditional Statements (`if-elif-else`)
Python:
```python
if x > 5:
    print("Big")
elif x == 5:
    print("Equal")
else:
    print("Small")
```

TelPy:
```telpy
okavela x 5 kanna_pedda ayithe:    # If x 5 than big becomes:
    "Peddadi" chupinchu            # "Big" show
lekapothe x 5 ki samam ayithe:     # Else x 5 to equal becomes:
    "Samanam" chupinchu            # "Equal" show
lekapothe:                         # Else:
    "Chinnadi" chupinchu           # "Small" show
```
*Note: The token mapping for operators allows for suffix-style reading.*
`>` -> `kanna_pedda`
`==` -> `ki_samam` (or just `samam`)

### Loops (`for`, `while`)
Python:
```python
for i in items:
    process(i)
```

TelPy:
```telpy
prathi i, items lo:      # Each i, items in:
    process(i)
```
*Structure*: `prathi <var>, <iterable> lo:`

Python:
```python
while count > 0:
    count -= 1
```

TelPy:
```telpy
count 0 kanna_pedda unnantha_varaku:   # count 0 than big being-until:
    count -= 1                         # count decrease (operator simplification?)
```
*Simplification*: `varaku count > 0:` is easier to implement, but `count 0 kanna_pedda unnantha_varaku:` is more natural. We will support the SOV structure.

## Functions
Python:
```python
def greet(name):
    return "Hello " + name
```

TelPy:
```telpy
pani greet(name) nirvachinchu:      # function greet(name) define:
    "Namaskaram " + name phalam_ivvu
```
*Keyword*: `pani` (work/function) or `kriya`. Let's use `pani` for simplicity, ending with `nirvachinchu` (define) is optional or implied? 
Python starts with `def`. TelPy could start with `nirvachinchu greet(name):`.
Let's stick to: `nirvachinchu greet(name):` to keep the header clear.
*Return*: `phalam_ivvu` (result give).

## Error Handling
Python:
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error")
```

TelPy:
```telpy
prayatninchu:
    x = 1 / 0
thappu_ayithe ZeroDivisionError:
    "Thappu" chupinchu
```

## Comparisons & Logic
- `x > y` -> `x y kanna_pedda`
- `x < y` -> `x y kanna_chinna`
- `x == y` -> `x y ki samam`
- `x and y` -> `x mariyu y`
- `x or y` -> `x leka y`
- `not x` -> `x kaadu`

## Variable Assignment
Standard `x = 5` is fine.
Colloquial: `x ki 5 ivvu` (give 5 to x)? Too verbose. Stick to `x = 5`.
