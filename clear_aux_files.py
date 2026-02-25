from shutil import rmtree
from glob import glob
import os


with open('.gitignore') as gi:
    for line in gi.readlines():
        line = line.strip()

        if not line:
            continue

        if line[0] == '#':
            if line == '## Added manually': break
            else: continue
        
        for file in glob(line):
            os.remove(file)


rmtree("%OUTDIR%", True)