INSTALL.md# VSS Programming Language - Installation Guide

Complete installation instructions for VSS (Telugu-style Python)

## 📋 Prerequisites

Before installing VSS, you need:

- **Python 3.7 or higher** installed on your system
- **pip** (Python package manager)
- **git** (for cloning the repository)

### Check if you have Python:

**Windows:**
```cmd
python --version
```

**Mac/Linux:**
```bash
python3 --version
```

If you don't have Python, download it from [python.org](https://www.python.org/downloads/)

---

## ⚡ Quick Install (Recommended)

This is the **easiest** way to install VSS:

### Step 1: Clone the repository

```bash
git clone https://github.com/siddharth-1118/vss-lang.git
cd vss-lang
```

### Step 2: Install VSS

```bash
pip install -e .
```

**Note:** The dot `.` at the end is important!

### Step 3: Verify installation

```bash
vss --version
vss --help
```

You should see:
```
VSS Programming Language v2.0
```

### Step 4: Run your first VSS program

```bash
vss examples/hello.vss
```

🎉 **Done!** VSS is now installed and you can use `vss` command anywhere!

---

## 🔧 Installation Methods

### Method 1: Install as System Command (Recommended)

This method installs VSS globally so you can use it from any directory.

```bash
# Clone the repository
git clone https://github.com/siddharth-1118/vss-lang.git
cd vss-lang

# Install in editable mode
pip install -e .

# Now use vss anywhere
vss myprogram.vss
vss --help
vss --version
```

**Benefits:**
- ✅ Use `vss` command from anywhere
- ✅ Easy to update (`git pull` + `pip install -e .`)
- ✅ Professional installation

---

### Method 2: Direct Python Execution

If you don't want to install, you can run VSS directly:

```bash
# Clone the repository
git clone https://github.com/siddharth-1118/vss-lang.git
cd vss-lang

# Run VSS files directly
python vss_transpiler.py examples/hello.vss
python vss_transpiler.py myprogram.vss
```

**Benefits:**
- ✅ No installation needed
- ✅ Portable
- ❌ Must be in vss-lang folder

---

### Method 3: Download ZIP (No Git)

If you don't have git:

1. Go to: https://github.com/siddharth-1118/vss-lang
2. Click green **"Code"** button → **"Download ZIP"**
3. Extract the ZIP file
4. Open terminal in extracted folder:

```bash
cd path/to/vss-lang
pip install -e .
```

---

## 🪟 Windows Specific Instructions

### Option A: Install with pip (Easiest)

```cmd
git clone https://github.com/siddharth-1118/vss-lang.git
cd vss-lang
pip install -e .
vss --version
```

### Option B: Create vss.bat for PATH

If `pip install` doesn't work, create a batch file:

```cmd
cd C:\vss-lang
echo @echo off > vss.bat
echo python "%~dp0vss_transpiler.py" %* >> vss.bat
```

Then add `C:\vss-lang` to your PATH:

1. Search "Environment Variables" in Windows
2. Edit PATH → Add New → `C:\vss-lang`
3. Restart terminal
4. Now `vss` command works everywhere!

---

## 🍎 Mac/Linux Specific Instructions

```bash
# Clone and install
git clone https://github.com/siddharth-1118/vss-lang.git
cd vss-lang
pip3 install -e .

# Or use python3 explicitly
python3 -m pip install -e .

# Verify
vss --version
```

If `vss` command not found, try:

```bash
python3 -m vss --version
```

Or add an alias to `~/.bashrc` or `~/.zshrc`:

```bash
alias vss='python3 -m vss'
```

---

## 📦 What Gets Installed?

When you run `pip install -e .`, it:

✅ Creates a `vss` command in your system  
✅ Links to your local vss-lang folder (editable mode)  
✅ Makes VSS available system-wide  
✅ Allows easy updates with `git pull`

---

## 🔄 Updating VSS

To get the latest version:

```bash
cd vss-lang
git pull
pip install -e . --upgrade
```

---

## ❌ Uninstalling VSS

```bash
pip uninstall vss-lang
```

---

## 🆘 Troubleshooting

### "vss: command not found"

**Solution 1:** Reinstall with pip
```bash
pip install -e . --force-reinstall
```

**Solution 2:** Use full path
```bash
python -m vss myprogram.vss
```

**Solution 3 (Windows):** Check if Python Scripts folder is in PATH
```cmd
where vss
```

### "pip: command not found"

Install pip:
```bash
python -m ensurepip --upgrade
```

### "Permission denied" (Mac/Linux)

Use `--user` flag:
```bash
pip install -e . --user
```

### "File not found" errors

Make sure you're in the `vss-lang` folder:
```bash
cd vss-lang
pwd  # Should show vss-lang path
```

---

## 📝 Verify Installation

Run these commands to make sure everything works:

```bash
# Check version
vss --version

# Show help
vss --help

# Run example
vss examples/hello.vss

# Run calculator
vss examples/calculator.vss
```

Expected output from `vss --version`:
```
VSS Programming Language v2.0
Python-like language with Telugu-style English keywords
GitHub: https://github.com/siddharth-1118/vss-lang
```

---

## 🎓 Next Steps

Now that VSS is installed:

1. ✅ Read the [README.md](README.md) for VSS keywords
2. ✅ Check [examples/](examples/) folder for sample programs
3. ✅ Write your first VSS program:

```vss
# myprogram.vss
mudinchu("Hello from VSS!")

lekka greet(name):
    mudinchu("Hello, " + name + "!")

greet("World")
```

Run it:
```bash
vss myprogram.vss
```

---

## 📞 Support

- **Issues:** https://github.com/siddharth-1118/vss-lang/issues
- **GitHub:** https://github.com/siddharth-1118/vss-lang

---

**Happy coding in VSS! 🚀**
