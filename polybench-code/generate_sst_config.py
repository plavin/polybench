#!/usr/bin/env python3

import os
import pathlib
import pprint


top_dirs = ['linear-algebra', 'medley', 'stencils', 'datamining']
paths = [pathlib.Path(a) for a in top_dirs]

prog_dirs = []

def dir_has_c_file(path):
    for p in path.iterdir():
        if ".c" in str(p):
            return True
    return False

def find_prog_dirs(path):
    for p in path.iterdir():
        if p.is_dir():
            if dir_has_c_file(p):
                prog_dirs.append(p)
            else:
                find_prog_dirs(p)

for p in paths:
    find_prog_dirs(p)

print(prog_dirs)

configs = {}
for p in prog_dirs:
    configs[str(p.stem)] = {
        'cmd' : str(p.stem),
        'directory' : str(p.resolve()),
        'ariel_markers' : False
    }

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(configs)
