import os
import re
from pathlib import Path
from setuptools import setup, Extension


INCLUDE_DIR = "./include"
SOURCE_DIR = "./src"

# Set Include dirs
include_dirs = [INCLUDE_DIR]

# Set source files
source_dir_path = Path(SOURCE_DIR)
src_files = [str(elem.absolute()) for elem in source_dir_path.glob("*.i")]
for filepath in source_dir_path.glob("*.cpp"):
    if re.search(r"(.*)_wrap.cpp", str(filepath)) is not None:
        continue
    src_files.append(str(filepath.absolute()))


os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"
setup(
    name="hello_world",
    version="1.0.0",
    ext_modules=[
        Extension(
            "_hello_world",
            sources=src_files,
            include_dirs=include_dirs,
            swig_opts=["-c++", "-py3"],
            language="c++",
            py_modules = "hello_world"
        )
    ],
)
