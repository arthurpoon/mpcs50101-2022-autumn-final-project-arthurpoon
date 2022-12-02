#!/usr/bin/env python 

"""tasks.py: module containing Task and Tasks objects

__author__      = "Arthur Poon"
__class_name__  = "Immersion Programming - M Section"
__version__ = "1.0"
__email__ = "arthur.poon@chicagobooth.edu
"""

#imported standard modules

import pickle
import itertools
import argparse
import tabulate


#importing custom modules
import timeformatting


class Task:
    """Representation of a task
    
    Attributes:
                - created - date
                - completed - date
                - name - string
                - unique id - number
                - priority - int value of 1, 2, or 3; 1 is default
                - due date - date, this is optional
    """

    def __init__(self, name, unique_id, priority=3, due_date = "-" ):

        """initate task object with attributes
        
        Methods:
        - add
        - delete
        - done
        - sort_tasks
        - pickle_tasks
        - list
        - report
        - query

        """

        self.created_date = timeformatting.get_time_in_CST()
        self.completed_date = "-"
        self.name = name
        self.unique_id = unique_id
        self.priority = priority 
        self.due_date = due_date
        
    #     #check that priority is set correctly
    #     self.check_priority_bounds()

    # #method to check priority
    # def check_priority_bounds(self):
    #     if 1 <= self.priority <= 3:
    #         pass
    #     else:
    #         print("Invalid Priority, please insert int 1, 2, or 3")


class Tasks:

    """A list of `Task` objects."""

    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks_list = [] 
        # your code here
        try:
            with open('.todo.pickle','rb') as f:
                self.tasks_list = pickle.load(f)
        except:
            print("no existing file of tasks, creating new list")
            pass

        if self.tasks_list == []:
            self.iterator = 0
        else:
            self.iterator = max([task.unique_id for task in self.tasks_list])

    def pickle_tasks(self):
        """Picle your task list to a file"""
        with open('.todo.pickle', 'wb') as f:
            pickle.dump(self.tasks_list,f)

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        print_list = []
        for task in self.tasks_list:
            if task.completed_date == None:
                print_list.append([task.unique_id,str((timeformatting.get_time_in_CST()-task.created_date).days)+"d",task.due_date,task.priority,task.name])

        if len(print_list)==0:
            print("no tasks to print")

        else:
            print(tabulate.tabulate(print_list, headers = ["ID","Age","Due Date","Priority","Task"],colalign=("left")))

    def report(self):
        print_list = []
        for task in self.tasks_list:
                print_list.append([task.unique_id,\
                    str((timeformatting.get_time_in_CST()-task.created_date).days)+"d",\
                        task.due_date,\
                        task.priority,\
                        task.name,\
                        timeformatting.datetime_to_long_str(task.created_date),\
                        task.completed_date])
        
        if len(print_list)==0:
            print("no tasks to print")
        else:
            print(tabulate.tabulate(print_list, headers = ["ID","Age","Due Date","Priority","Task","Created","Completed"],colalign=("left")))

    def done(self,completed_task_id):
        task_index = self.tasks_list.index([task for task in self.tasks_list if task.unique_id == completed_task_id][0])
        self.tasks_list[task_index].completed_date = timeformatting.datetime_to_long_str(timeformatting.get_time_in_CST())

    def query(self,query_terms):
        print(f"searching for {query_terms}")
        print_list =[]
        for task in self.tasks_list:
            if any(query_term.lower() in task.name.lower() for query_term in query_terms) and task.completed_date == None:
                print_list.append([task.unique_id,str((timeformatting.get_time_in_CST()-task.created_date).days)+"d",task.due_date,task.priority,task.name])

        if len(print_list)==0:
            print("no tasks to print")

        else:
            print(tabulate.tabulate(print_list, headers = ["ID","Age","Due Date","Priority","Task"],colalign=("left")))

    def add(self,name,priority,due_date):

        self.iterator += 1

        #initiate new instance of Task Class depending on presence of date
        if due_date == None:
            new_task = Task(name,self.iterator,priority)    
        else:
            due_date = timeformatting.datetime_to_str(due_date)
            new_task = Task(name,self.iterator,priority,due_date)    


        self.tasks_list.append(new_task)
        print(f"Created task {new_task.unique_id}")

    def delete(self, to_delete_task_id):
        task_index = self.tasks_list.index([task for task in self.tasks_list if task.unique_id == to_delete_task_id][0])
        self.tasks_list.pop(task_index)

    def sort_tasks(self):
        self.tasks_list.sort(key = lambda x: (x.due_date,x.priority))
        pass


