import pandas as pd
import configparser

def read_config(config_file):
    # Create a config parser
    config = configparser.ConfigParser()

    # Read the config file
    config.read(config_file)

    # Now, we need to get the parameters from the config file
    file1_path = config.get('File1', 'path')
    file1_encoding = config.get('File1', 'encoding')
    file1_key = config.get('File1', 'key')

    file2_path = config.get('File2', 'path')
    file2_encoding = config.get('File2', 'encoding')
    file2_key = config.get('File2', 'key')

    output_path = config.get('Output', 'path')
    output_encoding = config.get('Output', 'encoding')

    return file1_path, file1_encoding, file1_key, file2_path, file2_encoding, file2_key, output_path, output_encoding

# Here is where we use the read_config function to get the parameters from the config file
file1_path, file1_encoding, file1_key, file2_path, file2_encoding, file2_key, output_path, output_encoding = read_config('CSV_Data_Compare.conf')

df1 = pd.read_csv(file1_path, encoding=file1_encoding)
df2 = pd.read_csv(file2_path, encoding=file2_encoding)

df1 = df1.drop_duplicates(subset=file1_key)
df2 = df2.drop_duplicates(subset=file2_key)

df = pd.concat([df1, df2])
df = df.drop_duplicates(subset=file1_key, keep=False)

df.to_csv(output_path, encoding=output_encoding, index=False)
