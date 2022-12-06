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
import tabulate
import dateparser

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

        """initate task object with attributes"""

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

    """A list of `Task` objects.

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

        #iterator count to generate unique ID
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

            # dash is default value because Nonetype would prevent sorting in report function later on
            if task.completed_date == "-":
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
            #default value of completed date is a dash, not Nonetype
            if any(query_term.lower() in task.name.lower() for query_term in query_terms) and task.completed_date == "-":
                print_list.append([task.unique_id,str((timeformatting.get_time_in_CST()-task.created_date).days)+"d",task.due_date,task.priority,task.name])

        if len(print_list)==0:
            print("no tasks to print")

        else:
            print(tabulate.tabulate(print_list, headers = ["ID","Age","Due Date","Priority","Task"],colalign=("left")))

    def add(self,name,priority,due_date):

        self.iterator += 1

        #check if name is a string or an integer
        if name.isnumeric():
            print("There was an error in creating your task. Run 'todo -h' for usage instructions.")
            exit()

        #try to convert date if possible
        try:
            due_date = str(dateparser.parse(due_date))
        except:
            due_date = "-"

        #initiate new instance of Task Class depending on presence of date, needed because of the way emtpy entries are handled by timeparser to not override defaults
        new_task = Task(name,self.iterator,priority,due_date)    

        #add new task to the list of tasks
        self.tasks_list.append(new_task)
        print(f"Created task {new_task.unique_id}")

    def delete(self, to_delete_task_id):
        task_index = self.tasks_list.index([task for task in self.tasks_list if task.unique_id == to_delete_task_id][0])
        self.tasks_list.pop(task_index)

    def sort_tasks(self):
        self.tasks_list.sort(key = lambda x: (x.due_date,x.priority))
        pass


