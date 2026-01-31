#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Table Extractor Split

This module extracts rows from a CSV file based on specific column values,
and creates separate output files for each unique value.

Usage:
    python -m csv_tools.table_extractor_split -c config.conf
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


def extract_and_split_by_value(input_file, output_file, column, values, 
                                input_encoding='utf-8', output_encoding='utf-8'):
    """
    Extract rows from CSV and create separate files for each value.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Base path for output CSV files
        column (str): Column name to filter on
        values (list): List of values to match
        input_encoding (str): Input file encoding (default: 'utf-8')
        output_encoding (str): Output file encoding (default: 'utf-8')
        
    Returns:
        dict: Dictionary mapping values to number of rows extracted
    """
    print('Reading data...')
    df = pd.read_csv(input_file, encoding=input_encoding)
    print(f'Data read complete. Total rows: {len(df)}')
    
    print('Filtering data...')
    df_filtered = df[df[column].isin(values)]
    print(f'Filtering complete. Filtered rows: {len(df_filtered)}')
    
    print('Writing combined data...')
    df_filtered.to_csv(output_file, index=False, encoding=output_encoding)
    print(f'Combined data written to {output_file}')
    
    # Generate individual files for each value
    output_dir, output_filename = os.path.split(output_file)
    output_basename, output_ext = os.path.splitext(output_filename)
    
    value_counts = {}
    print('\nGenerating individual files for each value...')
    
    for value in values:
        df_value = df[df[column] == value]
        if len(df_value) > 0:
            output_file_value = os.path.join(output_dir, 
                                            f"{output_basename}_{value}{output_ext}")
            df_value.to_csv(output_file_value, index=False, encoding=output_encoding)
            value_counts[value] = len(df_value)
            print(f'  {value}: {len(df_value)} rows -> {output_file_value}')
        else:
            print(f'  {value}: No rows found')
            value_counts[value] = 0
    
    return value_counts


def main():
    """Main entry point for the table extractor split tool."""
    parser = argparse.ArgumentParser(
        description='Extract rows from CSV and create separate files for each value'
    )
    parser.add_argument('-c', '--config', type=str, 
                       default='Table_Extractor.conf',
                       help='Path to configuration file (default: Table_Extractor.conf)')
    
    args = parser.parse_args()
    
    # Read configuration
    config = read_config(args.config)
    
    # Extract and split data
    extract_and_split_by_value(
        config['input_file'],
        config['output_file'],
        config['column'],
        config['values'],
        config['input_encoding'],
        config['output_encoding']
    )


if __name__ == '__main__':
    main()
