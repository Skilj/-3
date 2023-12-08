import os


def get_pah(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


TXT_FILE = get_pah('poem.txt')
CSV_FILE = get_pah('users.csv')
JSON_FILE = get_pah('users.json')
YAML_FILE = get_pah('config.yaml')

TXT_FILE_W = get_pah('poem_w.txt')
CSV_FILE_W = get_pah('users_w.csv')
JSON_FILE_W = get_pah('users_w.json')
YAML_FILE_W = get_pah('config_w.yaml')

