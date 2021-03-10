#!/usr/bin/env python3
import ruamel.yaml
import sys

themes = "themes/nord.yaml"
FileAlacritty = "example.yml"
yaml = ruamel.yaml.YAML()


if __name__ == '__main__':
    updateChange = open(FileAlacritty,'r')
    addLines = open(themes,'r')

    readAlacritty = yaml.load(updateChange)
    readThemes = yaml.load(addLines)

    readAlacritty['colors'] = readThemes['colors']
    updateChange.close()
    addLines.close()

    updateFile = open(FileAlacritty,'w')
    yaml.dump(readAlacritty,updateFile)
    updateFile.close()