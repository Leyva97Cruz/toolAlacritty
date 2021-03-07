#!/usr/bin/env python3
import yaml
"""
with open('example.yaml') as archfile:
    doc = yaml.load_all(archfile,Loader=yaml.FullLoader)
    yaml.

    for data in doc:

        for u, d in data.items():

            if u == "colors":
                print("Encontrado {}".format(3))
"""
alacritty = "themes/dracula.yaml"
yaml_file = open(alacritty,'r')
yaml_content = yaml.load(yaml_file,Loader=yaml.FullLoader)

print("Key: Value")
for key, value in yaml_content.items():
    print(f"{key}:{value}")