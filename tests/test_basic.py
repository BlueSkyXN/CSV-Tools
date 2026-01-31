#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Basic Integration Tests for CSV-Tools

These tests verify that the refactored code works correctly.
"""

import os
import sys
import tempfile
import pandas as pd

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from csv_tools import compare_csv, merge_csv, split_csv


def test_compare_csv():
    """Test CSV comparison functionality."""
    print("\n=== Testing CSV Comparison ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files
        df1 = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})
        df2 = pd.DataFrame({'name': ['Alice', 'David', 'Eve'], 'age': [25, 28, 32]})
        
        file1 = os.path.join(tmpdir, 'test1.csv')
        file2 = os.path.join(tmpdir, 'test2.csv')
        output = os.path.join(tmpdir, 'output.csv')
        
        df1.to_csv(file1, index=False)
        df2.to_csv(file2, index=False)
        
        # Run comparison
        compare_csv.compare_csv_files(file1, file2, output, 'name')
        
        # Verify output exists
        assert os.path.exists(output), "Output file not created"
        
        # Read and verify results
        result = pd.read_csv(output)
        print(f"  ✓ Comparison successful: {len(result)} non-matching rows found")
        
        return True


def test_split_csv():
    """Test CSV splitting functionality."""
    print("\n=== Testing CSV Splitting ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test file
        df = pd.DataFrame({'col1': range(100), 'col2': range(100, 200)})
        input_file = os.path.join(tmpdir, 'input.csv')
        output_dir = os.path.join(tmpdir, 'output')
        
        df.to_csv(input_file, index=False)
        os.makedirs(output_dir, exist_ok=True)
        
        # Run split
        files = split_csv.split_csv_file(input_file, output_dir, chunk_size=30)
        
        # Verify outputs
        assert len(files) > 0, "No output files created"
        print(f"  ✓ Split successful: {len(files)} chunks created")
        
        return True


def test_merge_csv():
    """Test CSV merging functionality."""
    print("\n=== Testing CSV Merging ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files
        df1 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        df2 = pd.DataFrame({'col1': [7, 8, 9], 'col2': [10, 11, 12]})
        
        file1 = os.path.join(tmpdir, 'output_0.csv')
        file2 = os.path.join(tmpdir, 'output_1.csv')
        output = os.path.join(tmpdir, 'merged.csv')
        
        df1.to_csv(file1, index=False)
        df2.to_csv(file2, index=False)
        
        # Run merge
        count = merge_csv.merge_csv_files(tmpdir, output, file_prefix='output_')
        
        # Verify output
        assert os.path.exists(output), "Output file not created"
        result = pd.read_csv(output)
        assert len(result) == 6, f"Expected 6 rows, got {len(result)}"
        print(f"  ✓ Merge successful: {count} files merged")
        
        return True


def main():
    """Run all tests."""
    print("=" * 60)
    print("CSV-Tools Integration Tests")
    print("=" * 60)
    
    tests = [
        ("Compare CSV", test_compare_csv),
        ("Split CSV", test_split_csv),
        ("Merge CSV", test_merge_csv),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
                print(f"  ✗ {test_name} failed")
        except Exception as e:
            failed += 1
            print(f"  ✗ {test_name} failed with error: {str(e)}")
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
