#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "r-bolling with help from Kenzie Academy"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # your code here
    special_files = []
    dir_list = os.listdir(dirname)
    special_file_pattern = re.compile(r'.*__\w+__.*')
    for directory in dir_list:
        special_files.extend(special_file_pattern.findall(directory))
    # special_files = special_file_pattern.findall(dir_list)
    # print(special_files)
    return [os.path.abspath(x) for x in special_files]


def copy_to(path_list, dest_dir):
    '''Given the --todir arg, a target dir and a destination dir,
    copy the files in the destination dir to the target dir'''
    # your code here
    return


def zip_to(path_list, dest_zip):
    '''Given the --tozip arg, a target dir and a destination zip,
    zip the files in the target dir to the destination zip'''
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='target directory')
    ns = parser.parse_args(args)

    if ns.from_dir:
        special_files = get_special_paths(ns.from_dir)
        for special_file in special_files:
            print(special_file, end='\n')
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
