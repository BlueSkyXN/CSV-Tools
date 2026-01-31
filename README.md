# CSV-Tools

[English](#english) | [中文](#chinese)

---

<a name="english"></a>
## English

A comprehensive collection of Python utilities for CSV file processing and manipulation.

### Features

- **CSV Comparison**: Compare two CSV files and identify non-matching rows
- **CSV Merging**: Merge multiple CSV files into a single file
- **CSV Splitting**: Split large CSV files into smaller chunks
- **Encoding Conversion**: Convert CSV files from UTF-8 to ANSI encoding
- **Data Analysis**: Perform comparative analysis on CSV datasets
- **Data Comparison**: Identify unresolved and new records between datasets
- **Table Extraction**: Filter and extract specific rows from CSV files
- **SQL to CSV**: Execute SQL queries and export results to CSV

### Installation

#### From Source

```bash
# Clone the repository
git clone https://github.com/BlueSkyXN/CSV-Tools.git
cd CSV-Tools

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

#### Install Dependencies Only

```bash
pip install -r requirements.txt
```

### Requirements

- Python 3.7+
- pandas >= 1.5.0
- openpyxl >= 3.0.0
- pymysql >= 1.0.0
- tqdm >= 4.65.0

### Usage

#### 1. CSV Comparison

Compare two CSV files and output non-matching rows:

```bash
python -m csv_tools.compare_csv -a file1.csv -b file2.csv -c output.csv -d column_name
```

Options:
- `-a, --file-a`: Path to first CSV file (default: A.csv)
- `-b, --file-b`: Path to second CSV file (default: B.csv)
- `-c, --output`: Path to output CSV file (default: Output.csv)
- `-d, --column`: Column name for matching (default: name)

#### 2. CSV Merging

Merge multiple CSV files from a directory:

```bash
python -m csv_tools.merge_csv -i input_directory -o output.csv -p output_
```

Options:
- `-i, --input-dir`: Input directory containing CSV files (required)
- `-o, --output-file`: Output merged CSV file (required)
- `-p, --prefix`: File prefix to filter (default: output_)

#### 3. CSV Splitting

Split a large CSV file into smaller chunks:

```bash
python -m csv_tools.split_csv -i input.csv -o output_dir -s 100000
```

Options:
- `-i, --input`: Input CSV file path (default: ~/Desktop/input.csv)
- `-o, --output`: Output directory path (default: ~/Desktop/output/)
- `-s, --chunk-size`: Rows per chunk (default: 200000)

#### 4. UTF-8 to ANSI Conversion

Convert CSV from UTF-8 to ANSI encoding:

```bash
python -m csv_tools.utf8_to_ansi_csv -i input.csv -o output.csv
```

Options:
- `-i, --input`: Input UTF-8 CSV file (required)
- `-o, --output`: Output ANSI CSV file (required)

#### 5. CSV Data Analysis

Perform comparative analysis on CSV datasets:

```bash
python -m csv_tools.csv_data_analysis -c config.conf
```

Options:
- `-c, --config`: Configuration file path (default: CSV_DataAnalysis.conf)

Configuration file should contain settings for input files, department classification, and output format.

#### 6. CSV Data Comparison

Compare two CSV files to identify unresolved and new records:

```bash
python -m csv_tools.csv_data_compare -c config.conf
```

Options:
- `-c, --config`: Configuration file path (default: CSV_Data_Compare.conf)

#### 7. Table Extractor

Extract specific rows from CSV based on column values:

```bash
python -m csv_tools.table_extractor -c config.conf
```

Options:
- `-c, --config`: Configuration file path (default: Table_Extractor.conf)

#### 8. Table Extractor Plus

Extract rows and separate matching/non-matching data:

```bash
python -m csv_tools.table_extractor_plus -c config.conf
```

Options:
- `-c, --config`: Configuration file path (default: Table_Extractor.conf)

#### 9. Table Extractor Split

Extract rows and create separate files for each value:

```bash
python -m csv_tools.table_extractor_split -c config.conf
```

Options:
- `-c, --config`: Configuration file path (default: Table_Extractor.conf)

#### 10. SQL Query to CSV

Execute SQL queries and export to CSV:

```bash
# Execute query
python -m csv_tools.auto_sql_query_to_csv -q query.sql -i db_info.txt -o output.csv -e utf-8

# Generate sample files
python -m csv_tools.auto_sql_query_to_csv -s
```

Options:
- `-q, --query`: SQL query file path
- `-i, --input, --info`: Database connection info file
- `-o, --output`: Output CSV file path
- `-e, --encoding`: Output encoding (utf-8/utf8/u or ansi/a, default: utf-8)
- `-s, --sample`: Generate example input files

### Project Structure

```
CSV-Tools/
├── src/
│   └── csv_tools/          # Main package directory
│       ├── __init__.py     # Package initialization
│       ├── compare_csv.py  # CSV comparison tool
│       ├── merge_csv.py    # CSV merging tool
│       ├── split_csv.py    # CSV splitting tool
│       └── ...             # Other tools
├── examples/               # Example configuration files
├── docs/                   # Documentation
├── tests/                  # Unit tests
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup file
└── README.md              # This file
```

### Configuration Files

Example configuration files are provided in the root directory with `-template.conf` suffix:
- `CSV_DataAnalysis-template.conf`
- `CSV_Data_Compare-template.conf`
- `Table_Extractor-template.conf`

Copy these templates and modify them according to your needs.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

### Related Projects

- [json-to-csv](https://github.com/BlueSkyXN/json-to-csv) - Tools for processing AdguardHome QueryLog data
- [Auto-SQL-Query-to-CSV](https://github.com/BlueSkyXN/Auto-SQL-Query-to-CSV) - Database query extraction tools
- [CSV-BigData-Tools](https://github.com/BlueSkyXN/CSV-BigData-Tools) - CSV data analysis tools

---

<a name="chinese"></a>
## 中文

面向CSV文件开发的实用工具集合。

### 功能特性

- **CSV比较**：比较两个CSV文件并识别不匹配的行
- **CSV合并**：将多个CSV文件合并为单个文件
- **CSV拆分**：将大型CSV文件拆分为较小的块
- **编码转换**：将CSV文件从UTF-8转换为ANSI编码
- **数据分析**：对CSV数据集执行比较分析
- **数据对比**：识别数据集之间未解决和新增的记录
- **表格提取**：根据列值筛选和提取CSV文件中的特定行
- **SQL转CSV**：执行SQL查询并将结果导出为CSV

### 安装

#### 从源码安装

```bash
# 克隆仓库
git clone https://github.com/BlueSkyXN/CSV-Tools.git
cd CSV-Tools

# 安装依赖
pip install -r requirements.txt

# 安装包
pip install -e .
```

#### 仅安装依赖

```bash
pip install -r requirements.txt
```

### 系统要求

- Python 3.7+
- pandas >= 1.5.0
- openpyxl >= 3.0.0
- pymysql >= 1.0.0
- tqdm >= 4.65.0

### 使用方法

详细的使用说明请参考英文文档部分。

### 项目结构

```
CSV-Tools/
├── src/
│   └── csv_tools/          # 主包目录
│       ├── __init__.py     # 包初始化
│       ├── compare_csv.py  # CSV比较工具
│       ├── merge_csv.py    # CSV合并工具
│       ├── split_csv.py    # CSV拆分工具
│       └── ...             # 其他工具
├── examples/               # 示例配置文件
├── docs/                   # 文档
├── tests/                  # 单元测试
├── requirements.txt        # Python依赖
├── setup.py               # 包安装文件
└── README.md              # 本文件
```

### 配置文件

根目录下提供了带有 `-template.conf` 后缀的示例配置文件：
- `CSV_DataAnalysis-template.conf`
- `CSV_Data_Compare-template.conf`
- `Table_Extractor-template.conf`

复制这些模板并根据您的需求进行修改。

### 贡献

欢迎贡献！请随时提交Pull Request。

### 许可证

本项目采用GNU通用公共许可证v3.0 - 详见 [LICENSE](LICENSE) 文件。

### 关联项目

- [json-to-csv](https://github.com/BlueSkyXN/json-to-csv) - 处理AdguardHome的QueryLog数据的工具
- [Auto-SQL-Query-to-CSV](https://github.com/BlueSkyXN/Auto-SQL-Query-to-CSV) - 从数据库查询提取数据的工具
- [CSV-BigData-Tools](https://github.com/BlueSkyXN/CSV-BigData-Tools) - 分析CSV数据的工具
