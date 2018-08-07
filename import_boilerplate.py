#!/usr/bin/env python3
# Import from the BSD licensed jupyter_boilerplate project

# The idea is to extract the data, but it is often incomplete, only parts are useful, different layout (too many subcategories) etc.

import os
import sys
import json
import yaml
from glob import iglob
from pprint import pprint

REPO = 'https://github.com/moble/jupyter_boilerplate.git'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TMP = os.path.join(BASE_DIR, 'tmp')

os.chdir(BASE_DIR)

# setup empty tmp directory
os.system('rm -rf {0}; mkdir {0}'.format(TMP))
os.chdir(TMP)

# fresh clone of repo
os.system('git clone --depth=1 --recurse-submodules {}'.format(REPO))
os.chdir(BASE_DIR)

# read files: this overwrites files in src/
os.system('coffee read_boilerplate.coffee')

print("OK!\nTODO: cleanup tmp/ and jupyter_boilerplate/")