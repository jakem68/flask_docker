__author__ = 'Jan Kempeneers'

import sys
import yaml

def yaml_load(yaml_file):
    with open(yaml_file) as file:
        yaml_dict = yaml.full_load(file)
    return yaml_dict

def yaml_dump(yaml_dict, file):
    with open(file, 'w') as file:
        documents = yaml.dump(yaml_dict, file)
        

def run(yaml_file):
    yaml_dict = yaml_load(yaml_file)
    print(yaml_dict)

def main():
    yaml_file = sys.argv[1]
    run(yaml_file)

if __name__ == '__main__':
    main()