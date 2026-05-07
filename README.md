# city-macro-data

`city-macro-data` is a Python package for distributing China's city-level macroeconomic data.  
After installation, you can directly load the built-in dataset, inspect metadata, and run basic data validation. It is suitable for teaching, coursework, and quick starts for empirical analysis.

## Contents

- Standardized city panel dataset (CSV)
- Matching metadata (JSON), including data version, build time, and field information
- A concise and stable Python API

## Installation

Install from PyPI (available after release):

```bash
pip install city-macro-data
```

## Quick Start

```python
from city_macro_data import load_data, get_metadata, data_version, validate_data

df = load_data()
meta = get_metadata()

print(df.shape)
print(data_version())
print(meta.keys())

# Basic validation (non-empty checks, required columns, etc.)
validate_data()
```

## Main API

- `load_data()`: Load data and return a `pandas.DataFrame`
- `get_metadata()`: Load metadata and return a dictionary
- `data_version()`: Return the current data version
- `validate_data(required_columns=None)`: Run basic data quality checks

## Example Fields

The dataset includes indicators such as year, city, GDP, resident population, industrial structure, and fiscal revenue/expenditure.  
Please use the column names in the output of `load_data()` as the source of truth.

## Citation and Author ID

- Repository: [MinjieDING/city-macro-dualpkg](https://github.com/MinjieDING/city-macro-dualpkg)
- ORCID: [0000-0002-9673-1072](https://orcid.org/0000-0002-9673-1072)
- Citation metadata is provided in `CITATION.cff`.
