#!/usr/bin/env python3
import yaml
import sys

themes = "themes/nord.yaml"
FileAlacritty = "example.yml"


if __name__ == '__main__':
    updateChange = open(FileAlacritty,'r')
    addLines = open(themes,'r')

    readAlacritty = yaml.load(updateChange,Loader=yaml.FullLoader)
    readThemes = yaml.load(addLines,Loader=yaml.FullLoader)
    
    acritty['colors'] = readThemes['colors']

    updateChange.close()
    addLines.close()

    updateFile = open(FileAlacritty,'w')
    resulChanges = yaml.dump(readAlacritty,updateFile,default_flow_style=False,sort_keys=False)
    updateFile.close()

