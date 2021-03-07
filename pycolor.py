#!/usr/bin/env python3
import yaml

themes = "themes/nord.yaml"
FileAlacritty = "example.yaml"


if __name__ == '__main__':
    updateChange = open(FileAlacritty,'r')
    addLines = open(themes,'r')

    readAlacritty = yaml.load(updateChange,Loader=yaml.FullLoader)
    readThemes = yaml.load(addLines,Loader=yaml.FullLoader)
    
    readAlacritty['colors'] = readThemes['colors']
    updateChange.close()
    addLines.close()

    updateFile = open(FileAlacritty,'w')
    resulChanges = yaml.dump(readAlacritty,updateFile,default_flow_style=False,sort_keys=False)
    updateFile.close()

