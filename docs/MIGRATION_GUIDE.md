# Migration Guide: v0.6.6 to v0.7.0

This guide helps you migrate from the old flat structure (v0.6.6) to the new package structure (v0.7.0).

## What Changed?

### Structure Changes

**Before (v0.6.6):**
```
CSV-Tools/
├── compare_csv.py
├── merge_csv.py
├── Auto-SQL-Query-to-CSV.py
└── ... (all .py files in root)
```

**After (v0.7.0):**
```
CSV-Tools/
├── src/csv_tools/          # New package directory
│   ├── compare_csv.py
│   ├── merge_csv.py
│   ├── auto_sql_query_to_csv.py
│   └── ... (all modules here)
├── examples/               # Configuration templates
├── docs/                   # Documentation
└── tests/                  # Test files
```

### File Name Changes

All files now use snake_case naming:

| Old Name | New Name |
|----------|----------|
| `Auto-SQL-Query-to-CSV.py` | `auto_sql_query_to_csv.py` |
| `CSV_DataAnalysis.py` | `csv_data_analysis.py` |
| `CSV_Data_Compare.py` | `csv_data_compare.py` |
| `UTF8-to-ANSI_CSV.py` | `utf8_to_ansi_csv.py` |
| `Table_Extractor.py` | `table_extractor.py` |
| `Table_Extractor_Plus.py` | `table_extractor_plus.py` |
| `Table_Extractor_Split.py` | `table_extractor_split.py` |
| `compare_csv.py` | `compare_csv.py` (unchanged) |
| `merge_csv.py` | `merge_csv.py` (unchanged) |
| `split_csv.py` | `split_csv.py` (unchanged) |

## Migration Steps

### For Users

#### Option 1: Use the New Package Structure (Recommended)

1. **Update your repository:**
```bash
cd CSV-Tools
git pull origin main
```

2. **Install the package:**
```bash
pip install -e .
```

3. **Use the new command-line tools:**
```bash
# Old way
python compare_csv.py -a file1.csv -b file2.csv

# New way - Option A (module execution)
python -m csv_tools.compare_csv -a file1.csv -b file2.csv

# New way - Option B (console scripts)
csv-compare -a file1.csv -b file2.csv
```

#### Option 2: Continue Using Old Files (Temporary)

The old Python files are still in the root directory for backward compatibility. However:
- ⚠️ These files are **deprecated** and will be removed in v1.0.0
- 🔄 Please migrate to the new structure as soon as possible
- ❌ Old files will not receive updates or bug fixes

### For Developers

#### Updating Import Statements

**Before:**
```python
import compare_csv
import merge_csv
from CSV_DataAnalysis import read_csv
```

**After:**
```python
from csv_tools import compare_csv, merge_csv
from csv_tools.csv_data_analysis import read_csv

# Or
import csv_tools.compare_csv
import csv_tools.merge_csv
```

#### Updating Scripts

**Before:**
```python
#!/usr/bin/env python
import compare_csv

compare_csv.compare_csv_files('a.csv', 'b.csv', 'out.csv', 'name')
```

**After:**
```python
#!/usr/bin/env python
from csv_tools import compare_csv

compare_csv.compare_csv_files('a.csv', 'b.csv', 'out.csv', 'name')
```

### For CI/CD Pipelines

#### Using GitHub Actions

**Before:**
```yaml
- name: Run comparison
  run: python compare_csv.py -a file1.csv -b file2.csv
```

**After:**
```yaml
- name: Install CSV-Tools
  run: pip install -e .

- name: Run comparison
  run: csv-compare -a file1.csv -b file2.csv
```

## New Features in v0.7.0

### Console Commands

After installation, you can use these commands directly:

```bash
csv-compare        # Compare two CSV files
csv-merge          # Merge multiple CSV files
csv-split          # Split large CSV files
csv-utf8-to-ansi   # Convert encoding
csv-data-analysis  # Data analysis tool
csv-data-compare   # Data comparison tool
csv-table-extractor      # Extract table data
csv-table-extractor-plus # Extract with split output
csv-table-extractor-split # Extract and split by value
csv-sql-query      # SQL to CSV conversion
```

### Improved Documentation

- Comprehensive README with examples
- Function docstrings throughout
- Usage examples in all modules
- Configuration templates in `examples/`

### Better Error Handling

All tools now provide:
- Clear error messages
- Better validation
- Informative progress updates

## Troubleshooting

### Issue: "Module not found" error

**Solution:**
```bash
# Make sure you've installed the package
pip install -e .

# Or update your Python path
export PYTHONPATH="${PYTHONPATH}:/path/to/CSV-Tools/src"
```

### Issue: Old scripts don't work

**Solution:**
The old files are still in the root directory. They should work as before, but please migrate to the new structure.

### Issue: Configuration files not found

**Solution:**
Configuration templates are now in `examples/` directory:
```bash
cp examples/CSV_DataAnalysis-template.conf CSV_DataAnalysis.conf
# Edit the configuration file as needed
```

## Timeline

- **v0.7.0** (Current): Both old and new structures available
- **v0.8.0** (Planned): Deprecation warnings for old files
- **v1.0.0** (Future): Old files removed, only package structure available

## Need Help?

If you encounter issues during migration:
1. Check this guide
2. Review the [README.md](README.md)
3. Check [CONTRIBUTING.md](CONTRIBUTING.md) for development setup
4. Open an issue on GitHub

## Benefits of Migrating

- ✅ Better code organization
- ✅ Easier installation and distribution
- ✅ Console commands for convenience
- ✅ Better documentation
- ✅ Active maintenance and updates
- ✅ Consistent naming conventions
- ✅ Improved error handling

Start migrating today to take advantage of these improvements!
