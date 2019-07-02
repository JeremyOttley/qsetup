#!/usr/bin/python3

import os
import sys
import shutil
import subprocess

HOME = os.getenv('HOME') + "/"
SCRIPT_DIR = os.path.realpath(__file__)
CONFIG_DIR = os.getenv('XDG_CONFIG_HOME') + "/"

# Create directory if it does not exist already
if not os.path.exists(CONFIG_DIR + "qtile/"):
  os.makedirs(CONFIG_DIR + "qtile/")

##: Step 1: ensure that python3 is installed
def check():

##: Step 2: install prerequisites
def install():

###
# TEST AREA
###

def install_pip():
  subprocess.run(["curl", "https://bootstrap.pypa.io/get-pip.py", "-o", "get-pip.py"])
  subprocess.run(["python", "get-pip.py", "--user"])

def pip_install_xonsh():
  subprocess.run(["pip install", "--user", "xonsh", "ptk", "pygments>=2.2"])

def build_all():
  install_pip()
  pip_install_xonsh()
  subprocess.run(["touch", "~/.xonshrc"])

build_all()
