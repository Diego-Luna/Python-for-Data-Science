# Python for Data Science

Comprehensive implementation of the 42 School Python for Data Science curriculum, covering the trajectory from core Python mechanics to vector computation, tabular data manipulation, object-oriented architecture, and data-oriented design patterns.

---

## Table of Contents

- [Overview](#overview)
- [Curriculum Roadmap](#curriculum-roadmap)
- [Key Learning Keywords & Concepts](#key-learning-keywords--concepts)
- [Module Breakdown](#module-breakdown)
  - [Module 00: Starting](#module-00-starting)
  - [Module 01: Array](#module-01-array)
  - [Module 02: DataTable](#module-02-datatable)
  - [Module 03: OOP](#module-03-oop)
  - [Module 04: Data-Oriented Design (DoD)](#module-04-data-oriented-design-dod)
- [Environment Setup](#environment-setup)
- [Verification & Quality Assurance](#verification--quality-assurance)
- [GitHub Repository Configuration](#github-repository-configuration)
- [License](#license)

---

## Overview

This repository contains clean, modular, and PEP 8 compliant solutions for the 42 Python for Data Science module series. Each module targets essential paradigms required for modern data engineering and scientific computing:

1. **Foundations**: Data structures, string parsing, type inspection, packaging, and custom generators.
2. **Numerical Computing**: Multidimensional array transformations, image manipulation, and slicing with NumPy.
3. **Data Analysis & Visualization**: Tabular data wrangling, historical series cleaning, and plotting with Pandas and Matplotlib.
4. **Object-Oriented Design**: Abstract classes, multiple inheritance, Method Resolution Order (MRO), and operator overloading.
5. **Advanced Language Features**: Variadic arguments, closures, custom decorators, and structured data with Data Classes.

---

## Curriculum Roadmap

| Module | Directory | Focus Area | Key Libraries |
| :--- | :--- | :--- | :--- |
| **Python 0** | `Python-0-Starting` | Core syntax, data types, iterators, packaging | Standard Library, Setuptools, Wheel |
| **Python 1** | `Python-1-Array` | Vectorized operations, multidimensional slicing | NumPy, Pillow, Matplotlib |
| **Python 2** | `Python-2-DataTable` | Data ingestion, time-series plotting, projections | Pandas, Matplotlib, SciPy |
| **Python 3** | `Python-3-OOP` | Polymorphism, MRO, dunder operators, static methods | Standard Library (`abc`, `math`) |
| **Python 4** | `Python-4-Dod` | Closures, function decorators, dataclasses, metrics | Standard Library (`dataclasses`, `sys`) |

---

## Key Learning Keywords & Concepts

Below is the structured list of keywords and engineering concepts mastered throughout this repository:

### Core Python & Tooling
- **Type System**: Dynamic typing, type hints (`typing`), duck typing, truthiness, `None` vs `NaN`.
- **Built-in Data Structures**: `list`, `tuple`, `set`, `dict`, mutability, hashability, dictionary lookups.
- **Functional Programming**: List comprehensions, `lambda`, generator functions (`yield`), iterator protocol.
- **Packaging & Distribution**: `pyproject.toml`, build backends (`setuptools`, `flit`), wheel packaging, `pip`.

### Scientific Computing & Image Processing
- **NumPy Fundamentals**: `ndarray`, strides, memory layout, broadcasting, shape inspection, axes manipulation.
- **Vectorized Operations**: Element-wise arithmetic, conditional filtering, avoiding explicit Python loops.
- **Image Operations**: Channel separation (R/G/B), image inversion, grayscale conversion, transposition, cropping.

### Data Analysis & Visualization
- **Pandas DataFrames**: CSV parsing, indexing, label slicing, column extraction, handling missing data.
- **Data Visualization**: Line charts, multi-series plots, scatter plots, log-scaling, legends, axis labeling.
- **Data Normalization**: Parsing custom numerical suffixes (`k`, `M`, `B`), unit scaling, time-series alignment.

### OOP & Software Architecture
- **Abstract Base Classes**: `abc.ABC`, `@abstractmethod`, interface enforcement, polymorphism.
- **Multiple Inheritance & MRO**: Diamond inheritance problem, `super()`, C3 linearization algorithm.
- **Operator Overloading**: Dunder methods (`__add__`, `__sub__`, `__mul__`, `__truediv__`, `__repr__`).
- **Method Scope**: Instance methods vs `@classmethod` vs `@staticmethod`.

### Data-Oriented Design & Metaprogramming
- **Dynamic Parameter Handling**: Variadic parameters (`*args`, `**kwargs`), parameter unpacking.
- **Statistical Implementations**: Mean, Median, Quartiles (Q1/Q3), Variance, Standard Deviation from scratch.
- **Closures & Scope**: Lexical scoping, nonlocal state persistence, higher-order functions.
- **Decorators**: Function wrappers, signature preservation, execution rate limiters.
- **Data Classes**: `@dataclass`, field mutability, default factories, `field(init=False)`.

---

## Module Breakdown

### Module 00: Starting
*Path: `Python-0-Starting/`*

Covers basic Python mechanics, environment setups, and packaging standards.

- **ex00 (Hello.py)**: Mutability differences across `list`, `tuple`, `set`, and `dict`.
- **ex01 (format_ft_time.py)**: Epoch time handling, datetime formatting, and scientific notation.
- **ex02 (find_ft_type.py)**: Dynamic type identification and printing helper functions.
- **ex03 (NULL_not_found.py)**: Robust detection of empty or null-like values (`None`, `NaN`, `0`, `""`, `False`).
- **ex04 (whatis.py)**: Command-line argument parsing (`sys.argv`) and parity checking with error handling.
- **ex05 (building.py)**: Text parsing, character category categorization (upper, lower, digits, spaces, punctuation).
- **ex06 (ft_filter.py & filterstring.py)**: Re-implementation of `filter()` via list comprehensions and lambda expressions.
- **ex07 (sos.py)**: Morse code encoder implementing dictionary lookups and string sanitation.
- **ex08 (Loading.py)**: Generator-based CLI progress bar replicating `tqdm` using `yield` and terminal carriage returns.
- **ex09 (ft_package/)**: Modern package distribution with `pyproject.toml`, source distribution (`.tar.gz`), and wheel (`.whl`).

---

### Module 01: Array
*Path: `Python-1-Array/`*

Focuses on vectorized computation, multidimensional array operations, and matrix-based image processing.

- **ex00 (give_bmi.py)**: Vectorized BMI calculation and boolean masking for threshold limits using NumPy.
- **ex01 (array2D.py)**: 2D array slicing, shape introspection, and slice boundary validation.
- **ex02 (load_image.py)**: Reading RGB image formats into NumPy arrays and logging dimensional attributes.
- **ex03 (zoom.py)**: Slicing regions of interest, channel reduction, and grayscale visualization.
- **ex04 (rotate.py)**: 90-degree matrix rotation using array transposition without external transformation helpers.
- **ex05 (pimp_image.py)**: Pixel-level arithmetic transformations:
  - Color inversion
  - Green-only / Red-only / Blue-only channel isolation
  - Weighted luminance grayscale calculation

---

### Module 02: DataTable
*Path: `Python-2-DataTable/`*

Covers reading, transforming, and visualizing tabular datasets using Pandas and Matplotlib.

- **ex00 (load_csv.py)**: Safe CSV ingestion, dataset dimension validation, and exception handling.
- **ex01 (aff_life.py)**: Extraction and rendering of historical country life expectancy trends over centuries.
- **ex02 (aff_pop.py)**: Comparative multi-country population timeline visualization with unit parsing (`k`, `M`, `B`).
- **ex03 (projection_life.py)**: Cross-dataset joins and scatter-plot projection comparing GDP per Capita against Life Expectancy.

---

### Module 03: OOP
*Path: `Python-3-OOP/`*

Object-Oriented Programming principles, abstract base classes, inheritance hierarchies, and operator overloading.

- **ex00 (S1E9.py)**: Creation of abstract `Character` base class with `abc.ABC` and concrete character implementations.
- **ex01 (S1E7.py)**: Subclassing, class representation (`__str__`, `__repr__`), and factory class methods.
- **ex02 (DiamondTrap.py)**: Resolving the Diamond Problem in multiple inheritance using Python MRO and property accessors.
- **ex03 (ft_calculator.py)**: Vector-scalar arithmetic using dunder method operator overloading (`+`, `-`, `*`, `/`).
- **ex04 (ft_calculator.py)**: Vector-vector arithmetic (dot product, element-wise addition, subtraction) via `@staticmethod`.

---

### Module 04: Data-Oriented Design (DoD)
*Path: `Python-4-Dod/`*

Advanced language mechanisms, closures, metaprogramming, and structured data classes.

- **ex00 (statistics.py)**: Dynamic statistics calculator processing `*args` and `**kwargs` for Mean, Median, Quartiles, Variance, and Std Dev.
- **ex01 (in_out.py)**: Higher-order functions returning stateful closures for iterative mathematical operations.
- **ex02 (callLimit.py)**: Function execution rate limiter implemented as a parameterized decorator.
- **ex03 (new_student.py)**: Type-safe student data structures using `@dataclass` with field generation and exclusion (`field(init=False)`).

---

## Environment Setup

### Prerequisites
- Python 3.10+
- `pip` and `virtualenv`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/diegoluna/Python-for-Data-Science.git
   cd Python-for-Data-Science
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install numpy pandas matplotlib pillow flake8 build
   ```

---

## Verification & Quality Assurance

All exercises adhere to strict formatting and type guidelines.

### Linting & Formatting
Run `flake8` across the workspace to check compliance:
```bash
flake8 Python-*/
```

### Running Test Scripts
Each exercise includes dedicated test suites (`tester.py`) or entry-point commands. Run an exercise directly from its directory:

```bash
# Example: Running Module 00 Exercise 08 (Progress Bar)
python3 Python-0-Starting/ex08/tester.py

# Example: Running Module 01 Exercise 00 (BMI Calculator)
python3 Python-1-Array/ex00/tester.py

# Example: Running Module 02 Exercise 01 (Life Expectancy Chart)
python3 Python-2-DataTable/ex01/tester.py

# Example: Running Module 03 Exercise 02 (Diamond Inheritance)
python3 Python-3-OOP/ex02/tester.py

# Example: Running Module 04 Exercise 02 (Decorator Rate Limiter)
python3 Python-4-Dod/ex02/tester.py
```

---

## GitHub Repository Configuration

Use the following metadata to configure your GitHub repository settings:

### Description (About Section)
```text
42 School Python for Data Science curriculum: NumPy vectorization, Pandas tabular manipulation, Matplotlib visualization, OOP & MRO architectures, and advanced data-oriented design patterns.
```

### Repository Topics / Tags
Copy and paste these tags into GitHub's **Topics** field:

```text
python, data-science, 42-school, 42, numpy, pandas, matplotlib, oop, data-analysis, data-oriented-design, dataclasses, decorators, python3, algorithms, matrix-operations
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](file:///Users/diegoluna/Documents/42course/Python-for-Data-Science/LICENSE) file for details.
