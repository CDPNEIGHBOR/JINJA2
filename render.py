#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
from pprint import pprint
import yaml

with open(r'C:\Users\Stephen Hendry\PycharmProjects\YAML\stephen.yaml', 'r') as stephen:
    stephen_data = yaml.load(stephen, Loader=yaml.FullLoader)

template_dir = r'C:\Users\Stephen Hendry\PycharmProjects\jinja2'

merge = stephen_data['stephen']

template_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)

template = template_env.get_template('stephen.j2')
complete = template.render(merge)

print(complete)








