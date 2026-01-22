import sys
import os
from .compiler import compile_telpy

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m telpy.cli <file.tel>")
        return

    filename = sys.argv[1]
    if not filename.endswith('.tel'):
        print("Error: File must match *.tel")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()

        python_code = compile_telpy(source)
        
        # Execute it
        print("--- Transpiled Python Code ---")
        print(python_code)
        print("--- Output ---")
        exec(python_code, {'__name__': '__main__'})
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
