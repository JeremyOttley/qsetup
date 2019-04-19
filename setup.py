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

