# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2026-01-31

### Added
- Proper Python package structure with `src/csv_tools/` directory
- `requirements.txt` for dependency management
- `setup.py` for package installation
- Comprehensive bilingual README (English and Chinese)
- Detailed code review documentation
- Console script entry points for all tools
- Module-level and function-level docstrings
- Usage examples in all modules
- Examples directory for configuration templates

### Changed
- **BREAKING**: Reorganized all Python files into `src/csv_tools/` package
- Renamed all files to follow snake_case convention:
  - `Auto-SQL-Query-to-CSV.py` → `auto_sql_query_to_csv.py`
  - `CSV_DataAnalysis.py` → `csv_data_analysis.py`
  - `CSV_Data_Compare.py` → `csv_data_compare.py`
  - `UTF8-to-ANSI_CSV.py` → `utf8_to_ansi_csv.py`
  - `Table_Extractor.py` → `table_extractor.py`
  - `Table_Extractor_Plus.py` → `table_extractor_plus.py`
  - `Table_Extractor_Split.py` → `table_extractor_split.py`
  - `compare_csv.py` → maintained (already correct)
  - `merge_csv.py` → maintained (already correct)
  - `split_csv.py` → maintained (already correct)
- Improved error handling across all modules
- Enhanced user feedback with informative messages
- Standardized configuration file handling
- Improved command-line argument parsing

### Improved
- Code organization and structure
- Documentation quality and completeness
- Consistency in naming conventions
- Error handling and user feedback
- Code readability and maintainability
- Configuration file handling
- Path management with proper OS-independent functions

### Fixed
- Inconsistent naming conventions
- Missing documentation
- Hardcoded paths in some modules
- Encoding handling in various tools
- Error handling edge cases

## [0.6.6] - Previous Version

### Notes
- Original version before comprehensive refactoring
- All core functionality preserved in new version
- Migration guide available in CODE_REVIEW.md

---

## Migration Guide

### For Users

**Old Way** (v0.6.6):
```bash
python compare_csv.py -a file1.csv -b file2.csv
```

**New Way** (v0.7.0):
```bash
# Option 1: Direct module execution
python -m csv_tools.compare_csv -a file1.csv -b file2.csv

# Option 2: After installation (recommended)
pip install -e .
csv-compare -a file1.csv -b file2.csv
```

### For Developers

If you were importing these modules directly:

**Old Way**:
```python
import compare_csv
```

**New Way**:
```python
from csv_tools import compare_csv
# or
import csv_tools.compare_csv
```

---

## Upcoming Features

### Planned for v0.8.0
- Unit tests using pytest
- CI/CD pipeline with GitHub Actions
- Type hints throughout the codebase
- Improved logging system
- Configuration file validation

### Planned for v0.9.0
- Performance optimizations for large files
- Enhanced error recovery
- Additional output formats
- Web-based GUI option

### Planned for v1.0.0
- Complete API documentation
- Comprehensive test coverage (>80%)
- Full internationalization support
- Docker container support
