#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Table Extractor

This module extracts rows from a CSV file based on specific column values.

Usage:
    python -m csv_tools.table_extractor -c config.conf
"""

import argparse
import configparser
import os
import pandas as pd


def read_config(config_file='Table_Extractor.conf'):
    """
    Read configuration file for table extraction.
    
    Args:
        config_file (str): Path to configuration file
        
    Returns:
        dict: Configuration parameters
    """
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    
    return {
        'input_file': config.get('File', 'input_file', 
                                fallback=os.path.join(os.getcwd(), 'input.csv')),
        'output_file': config.get('File', 'output_file', 
                                 fallback=os.path.join(os.getcwd(), 'output.csv')),
        'input_encoding': config.get('File', 'input_encoding', fallback='utf-8'),
        'output_encoding': config.get('File', 'output_encoding', fallback='utf-8'),
        'column': config.get('Filter', 'column'),
        'values': [x.strip() for x in config.get('Filter', 'values').split(',')]
    }


def extract_table_data(input_file, output_file, column, values, 
                      input_encoding='utf-8', output_encoding='utf-8'):
    """
    Extract rows from CSV where column matches specified values.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
        column (str): Column name to filter on
        values (list): List of values to match
        input_encoding (str): Input file encoding (default: 'utf-8')
        output_encoding (str): Output file encoding (default: 'utf-8')
        
    Returns:
        int: Number of rows extracted
    """
    print('Reading data...')
    df = pd.read_csv(input_file, encoding=input_encoding)
    print(f'Data read complete. Total rows: {len(df)}')
    
    print('Filtering data...')
    df_filtered = df[df[column].isin(values)]
    print(f'Filtering complete. Filtered rows: {len(df_filtered)}')
    
    print('Writing data...')
    df_filtered.to_csv(output_file, index=False, encoding=output_encoding)
    print(f'Data written to {output_file}')
    
    return len(df_filtered)


def main():
    """Main entry point for the table extractor tool."""
    parser = argparse.ArgumentParser(
        description='Extract rows from CSV based on column values'
    )
    parser.add_argument('-c', '--config', type=str, 
                       default='Table_Extractor.conf',
                       help='Path to configuration file (default: Table_Extractor.conf)')
    
    args = parser.parse_args()
    
    # Read configuration
    config = read_config(args.config)
    
    # Extract data
    extract_table_data(
        config['input_file'],
        config['output_file'],
        config['column'],
        config['values'],
        config['input_encoding'],
        config['output_encoding']
    )


if __name__ == '__main__':
    main()
