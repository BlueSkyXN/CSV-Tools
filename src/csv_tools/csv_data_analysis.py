#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CSV Data Analysis Tool

This module performs comparative analysis on two CSV files, classifying data
by departments and identifying unresolved and new violations.

Usage:
    python -m csv_tools.csv_data_analysis -c config.conf
"""

import argparse
import configparser
import pandas as pd
from openpyxl import Workbook


def read_csv(file_path, encoding='UTF-8'):
    """
    Read CSV file with specified encoding.
    
    Args:
        file_path (str): Path to CSV file
        encoding (str): File encoding (default: 'UTF-8')
        
    Returns:
        pd.DataFrame: Loaded data
    """
    return pd.read_csv(file_path, encoding=encoding)


def classify_data(data, dev_dep, dep_key):
    """
    Classify data into development and non-development departments.
    
    Args:
        data (pd.DataFrame): Input data
        dev_dep (list): List of development department names
        dep_key (str): Department column name
        
    Returns:
        tuple: (dev_data, non_dev_data) - Classified DataFrames
    """
    dev_data = data[data[dep_key].isin(dev_dep)]
    non_dev_data = data[~data[dep_key].isin(dev_dep)]
    return dev_data, non_dev_data


def calculate_summary_per_dep(data_last, data_current, dep_column, id_column,
                              tag_unresolved, tag_new, stat_names):
    """
    Calculate summary statistics per department.
    
    Args:
        data_last (pd.DataFrame): Previous period data
        data_current (pd.DataFrame): Current period data
        dep_column (str): Department column name
        id_column (str): Unique ID column name
        tag_unresolved (str): Label for unresolved records
        tag_new (str): Label for new records
        stat_names (dict): Names for statistics columns
        
    Returns:
        tuple: (summary, detailed_data) - Summary and detailed DataFrames
    """
    # Find unique records
    data_last_unique = data_last.drop_duplicates(subset=[id_column])
    data_current_unique = data_current.drop_duplicates(subset=[id_column])
    
    # Identify unresolved records (present in both datasets)
    unresolved_ids = data_last_unique[
        data_last_unique[id_column].isin(data_current[id_column])
    ][id_column]
    
    # Identify new violations (only in current dataset)
    new_violations_ids = data_current_unique[
        ~data_current_unique[id_column].isin(data_last[id_column])
    ][id_column]
    
    # Extract records
    unresolved_records = data_current[
        data_current[id_column].isin(unresolved_ids)
    ].copy()
    new_violations_records = data_current[
        data_current[id_column].isin(new_violations_ids)
    ].copy()
    
    # Add tags
    unresolved_records[tag_unresolved] = 1
    new_violations_records[tag_new] = 1
    
    # Combine detailed data
    detailed_data = pd.concat([unresolved_records, new_violations_records])
    detailed_data[[tag_unresolved, tag_new]] = detailed_data[
        [tag_unresolved, tag_new]
    ].fillna(0).astype(int)
    
    # Calculate summary per department
    def calculate_per_dep_group(group):
        return pd.Series({
            stat_names['Stat_1']: group[id_column].nunique(),
            stat_names['Stat_2']: group[group[tag_unresolved] == 1][id_column].nunique(),
            stat_names['Stat_3']: group[group[tag_new] == 1][id_column].nunique()
        })
    
    summary = detailed_data.groupby(dep_column).apply(
        calculate_per_dep_group
    ).reset_index()
    
    # Add total row
    total_row = summary.sum(numeric_only=True)
    total_row[dep_column] = "总计"
    total_row = pd.DataFrame([total_row])
    summary = pd.concat([summary, total_row], ignore_index=True).fillna("")
    
    return summary, detailed_data


def write_to_excel(output_file_path, summary_dev, summary_non_dev,
                  dev_detail_current, non_dev_detail_current, sheet_names):
    """
    Write analysis results to Excel file.
    
    Args:
        output_file_path (str): Output Excel file path
        summary_dev (pd.DataFrame): Development departments summary
        summary_non_dev (pd.DataFrame): Non-development departments summary
        dev_detail_current (pd.DataFrame): Development departments detail
        non_dev_detail_current (pd.DataFrame): Non-development departments detail
        sheet_names (dict): Names for Excel sheets
        
    Returns:
        None
    """
    with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        summary_dev.to_excel(writer, index=False, 
                           sheet_name=sheet_names['S_name_1'])
        dev_detail_current.to_excel(writer, index=False, 
                                   sheet_name=sheet_names['S_name_2'])
        summary_non_dev.to_excel(writer, index=False, 
                                sheet_name=sheet_names['S_name_3'])
        non_dev_detail_current.to_excel(writer, index=False, 
                                       sheet_name=sheet_names['S_name_4'])


def main():
    """Main entry point for CSV data analysis tool."""
    # Argument parser setup
    parser = argparse.ArgumentParser(
        description='CSV Data Analysis Tool - Compare and analyze CSV data'
    )
    parser.add_argument('-c', '--config', type=str, 
                       default='CSV_DataAnalysis.conf',
                       help='Path to configuration file (default: CSV_DataAnalysis.conf)')
    
    args = parser.parse_args()
    
    # Read configuration file
    config = configparser.ConfigParser()
    config.read(args.config, encoding='utf-8')
    
    # Extract configuration parameters
    last_file_path = (config.get('Files', 'Last_file_path') + 
                     config.get('Files', 'Last_file_name'))
    current_file_path = (config.get('Files', 'Current_file_path') + 
                        config.get('Files', 'Current_file_name'))
    output_file_path = (config.get('Files', 'Output_file_path') + 
                       config.get('Files', 'Output_file_name'))
    
    dev_dep = config.get('DepSet', 'dev_dep').split(',')
    tag_unresolved = config.get('TagSet', 'Tag1')
    tag_new = config.get('TagSet', 'Tag2')
    sheet_names = config['Sheet']
    stat_names = {key: config.get('Sheet', key) 
                 for key in ['Stat_1', 'Stat_2', 'Stat_3']}
    
    # Read data
    print("Reading previous period data...")
    last_data = read_csv(
        last_file_path,
        config.get('Files', 'Last_file_encoding', fallback='UTF-8')
    )
    
    print("Reading current period data...")
    current_data = read_csv(
        current_file_path,
        config.get('Files', 'Current_file_encoding', fallback='UTF-8')
    )
    
    # Classify data by department
    print("Classifying data by department...")
    dev_data_last, non_dev_data_last = classify_data(
        last_data, dev_dep, 
        config.get('MainKEY', 'input_key_last_dep')
    )
    dev_data_current, non_dev_data_current = classify_data(
        current_data, dev_dep,
        config.get('MainKEY', 'input_key_current_dep')
    )
    
    # Calculate summaries
    print("Calculating development departments summary...")
    summary_dev, dev_detail_current = calculate_summary_per_dep(
        dev_data_last, dev_data_current,
        config.get('MainKEY', 'input_key_current_dep'),
        config.get('MainKEY', 'input_key_current_id'),
        tag_unresolved, tag_new, stat_names
    )
    
    print("Calculating non-development departments summary...")
    summary_non_dev, non_dev_detail_current = calculate_summary_per_dep(
        non_dev_data_last, non_dev_data_current,
        config.get('MainKEY', 'input_key_current_dep'),
        config.get('MainKEY', 'input_key_current_id'),
        tag_unresolved, tag_new, stat_names
    )
    
    # Write results to Excel
    print("Writing results to Excel...")
    write_to_excel(output_file_path, summary_dev, summary_non_dev,
                  dev_detail_current, non_dev_detail_current, sheet_names)
    
    print(f"\nAnalysis complete!")
    print(f"Output file: {output_file_path}")


if __name__ == '__main__':
    main()
