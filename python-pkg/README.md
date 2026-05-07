# city-macro-data

`city-macro-data` is a distributable dataset package for city-level macro data.

## Installation

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
print(validate_data())
```

## API

- `load_data()`: return dataset as `pandas.DataFrame`
- `get_metadata()`: return metadata from `metadata.json`
- `data_version()`: return dataset version string
- `validate_data(required_columns=None)`: validate non-empty data and required columns

## Data Update Workflow (for maintainers)

From repository root:

```bash
python build-data/build_data.py
powershell -ExecutionPolicy Bypass -File scripts/sync_packages.ps1
python -m pip install --force-reinstall .\python-pkg
```

## Notes for Windows Users

Avoid editable install (`pip install -e`) under non-ASCII paths. Use normal install:

```bash
python -m pip install .\python-pkg
```
