#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Auto SQL Query to CSV

This module executes SQL queries against a database and exports results to CSV.

Usage:
    python -m csv_tools.auto_sql_query_to_csv -q query.sql -i db_info.txt -o output.csv
    python -m csv_tools.auto_sql_query_to_csv -s  # Generate sample files
"""

import argparse
import os
import pandas as pd
import pymysql


def read_sql_file(path):
    """
    Read SQL query from file.
    
    Args:
        path (str): Path to SQL file
        
    Returns:
        str: SQL query content
    """
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def read_db_info_file(path):
    """
    Read database connection info from file.
    
    Expected format:
        host=localhost
        user=username
        password=password
        database=dbname
        port=3306
    
    Args:
        path (str): Path to database info file
        
    Returns:
        dict: Database connection parameters
    """
    db_info = {}
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    db_info[key.strip()] = value.strip().replace("'", "").replace('"', '')
    return db_info


def execute_sql(db_info, query):
    """
    Execute SQL query and return results as DataFrame.
    
    Args:
        db_info (dict): Database connection parameters
        query (str): SQL query to execute
        
    Returns:
        pd.DataFrame or None: Query results, or None if error occurs
    """
    try:
        conn = pymysql.connect(
            host=db_info['host'],
            user=db_info['user'],
            password=db_info['password'],
            db=db_info['database'],
            port=int(db_info.get('port', 3306))
        )
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except pymysql.Error as e:
        print(f"Database connection error: {str(e)}")
        return None


def write_to_csv(df, path, encoding='utf-8'):
    """
    Write DataFrame to CSV file with specified encoding.
    
    Args:
        df (pd.DataFrame): Data to write
        path (str): Output file path
        encoding (str): Output encoding ('utf-8', 'utf8', 'ansi', 'a')
        
    Returns:
        None
    """
    encoding_lower = encoding.lower()
    
    if encoding_lower in ['a', 'ansi']:
        df.to_csv(path, index=False, encoding='ansi')
        print(f"Output file encoding: ANSI")
    elif encoding_lower in ['u', 'utf8', 'utf-8']:
        df.to_csv(path, index=False, encoding='utf-8')
        print(f"Output file encoding: UTF-8")
    else:
        print(f"Unsupported encoding: {encoding}")
        print("Using UTF-8 as default")
        df.to_csv(path, index=False, encoding='utf-8')


def write_example_input_files():
    """
    Generate example SQL query and database info files.
    
    Returns:
        None
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os_linesep = os.linesep
    
    # Write example SQL query file
    sql_query_example = f"-- Example SQL Query{os_linesep}SELECT * FROM table_name;"
    sql_query_file = os.path.join(current_dir, "example_query.sql")
    with open(sql_query_file, 'w', encoding='utf-8') as file:
        file.write(sql_query_example)
    print(f"Created example SQL file: {sql_query_file}")
    
    # Write example database info file
    db_info_example = (f"# Example Database Connection Info{os_linesep}"
                      f"host=localhost{os_linesep}"
                      f"user=username{os_linesep}"
                      f"password=pass123{os_linesep}"
                      f"database=db_name{os_linesep}"
                      f"port=3306{os_linesep}")
    db_info_file = os.path.join(current_dir, "example_db_info.txt")
    with open(db_info_file, 'w', encoding='utf-8') as file:
        file.write(db_info_example)
    print(f"Created example DB info file: {db_info_file}")


def main():
    """Main entry point for SQL query to CSV tool."""
    parser = argparse.ArgumentParser(
        description='Execute SQL queries and export results to CSV'
    )
    
    parser.add_argument('-q', '--query', dest='sql_query_path',
                       help='Path to SQL query file')
    parser.add_argument('-i', '--input', '--info', dest='db_info_path',
                       help='Path to database connection info file')
    parser.add_argument('-o', '--output', dest='output_path',
                       help='Path to output CSV file')
    parser.add_argument('-e', '--encoding', default='u',
                       help='Output CSV encoding (u/utf8/utf-8 or a/ansi, default: utf-8)')
    parser.add_argument('-s', '--sample', action='store_true',
                       help='Generate example input files')
    
    args = parser.parse_args()
    
    # Handle sample file generation
    if args.sample:
        write_example_input_files()
        return
    
    # Validate required arguments
    if not all([args.sql_query_path, args.db_info_path, args.output_path]):
        parser.print_help()
        print("\nError: -q, -i, and -o arguments are required unless using -s")
        return
    
    # Validate encoding
    encoding = args.encoding.lower()
    if encoding not in ['a', 'ansi', 'u', 'utf8', 'utf-8']:
        print(f"Unsupported encoding: {encoding}")
        print("Supported encodings: utf-8, utf8, u, ansi, a")
        return
    
    # Execute query
    print("Reading SQL query...")
    query = read_sql_file(args.sql_query_path)
    
    print("Reading database connection info...")
    db_info = read_db_info_file(args.db_info_path)
    
    print("Executing SQL query...")
    df = execute_sql(db_info, query)
    
    if df is not None:
        print(f"Query executed successfully. Rows returned: {len(df)}")
        print("Writing to CSV...")
        write_to_csv(df, args.output_path, encoding)
        print(f"Task completed!")
        print(f"Output file: {args.output_path}")
    else:
        print("Query execution failed.")


if __name__ == "__main__":
    main()
