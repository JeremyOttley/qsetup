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

def write_config():
  f = open("test.py", "a")
  f.write("""
$PATH.append('/home/gazbit/bin')
$DEV = $HOME +'/.workspace'
$PROMPT = '自由 [{short_cwd}] {gitstatus}  '

#ALIASES
##SYS
aliases['la'] = 'ls -a'

##DIR JUMPS
aliases['work'] = 'cd $DEV'
aliases['..'] = 'cd ..'
aliases['fuck'] = 'sudo !!'
aliases['feh-set'] = 'feh --bg-fill'
"""
  )
  f.close()

write_config()


