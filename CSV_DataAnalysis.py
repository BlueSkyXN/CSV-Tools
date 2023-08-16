import pandas as pd
import configparser
from openpyxl import Workbook

# Function to read CSV data
def read_csv(file_path, encoding):
    return pd.read_csv(file_path, encoding=encoding)

# Function to classify data
def classify_data(data, dev_dep, dep_key):
    dev_data = data[data[dep_key].isin(dev_dep)]
    non_dev_data = data[~data[dep_key].isin(dev_dep)]
    return dev_data, non_dev_data

# Function to calculate summary per department
def calculate_summary_per_dep(data_last, data_current, dep_column, id_column, tag_unresolved, tag_new, stat_names):
    data_last_unique = data_last.drop_duplicates(subset=[id_column])
    data_current_unique = data_current.drop_duplicates(subset=[id_column])
    unresolved_ids = data_last_unique[data_last_unique[id_column].isin(data_current[id_column])][id_column]
    new_violations_ids = data_current_unique[~data_current_unique[id_column].isin(data_last[id_column])][id_column]
    unresolved_records = data_current[data_current[id_column].isin(unresolved_ids)].copy()
    new_violations_records = data_current[data_current[id_column].isin(new_violations_ids)].copy()

    # Adding tags from config
    unresolved_records[tag_unresolved] = 1
    new_violations_records[tag_new] = 1

    detailed_data = pd.concat([unresolved_records, new_violations_records])
    detailed_data[[tag_unresolved, tag_new]] = detailed_data[[tag_unresolved, tag_new]].fillna(0).astype(int)

    # Calculating summary using a custom function per department
    def calculate_per_dep_group(group):
        return pd.Series({
            stat_names['Stat_1']: group[id_column].nunique(),
            stat_names['Stat_2']: group[group[tag_unresolved] == 1][id_column].nunique(),
            stat_names['Stat_3']: group[group[tag_new] == 1][id_column].nunique()
        })

    summary = detailed_data.groupby(dep_column).apply(calculate_per_dep_group).reset_index()

    # Adding total row
    total_row = summary.sum(numeric_only=True)
    total_row[dep_column] = "总计"
    #summary = pd.concat([summary, pd.DataFrame([total_row]).set_index(dep_column)]).fillna("").reset_index()
    total_row = pd.DataFrame([total_row])  # 将总计行转换为DataFrame
    summary = pd.concat([summary, total_row], ignore_index=True).fillna("")  # 添加总计行

    return summary, detailed_data

# Function to write data to Excel
def write_to_excel_fixed(output_file_path, summary_dev, summary_non_dev, dev_detail_current, non_dev_detail_current, sheet_names):
    with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        summary_dev.to_excel(writer, index=False, sheet_name=sheet_names['S_name_1'])
        dev_detail_current.to_excel(writer, index=False, sheet_name=sheet_names['S_name_2'])
        summary_non_dev.to_excel(writer, index=False, sheet_name=sheet_names['S_name_3'])
        non_dev_detail_current.to_excel(writer, index=False, sheet_name=sheet_names['S_name_4'])


# Main code execution
config = configparser.ConfigParser()
config.read("CSV_DataAnalysis.conf", encoding='utf-8')

# Extracting required parameters from the configuration
last_file_path = config.get('Files', 'Last_file_path') + config.get('Files', 'Last_file_name')
current_file_path = config.get('Files', 'Current_file_path') + config.get('Files', 'Current_file_name')
output_file_path = config.get('Files', 'Output_file_path') + config.get('Files', 'Output_file_name')
dev_dep = config.get('DepSet', 'dev_dep').split(',')
tag_unresolved = config.get('TagSet', 'Tag1')
tag_new = config.get('TagSet', 'Tag2')
sheet_names = config['Sheet']
stat_names = {key: config.get('Sheet', key) for key in ['Stat_1', 'Stat_2', 'Stat_3']}

# Reading data
last_data = read_csv(last_file_path, config.get('Files', 'Last_file_encoding', fallback='UTF8'))
current_data = read_csv(current_file_path, config.get('Files', 'Current_file_encoding', fallback='UTF8'))

# Classifying data
dev_data_last, non_dev_data_last = classify_data(last_data, dev_dep, config.get('MainKEY', 'input_key_last_dep'))
dev_data_current, non_dev_data_current = classify_data(current_data, dev_dep, config.get('MainKEY', 'input_key_current_dep'))

# Calculating summary
summary_dev, dev_detail_current = calculate_summary_per_dep(dev_data_last, dev_data_current, config.get('MainKEY', 'input_key_current_dep'), config.get('MainKEY', 'input_key_current_id'), tag_unresolved, tag_new, stat_names)
summary_non_dev, non_dev_detail_current = calculate_summary_per_dep(non_dev_data_last, non_dev_data_current, config.get('MainKEY', 'input_key_current_dep'), config.get('MainKEY', 'input_key_current_id'), tag_unresolved, tag_new, stat_names)

write_to_excel_fixed(output_file_path, summary_dev, summary_non_dev, dev_detail_current, non_dev_detail_current, sheet_names)
