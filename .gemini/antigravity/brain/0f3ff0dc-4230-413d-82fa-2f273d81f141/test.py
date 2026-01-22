import sys
import subprocess
import os

try:
    import lark
    print("Lark found. Running hello.tel...")
    
    # Run the CLI
    cmd = [sys.executable, '-m', 'telpy.cli', 'hello.tel']
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd())
    
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    
except ImportError:
    print("Lark not found. Please run: pip install lark")
