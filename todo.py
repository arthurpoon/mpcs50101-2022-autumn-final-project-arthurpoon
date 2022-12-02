#!/usr/bin/env python 

"""task_manager.py: module to be run for task manager application

__author__      = "Arthur Poon"
__class_name__  = "Immersion Programming - M Section"
__version__ = "1.0"
__email__ = "arthur.poon@chicagobooth.edu
"""

from tasks import Task, Tasks
import argparse
import dateparser

def main():
    """The main functionality of this smodule"""
    Tasks_obj = Tasks()

    parser = argparse.ArgumentParser(description='Update your ToDo List.')

    parser.add_argument('--add', type=str, required = False, help='a task string to add to your list')
    parser.add_argument('--due', type=str, required = False, help='due date, ideally in mm/dd/yyyy format')
    parser.add_argument('--priority', type=int, required = False, default = 3, help='priority of a task; default value is 3')
    
    parser.add_argument('--query', type=str, required = False, nargs = "+", help='what to search for within tasks')
    parser.add_argument('--list', action = 'store_true', required=False, help="list all tasks that have not been completed")
    parser.add_argument('--done', type=int, required=False, help="enter ID of task to be marked done")
    parser.add_argument('--delete',type=int, required=False, help="enter ID of task to be deleted")
    parser.add_argument('--report', action = 'store_true', required=False, help="list all tasks that have not been completed")
    
    
    #Parse the argument
    args = parser.parse_args()


    #operations based on arguments
    if args.add:
        Tasks_obj.add(args.add,args.priority,dateparser.parse(args.due))

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
