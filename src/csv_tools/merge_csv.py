#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CSV Merge Tool

This module provides functionality to merge multiple CSV files from a directory
into a single output file.

Usage:
    python -m csv_tools.merge_csv -i input_directory -o output.csv
"""

import argparse
import os
import pandas as pd


def merge_csv_files(input_dir, output_file, file_prefix='output_'):
    """
    Merge multiple CSV files from a directory into a single file.
    
    Args:
        input_dir (str): Path to the directory containing CSV files
        output_file (str): Path to the output merged CSV file
        file_prefix (str): Prefix to filter CSV files (default: 'output_')
        
    Returns:
        int: Number of files merged
    """
    # List all CSV files with the specified prefix
    files = [f for f in os.listdir(input_dir) 
             if f.startswith(file_prefix) and f.endswith('.csv')]
    
    if not files:
        print(f"No CSV files found with prefix '{file_prefix}' in {input_dir}")
        return 0
    
    # Read all CSV files and merge them
    dfs = []
    for file in files:
        path = os.path.join(input_dir, file)
        df = pd.read_csv(path)
        dfs.append(df)
    
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Save merged data to output file
    merged_df.to_csv(output_file, index=False)
    print(f"Merged {len(dfs)} CSV files into {output_file}")
    
    return len(dfs)


def main():
    """Main entry point for the CSV merge tool."""
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='Merge multiple CSV files into a single file'
    )
    
    # Add arguments
    parser.add_argument('-i', '--input-dir', type=str, required=True,
                       help='Input directory path containing CSV files')
    parser.add_argument('-o', '--output-file', type=str, required=True,
                       help='Output file path for merged CSV')
    parser.add_argument('-p', '--prefix', type=str, default='output_',
                       help='File prefix to filter CSV files (default: output_)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Execute merge
    merge_csv_files(args.input_dir, args.output_file, args.prefix)


if __name__ == '__main__':
    main()
