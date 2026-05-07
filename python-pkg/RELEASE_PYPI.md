# Python Package Release Guide

This document is the release template for `city-macro-data`.

## 0) Prerequisites

- Have a PyPI account: <https://pypi.org/>
- (Recommended) Have a TestPyPI account: <https://test.pypi.org/>
- Create API tokens in account settings.

Set token in shell (PowerShell):

```powershell
$env:TWINE_USERNAME="__token__"
$env:TWINE_PASSWORD="pypi-xxxx-your-token"
```

## 1) Bump version

From repository root:

```powershell
python scripts/bump_python_version.py patch
```

Use `minor` / `major` when needed.

## 2) Build and check

```powershell
powershell -ExecutionPolicy Bypass -File scripts/python_build_and_check.ps1
```

This runs:
- `python -m build python-pkg`
- `python -m twine check python-pkg/dist/*`

## 3) Publish command templates

### Publish to TestPyPI first (recommended)

```powershell
python -m twine upload --repository-url https://test.pypi.org/legacy/ python-pkg/dist/*
```

Install test package:

```powershell
pip install -i https://test.pypi.org/simple/ city-macro-data
```

### Publish to PyPI (public)

```powershell
python -m twine upload python-pkg/dist/*
```

Install from public PyPI:

```powershell
pip install city-macro-data
```

## 4) Post-release checks

- Verify package page on PyPI
- Install in a clean virtual environment
- Run:

```powershell
python -c "from city_macro_data import load_data, validate_data; print(load_data().shape); print(validate_data())"
```
