#!/usr/bin/env python3

import os
import pathlib

# get enclosing folder name
# the folder name is the name of the project and will help us set the env in Deadline later on
cwd = os.getcwd()
path = pathlib.PurePath(cwd)
dirname = path.name

print(dirname)
