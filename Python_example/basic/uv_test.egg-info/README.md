[porject]

name = "uv-test"
version = "0.1.0"
description = "add ypit description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "numpy>=2.4.6",
    "request>=2.34.2", 
]

[project.scripts]
test_package_main = "test_package.__init__:main"

[build-system]
requires