#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CSV Tools Package
A collection of utilities for CSV file processing and manipulation.
"""

__version__ = '0.7.0'
__author__ = 'BlueSkyXN'
__license__ = 'GPL-3.0'

# Import main modules for easier access
from . import compare_csv
from . import merge_csv
from . import split_csv
from . import utf8_to_ansi_csv
from . import csv_data_analysis
from . import csv_data_compare
from . import table_extractor
from . import table_extractor_plus
from . import table_extractor_split
from . import auto_sql_query_to_csv

__all__ = [
    'compare_csv',
    'merge_csv',
    'split_csv',
    'utf8_to_ansi_csv',
    'csv_data_analysis',
    'csv_data_compare',
    'table_extractor',
    'table_extractor_plus',
    'table_extractor_split',
    'auto_sql_query_to_csv',
]
