from setuptools import setup
import pathlib

# Read the contents of README file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="vss-lang",
    version="2.1.0",    author="Siddharth",
    author_email="saisiddharthwoota@gmail.com",
    description="VSS Programming Language - Python with Telugu-style English keywords",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/siddharth-1118/vss-lang",
    project_urls={
        "Bug Reports": "https://github.com/siddharth-1118/vss-lang/issues",
        "Source": "https://github.com/siddharth-1118/vss-lang",
        "Documentation": "https://github.com/siddharth-1118/vss-lang/blob/main/README.md",
    },
    py_modules=["vss_transpiler"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Compilers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Natural Language :: Telugu",
    ],
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "vss=vss_transpiler:main",
        ],
    },
    keywords="vss telugu english programming-language python-like transpiler interpreter lekka mudinchu chupu aithe leni daka prati loop function class try except import as from with open read write file variables operators .vss vss-lang vss-language telugu-style",
    license="MIT",
)
