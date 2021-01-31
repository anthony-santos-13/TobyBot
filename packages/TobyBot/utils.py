import yaml
from yamlinclude.constructor import YamlIncludeConstructor

def get_dict_from_yaml(yaml_path):
    dict = None
    yaml_path = yaml_path.replace('\\', '/')
    yaml_base_dir = yaml_path.replace('/'+yaml_path.split('/')[-1], '')
    YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir=yaml_base_dir)

    try:
        with open(yaml_path,'r') as f:
            dict =  yaml.load(f, Loader=yaml.FullLoader)
    except Exception as e:
        if 'No such file or directory' in str(e):
            dict = {}
            write_dict_to_yaml(yaml_path, dict)

    return dict

def write_dict_to_yaml(file_path, dict):
    stream = open(file_path, 'w')
    yaml.dump(dict, stream, default_flow_style=False, sort_keys = False)