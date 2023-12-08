import yaml

from example_from_lesson.test_data.read_write_files.files import YAML_FILE_W, YAML_FILE

with open(YAML_FILE) as f:
    templates = yaml.safe_load(f)

print(templates)


login = "alisa"
kafka = {
    'caRootLocation': 'certs//kafka-ca-root.crt',
    'certLocation': 'certs//kafka-client.crtt',
    'keyLocation': 'certs//kafka-client.pem'
}

to_yaml = {'login': login, 'kafka': kafka}

with open(YAML_FILE_W, 'w') as f:
    yaml.dump(to_yaml, f, default_flow_style=False)



