#!/usr/bin/env python 

"""task_manager.py: module to be run for task manager application

__author__      = "Arthur Poon"
__class_name__  = "Immersion Programming - M Section"
__version__ = "1.0"
__email__ = "arthur.poon@chicagobooth.edu
"""

from tasks import Task, Tasks
import commandgetparse

def main():
    """The main functionality of this smodule"""
    Tasks_obj = Tasks()

    args = commandgetparse.get_and_parse_command_line_inputs()

    #operations based on arguments
    if args.add:
        Tasks_obj.add(args.add,args.priority,args.due)

    elif args.report:
        Tasks_obj.sort_tasks()
        Tasks_obj.report()

    elif args.list:
        Tasks_obj.sort_tasks()
        Tasks_obj.list()

    elif args.query:
        Tasks_obj.sort_tasks()
        query_terms = args.query
        Tasks_obj.query(query_terms)

    elif args.done:
        Tasks_obj.done(args.done)

    elif args.delete:
        Tasks_obj.delete(args.delete)


    ## do something with the data based on the user commands
    Tasks_obj.pickle_tasks()
    exit()

if __name__ == "__main__":
    main()
