#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CSV-Tools Setup Configuration
A collection of utilities for CSV file processing and manipulation.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
def read_file(filename):
    """Read file contents."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

setup(
    name='csv-tools',
    version='0.7.0',
    description='A collection of utilities for CSV file processing and manipulation',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='BlueSkyXN',
    url='https://github.com/BlueSkyXN/CSV-Tools',
    license='GPL-3.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas>=1.5.0',
        'openpyxl>=3.0.0',
        'pymysql>=1.0.0',
        'tqdm>=4.65.0',
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
    entry_points={
        'console_scripts': [
            'csv-merge=csv_tools.merge_csv:main',
            'csv-split=csv_tools.split_csv:main',
            'csv-compare=csv_tools.compare_csv:main',
            'csv-utf8-to-ansi=csv_tools.utf8_to_ansi_csv:main',
            'csv-data-analysis=csv_tools.csv_data_analysis:main',
            'csv-data-compare=csv_tools.csv_data_compare:main',
            'csv-table-extractor=csv_tools.table_extractor:main',
            'csv-table-extractor-plus=csv_tools.table_extractor_plus:main',
            'csv-table-extractor-split=csv_tools.table_extractor_split:main',
            'csv-sql-query=csv_tools.auto_sql_query_to_csv:main',
        ],
    },
)
