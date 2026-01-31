#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UTF-8 to ANSI Converter

This module converts CSV files from UTF-8 encoding to ANSI encoding.
Note: ANSI encoding may lose some Unicode characters that are not supported.

Usage:
    python -m csv_tools.utf8_to_ansi_csv -i input.csv -o output.csv
"""

import argparse
import sys


def convert_utf8_to_ansi(input_file, output_file):
    """
    Convert a UTF-8 encoded file to ANSI encoding.
    
    Args:
        input_file (str): Path to the input UTF-8 encoded file
        output_file (str): Path to the output ANSI encoded file
        
    Returns:
        None
        
    Note:
        Characters not supported in ANSI encoding will be ignored.
    """
    try:
        # Read UTF-8 content
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert to ANSI encoding
        ansi_content = content.encode('ansi', 'ignore').decode('ansi')
        
        # Write ANSI content
        with open(output_file, 'w', encoding='ansi') as f:
            f.write(ansi_content)
        
        print(f"Successfully converted {input_file} to ANSI encoding")
        print(f"Output saved to: {output_file}")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for the UTF-8 to ANSI converter."""
    parser = argparse.ArgumentParser(
        description='Convert UTF-8 encoded CSV file to ANSI encoding'
    )
    
    parser.add_argument('-i', '--input', type=str, required=True,
                       help='Input file path (UTF-8 encoded)')
    parser.add_argument('-o', '--output', type=str, required=True,
                       help='Output file path (ANSI encoded)')
    
    args = parser.parse_args()
    
    if not args.input or not args.output:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    convert_utf8_to_ansi(args.input, args.output)


if __name__ == '__main__':
    main()
