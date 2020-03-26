#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
from pprint import pprint
import yaml

with open(r'C:\Users\Stephen Hendry\PycharmProjects\jinja2\topology.yaml', 'r') as topology:
    topology_data = yaml.load(topology, Loader=yaml.FullLoader)

template_dir = r'C:\Users\Stephen Hendry\PycharmProjects\jinja2'

template_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)

merge = topology_data['all_devices']

targets = topology_data['all_devices']

for device in targets:
    print('#' * 25 + 'HERE IS THE JINJA2 TEMPLATE FOR ' + device.upper() + '#' * 25)
    template = template_env.get_template('topology.j2')
    complete = template.render(merge[device])
    pprint(complete)







