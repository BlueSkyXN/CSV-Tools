#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CSV Split Tool

This module provides functionality to split a large CSV file into smaller chunks.
Useful for processing large datasets that may be difficult to handle as a single file.

Usage:
    python -m csv_tools.split_csv -i input.csv -o output_dir -s 100000
"""

import argparse
import os
import pandas as pd
from tqdm import tqdm


def split_csv_file(input_file, output_dir, chunk_size=200000):
    """
    Split a CSV file into smaller chunks.
    
    Args:
        input_file (str): Path to the input CSV file
        output_dir (str): Path to the output directory for chunk files
        chunk_size (int): Number of rows per chunk (default: 200000)
        
    Returns:
        list: List of output file paths
    """
    # Expand user home directory if present
    input_file = os.path.expanduser(input_file)
    output_dir = os.path.expanduser(output_dir)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read CSV file in chunks
    df_reader = pd.read_csv(input_file, chunksize=chunk_size)
    
    # Process each chunk
    file_names = []
    file_sizes = []
    
    for i, chunk in enumerate(tqdm(df_reader, desc="Splitting CSV")):
        # Determine output file path
        output_path = os.path.join(output_dir, f"output_{i}.csv")
        
        # Save chunk as CSV file
        chunk.to_csv(output_path, index=False)
        
        # Record file info
        file_names.append(output_path)
        file_sizes.append(os.path.getsize(output_path))
    
    # Print summary
    print("\nGenerated files:")
    for i, fn in enumerate(file_names):
        size_mb = file_sizes[i] / (1024 * 1024)
        print(f"  {fn} ({size_mb:.2f} MB)")
    
    return file_names


def main():
    """Main entry point for the CSV split tool."""
    parser = argparse.ArgumentParser(
        description='Split a large CSV file into smaller chunks'
    )
    
    parser.add_argument('-i', '--input', type=str, 
                       default='~/Desktop/input.csv',
                       help='Path to input CSV file (default: ~/Desktop/input.csv)')
    parser.add_argument('-o', '--output', type=str, 
                       default='~/Desktop/output/',
                       help='Path to output directory (default: ~/Desktop/output/)')
    parser.add_argument('-s', '--chunk-size', type=int, 
                       default=200000,
                       help='Number of rows per chunk (default: 200000)')
    
    args = parser.parse_args()
    
    split_csv_file(args.input, args.output, args.chunk_size)


if __name__ == '__main__':
    main()
