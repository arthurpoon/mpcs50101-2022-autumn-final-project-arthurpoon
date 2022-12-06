#!/usr/bin/env python 

"""commandgetparse.py: module containing parsing of command line inputs

__author__      = "Arthur Poon"
__class_name__  = "Immersion Programming - M Section"
__version__ = "1.0"
__email__ = "arthur.poon@chicagobooth.edu
"""

import argparse

def get_and_parse_command_line_inputs():

    parser = argparse.ArgumentParser(description='Update your ToDo List.')

    parser.add_argument('--add', required = False, help='a task string to add to your list')
    parser.add_argument('--due', type=str, required = False, help='due date, ideally in mm/dd/yyyy format')
    parser.add_argument('--priority', type=int, required = False, default = 3, help='priority of a task; default value is 3')
    
    parser.add_argument('--query', type=str, required = False, nargs = "+", help='what to search for within tasks')
    parser.add_argument('--list', action = 'store_true', required=False, help="list all tasks that have not been completed")
    parser.add_argument('--done', type=int, required=False, help="enter ID of task to be marked done")
    parser.add_argument('--delete',type=int, required=False, help="enter ID of task to be deleted")
    parser.add_argument('--report', action = 'store_true', required=False, help="list all tasks that have not been completed")
    
    #Parse the argument
    args = parser.parse_args()

    return args