
import pandas as pd
import configparser
import openpyxl

def read_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')
    return config

def read_csv(file_path, encoding='utf-8'):
    return pd.read_csv(file_path, encoding=encoding).dropna(how="all", axis=1)

def classify_data(data, dev_dep_list, dep_column):
    dev_data = data[data[dep_column].isin(dev_dep_list)]
    non_dev_data = data[~data[dep_column].isin(dev_dep_list)]
    return dev_data, non_dev_data

def calculate_summary(data_last, data_current, dep_column, id_column, tag_unresolved, tag_new, stat_names):
    data_last_unique = data_last.drop_duplicates(subset=[id_column])
    data_current_unique = data_current.drop_duplicates(subset=[id_column])
    unresolved_ids = data_last_unique[data_last_unique[id_column].isin(data_current[id_column])][id_column]
    new_violations_ids = data_current_unique[~data_current_unique[id_column].isin(data_last[id_column])][id_column]
    unresolved_records = data_current[data_current[id_column].isin(unresolved_ids)].copy()
    new_violations_records = data_current[data_current[id_column].isin(new_violations_ids)].copy()

    # Adding tags from config
    unresolved_records['Tag_Unresolved'] = 1
    new_violations_records['Tag_New'] = 1

    detailed_data = pd.concat([unresolved_records, new_violations_records])
    detailed_data[['Tag_Unresolved', 'Tag_New']] = detailed_data[['Tag_Unresolved', 'Tag_New']].fillna(0).astype(int)

    # Fixing the calculation of unresolved
    summary = detailed_data.groupby(dep_column, as_index=False).agg({
        id_column: [
            (stat_names['Stat_1'], lambda x: x.nunique()),
            (stat_names['Stat_2'], lambda x: (detailed_data[detailed_data['Tag_Unresolved'] == 1][id_column]).nunique()),
            (stat_names['Stat_3'], lambda x: (detailed_data[detailed_data['Tag_New'] == 1][id_column]).nunique())
        ]
    }).fillna(0)
    summary.columns = summary.columns.droplevel(0)

    # Adding total row
    total_row = summary.sum(numeric_only=True)
    total_row[dep_column] = "总计"
    summary = pd.concat([summary, pd.DataFrame([total_row])]).fillna("")

    return summary, detailed_data

def write_to_excel(file_path, dev_summary, non_dev_summary, dev_detail, non_dev_detail, sheet_names):
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        dev_summary.to_excel(writer, sheet_name=sheet_names['S_name_1'], index=False)
        dev_detail.to_excel(writer, sheet_name=sheet_names['S_name_2'], index=False, index_label=False)
        non_dev_summary.to_excel(writer, sheet_name=sheet_names['S_name_3'], index=False)
        non_dev_detail.to_excel(writer, sheet_name=sheet_names['S_name_4'], index=False, index_label=False)

config_file_path = "CSV_DataAnalysis.conf"
config = read_config(config_file_path)
last_file_path = config.get('Files', 'Last_file_path') + config.get('Files', 'Last_file_name')
current_file_path = config.get('Files', 'Current_file_path') + config.get('Files', 'Current_file_name')
output_file_path = config.get('Files', 'Output_file_path') + config.get('Files', 'Output_file_name')
dev_dep = config.get('DepSet', 'dev_dep').split(',')
tag_unresolved = config.get('TagSet', 'Tag1')
tag_new = config.get('TagSet', 'Tag2')
sheet_names = config['Sheet']
stat_names = {key: config.get('Sheet', key) for key in ['Stat_1', 'Stat_2', 'Stat_3']}

last_data = read_csv(last_file_path, config.get('Files', 'Last_file_encoding', fallback='UTF8'))
current_data = read_csv(current_file_path, config.get('Files', 'Current_file_encoding', fallback='UTF8'))
dev_data_last, non_dev_data_last = classify_data(last_data, dev_dep, config.get('MainKEY', 'input_key_last_dep'))
dev_data_current, non_dev_data_current = classify_data(current_data, dev_dep, config.get('MainKEY', 'input_key_current_dep'))
summary_dev, dev_detail_current = calculate_summary(dev_data_last, dev_data_current, config.get('MainKEY', 'input_key_current_dep'), config.get('MainKEY', 'input_key_current_id'), tag_unresolved, tag_new, stat_names)
summary_non_dev, non_dev_detail_current = calculate_summary(non_dev_data_last, non_dev_data_current, config.get('MainKEY', 'input_key_current_dep'), config.get('MainKEY', 'input_key_current_id'), tag_unresolved, tag_new, stat_names)
write_to_excel(output_file_path, summary_dev, summary_non_dev, dev_detail_current, non_dev_detail_current, sheet_names)
