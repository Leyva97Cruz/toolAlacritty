#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t","--theme",help="Select the theme in the console")
parser.add_argument("-f","--font",help="Select the font in the console")

args = parser.parse_args()

print("Nombre del tema : {}\nNombre de la fuente : {} ".format(args.theme,args.font))
