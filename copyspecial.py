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
    return [os.path.abspath(x) for x in special_files]


def copy_to(path_list, dest_dir):
    '''Given the --todir arg, a path list and a destination dir,
    copy the files in the path list to the destination dir'''
    # your code here
    print('Path List: ', path_list)
    print('Dest Dir: ', dest_dir)
    if os.path.exists(dest_dir) is False:
        os.makedirs(dest_dir)
    for path in path_list:
        if os.path.exists(path):
            shutil.copy(path, dest_dir)
    return


def zip_to(path_list, dest_zip):
    '''Given the --tozip arg, a path list and a destination zip,
    zip the files in the path list to the destination zip'''
    # your code here
    print('Command I\'m going to do:', '\n', 'zip -j ', dest_zip)
    print(*path_list, sep='\n')
    for path in path_list:
        try:
            output = subprocess.run(['zip', '-j', dest_zip, path], check=True)
        except subprocess.CalledProcessError as e:
            return e
    return output


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='target directory')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    if ns.todir and ns.from_dir:
        copy_to(os.listdir(ns.from_dir), ns.todir)
    elif ns.tozip and ns.from_dir:
        data = zip_to(os.listdir(ns.from_dir), ns.tozip)
        print(data)
    elif ns.from_dir and not ns.tozip and not ns.todir:
        special_files = get_special_paths(ns.from_dir)
        for special_file in special_files:
            print(special_file, end='\n')
    else:
        parser.print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
