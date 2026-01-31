#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CSV Data Comparison Tool

This module compares two CSV files to identify unresolved and new records
based on a unique identifier column.

Usage:
    python -m csv_tools.csv_data_compare -c config.conf
"""

import argparse
import configparser
import pandas as pd


def read_config(config_file):
    """
    Read configuration file for CSV comparison.
    
    Args:
        config_file (str): Path to the configuration file
        
    Returns:
        tuple: Configuration parameters for input/output files and keys
    """
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    
    # Input File 1 settings
    input_file_1_path = config.get('Input_File_1', 'path', fallback='input1.csv')
    input_file_1_encoding = config.get('Input_File_1', 'encoding', fallback='UTF-8')
    key_1 = config.get('Input_File_1', 'key')
    
    # Input File 2 settings
    input_file_2_path = config.get('Input_File_2', 'path', fallback='input2.csv')
    input_file_2_encoding = config.get('Input_File_2', 'encoding', fallback='UTF-8')
    key_2 = config.get('Input_File_2', 'key')
    
    # Output File 1 settings (unresolved records)
    output_file_1_path = config.get('Output_File_1', 'path', fallback='output1.csv')
    output_file_1_encoding = config.get('Output_File_1', 'encoding', fallback='UTF-8')
    
    # Output File 2 settings (new records)
    output_file_2_path = config.get('Output_File_2', 'path', fallback='output2.csv')
    output_file_2_encoding = config.get('Output_File_2', 'encoding', fallback='UTF-8')
    
    return (input_file_1_path, input_file_1_encoding, key_1,
            input_file_2_path, input_file_2_encoding, key_2,
            output_file_1_path, output_file_1_encoding,
            output_file_2_path, output_file_2_encoding)


def compare_csv_data(df1, key_1, df2, key_2):
    """
    Compare two dataframes and identify unresolved and new records.
    
    Args:
        df1 (pd.DataFrame): First dataframe
        key_1 (str): Key column in first dataframe
        df2 (pd.DataFrame): Second dataframe
        key_2 (str): Key column in second dataframe
        
    Returns:
        tuple: (unresolved_df, new_df) - DataFrames for unresolved and new records
    """
    # Find unresolved records (keys present in both files)
    common_keys = set(df1[key_1]).intersection(set(df2[key_2]))
    unresolved_df = df2[df2[key_2].isin(common_keys)]
    
    # Find new records (keys in df2 but not in df1)
    new_keys = set(df2[key_2]) - set(df1[key_1])
    new_df = df2[df2[key_2].isin(new_keys)]
    
    return unresolved_df, new_df


def main():
    """Main entry point for CSV data comparison tool."""
    parser = argparse.ArgumentParser(
        description='Compare two CSV files to identify unresolved and new records'
    )
    parser.add_argument('-c', '--config', type=str, 
                       default='CSV_Data_Compare.conf',
                       help='Path to configuration file (default: CSV_Data_Compare.conf)')
    
    args = parser.parse_args()
    
    # Read configuration
    (input_file_1_path, input_file_1_encoding, key_1,
     input_file_2_path, input_file_2_encoding, key_2,
     output_file_1_path, output_file_1_encoding,
     output_file_2_path, output_file_2_encoding) = read_config(args.config)
    
    # Read input CSV files
    print(f"Reading {input_file_1_path}...")
    df1 = pd.read_csv(input_file_1_path, encoding=input_file_1_encoding)
    
    print(f"Reading {input_file_2_path}...")
    df2 = pd.read_csv(input_file_2_path, encoding=input_file_2_encoding)
    
    # Compare data
    print("Comparing data...")
    unresolved_df, new_df = compare_csv_data(df1, key_1, df2, key_2)
    
    # Save results
    print(f"Saving unresolved records to {output_file_1_path}...")
    unresolved_df.to_csv(output_file_1_path, encoding=output_file_1_encoding, 
                         index=False)
    
    print(f"Saving new records to {output_file_2_path}...")
    new_df.to_csv(output_file_2_path, encoding=output_file_2_encoding, 
                  index=False)
    
    print(f"\nComparison complete!")
    print(f"  Unresolved records: {len(unresolved_df)}")
    print(f"  New records: {len(new_df)}")


if __name__ == '__main__':
    main()
