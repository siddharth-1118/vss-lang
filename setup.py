from setuptools import setup

setup(
    name="vss-lang",
    version="2.0.0",
    py_modules=["vss_transpiler"],
    entry_points={
        "console_scripts": [
            "vss=vss_transpiler:main",
        ],
    },
    python_requires=">=3.7",
)
