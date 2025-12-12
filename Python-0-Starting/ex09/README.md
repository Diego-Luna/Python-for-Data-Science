# ft_package

A sample test package for counting elements in lists.

## Installation

You can install the package using pip:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

or

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```

## Building the package

To build the distribution files:

```bash
python -m build
```

This will create both `.tar.gz` and `.whl` files in the `dist/` directory.

## License

MIT License - see LICENSE file for details.
