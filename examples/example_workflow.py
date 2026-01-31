#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example: Basic CSV Processing Workflow

This example demonstrates a basic workflow using CSV-Tools:
1. Split a large CSV file
2. Process each chunk
3. Merge the results
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.csv_tools import split_csv, merge_csv


def main():
    """
    Example workflow for processing CSV files.
    """
    print("CSV-Tools Example Workflow")
    print("=" * 50)
    
    # Example parameters
    input_file = "large_dataset.csv"
    temp_dir = "/tmp/csv_chunks"
    output_file = "processed_output.csv"
    
    print("\nNote: This is a demonstration script.")
    print("Actual file paths should be provided as arguments.\n")
    
    # Step 1: Split large CSV
    print("Step 1: Splitting large CSV file...")
    print(f"  Input: {input_file}")
    print(f"  Output directory: {temp_dir}")
    print(f"  Chunk size: 100000 rows")
    
    # Uncomment to actually run:
    # split_csv.split_csv_file(input_file, temp_dir, chunk_size=100000)
    
    print("\n✓ Split complete\n")
    
    # Step 2: Process each chunk (your custom processing here)
    print("Step 2: Processing each chunk...")
    print("  (Add your custom processing logic here)")
    
    print("\n✓ Processing complete\n")
    
    # Step 3: Merge results
    print("Step 3: Merging processed chunks...")
    print(f"  Input directory: {temp_dir}")
    print(f"  Output file: {output_file}")
    
    # Uncomment to actually run:
    # merge_csv.merge_csv_files(temp_dir, output_file, file_prefix='output_')
    
    print("\n✓ Merge complete\n")
    
    print("=" * 50)
    print("Workflow complete!")
    

if __name__ == '__main__':
    main()
