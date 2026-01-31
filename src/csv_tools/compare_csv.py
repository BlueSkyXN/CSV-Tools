#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CSV Comparison Tool

This module provides functionality to compare two CSV files and identify
rows that don't match based on a specific column.

Usage:
    python -m csv_tools.compare_csv -a file1.csv -b file2.csv -c output.csv -d column_name
"""

import argparse
import pandas as pd


def compare_csv_files(file_a, file_b, output_file, match_column):
    """
    Compare two CSV files and output non-matching rows.
    
    Args:
        file_a (str): Path to the first CSV file
        file_b (str): Path to the second CSV file
        output_file (str): Path to the output CSV file
        match_column (str): Column name to use for matching
        
    Returns:
        None
    """
    # Read CSV files
    df_a = pd.read_csv(file_a)
    df_b = pd.read_csv(file_b)
    
    # Perform outer merge and identify non-matching rows
    df = df_a.merge(df_b, how='outer', left_on=match_column, 
                    right_on=match_column, indicator=True)
    
    # Extract non-matching rows
    output = df[df['_merge'] != 'both']
    
    # Write to output CSV file
    output.to_csv(output_file, index=False)
    print(f"Comparison complete. Non-matching rows saved to {output_file}")


def main():
    """Main entry point for the CSV comparison tool."""
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='Compare two CSV files and identify non-matching rows'
    )
    
    # Add arguments
    parser.add_argument('-a', '--file-a', default='A.csv',
                       help='Path to the first input CSV file (default: A.csv)')
    parser.add_argument('-b', '--file-b', default='B.csv',
                       help='Path to the second input CSV file (default: B.csv)')
    parser.add_argument('-c', '--output', default='Output.csv',
                       help='Path to the output CSV file (default: Output.csv)')
    parser.add_argument('-d', '--column', default='name',
                       help='Column to be matched (default: name)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Execute comparison
    compare_csv_files(args.file_a, args.file_b, args.output, args.column)


if __name__ == '__main__':
    main()
