#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Table Extractor Plus

This module extracts rows from a CSV file based on specific column values,
and also outputs non-matching rows to a separate file.

Usage:
    python -m csv_tools.table_extractor_plus -c config.conf
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
    
    output_file = config.get('File', 'output_file', 
                            fallback=os.path.join(os.getcwd(), 'output.csv'))
    output_encoding = config.get('File', 'output_encoding', fallback='utf-8')
    
    return {
        'input_file': config.get('File', 'input_file', 
                                fallback=os.path.join(os.getcwd(), 'input.csv')),
        'output_file': output_file,
        'input_encoding': config.get('File', 'input_encoding', fallback='utf-8'),
        'output_encoding': output_encoding,
        'column': config.get('Filter', 'column'),
        'values': [x.strip() for x in config.get('Filter', 'values').split(',')],
        'output_file_other': config.get('File', 'output_file_other', 
                                       fallback=output_file.rsplit('.', 1)[0] + '_other.csv'),
        'output_encoding_other': config.get('File', 'output_encoding_other', 
                                           fallback=output_encoding)
    }


def extract_table_data_split(input_file, output_file, output_file_other,
                             column, values, 
                             input_encoding='utf-8', 
                             output_encoding='utf-8',
                             output_encoding_other='utf-8'):
    """
    Extract rows from CSV, splitting into matching and non-matching files.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file for matching rows
        output_file_other (str): Path to output CSV file for non-matching rows
        column (str): Column name to filter on
        values (list): List of values to match
        input_encoding (str): Input file encoding (default: 'utf-8')
        output_encoding (str): Output file encoding for matches (default: 'utf-8')
        output_encoding_other (str): Output file encoding for non-matches (default: 'utf-8')
        
    Returns:
        tuple: (num_matching, num_non_matching) - Number of rows in each category
    """
    print('Reading data...')
    df = pd.read_csv(input_file, encoding=input_encoding)
    print(f'Data read complete. Total rows: {len(df)}')
    
    print('Filtering data...')
    df_filtered = df[df[column].isin(values)]
    df_filtered_other = df[~df[column].isin(values)]
    print(f'Filtering complete.')
    print(f'  Matching rows: {len(df_filtered)}')
    print(f'  Non-matching rows: {len(df_filtered_other)}')
    
    print('Writing matching data...')
    df_filtered.to_csv(output_file, index=False, encoding=output_encoding)
    print(f'Matching data written to {output_file}')
    
    print('Writing non-matching data...')
    df_filtered_other.to_csv(output_file_other, index=False, 
                             encoding=output_encoding_other)
    print(f'Non-matching data written to {output_file_other}')
    
    return len(df_filtered), len(df_filtered_other)


def main():
    """Main entry point for the table extractor plus tool."""
    parser = argparse.ArgumentParser(
        description='Extract rows from CSV and separate matching/non-matching data'
    )
    parser.add_argument('-c', '--config', type=str, 
                       default='Table_Extractor.conf',
                       help='Path to configuration file (default: Table_Extractor.conf)')
    
    args = parser.parse_args()
    
    # Read configuration
    config = read_config(args.config)
    
    # Extract and split data
    extract_table_data_split(
        config['input_file'],
        config['output_file'],
        config['output_file_other'],
        config['column'],
        config['values'],
        config['input_encoding'],
        config['output_encoding'],
        config['output_encoding_other']
    )


if __name__ == '__main__':
    main()
