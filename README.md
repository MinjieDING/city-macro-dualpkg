# city-macro-dualpkg

Minimal monorepo template for distributing the same city macro dataset as both:

- a Python package (`city-macro-data`)
- an R package (`citymacrodata`)

## Repository layout

- `data-src/`: raw source files (Excel)
- `build-data/`: one build script to standardize data
- `dist-data/`: canonical outputs (`city_macro.csv`, `metadata.json`)
- `python-pkg/`: installable Python package
- `r-pkg/`: installable R package
- `scripts/sync_packages.ps1`: copy `dist-data` into both packages

## Quick start

1. Put your Excel file in `data-src/` (default name: `city_macro.xlsx`).
2. Build standard data:
   - `python build-data/build_data.py`
3. Sync data to Python and R packages:
   - `powershell -ExecutionPolicy Bypass -File scripts/sync_packages.ps1`
4. Install Python package locally:
   - `pip install -e python-pkg`
5. Build/check R package:
   - `R CMD build r-pkg`
   - `R CMD check citymacrodata_0.1.0.tar.gz`

## API parity

- Python: `load_data()`, `get_metadata()`, `data_version()`
- R: `load_data()`, `get_metadata()`, `data_version()`
