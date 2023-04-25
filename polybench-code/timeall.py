#!/usr/bin/env python3

import pathlib
import pprint
import subprocess
import sys


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

# Time is in seconds
def parse_time(out):
    outs = out.split('\n')
    for ln in outs:
        if 'real' in ln:
            return ln.split(' ')[1]

    print('UNABLE TO PARSE TIME')
    sys.exit(1)

max_len = 0
for p in prog_dirs:
    if len(str(p.stem)) > max_len:
        max_len = len(str(p.stem))

print(f'Timing {len(prog_dirs)} programs')
alltimes = {}
for i, p in enumerate(prog_dirs):
    name = str(p.stem)
    print(f'{str(i).rjust(2)} {name.ljust(max_len+2)} ', end='')
    sys.stdout.flush()
    subp = subprocess.run(['time', '-p', str(p.joinpath(p.stem))],
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                   encoding='utf-8', check=True)
    time = parse_time(subp.stderr)
    print(f'{time}s')
    alltimes[name] = float(time)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(alltimes)

shorttimes = []
longtimes = []
for name,time in alltimes.items():
    if time < 1.0:
        shorttimes.append(name)
    else:
        longtimes.append(name)

print('\nThe following programs ran in less than a second:')
print(shorttimes)
print('\nThe following programs took at least a second to run:')
print(longtimes)
