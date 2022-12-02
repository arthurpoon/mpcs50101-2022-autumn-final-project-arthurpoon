#!/usr/bin/env python 

"""timeformatting.py: module containing timezone conversions and datetime formatting

__author__      = "Arthur Poon"
__class_name__  = "Immersion Programming - M Section"
__version__ = "1.0"
__email__ = "arthur.poon@chicagobooth.edu
"""

#imported modules

import time
import datetime
import pytz

#helper function to format datetime objects to short string
def datetime_to_str(ADatetime_obj):
    """converts datetime ojbect into a string of m/d/Y format"""
    date_string = ADatetime_obj .strftime('%m/%d/%Y')
    return date_string

#helper function to format datetime objects to long format string
def datetime_to_long_str(ADatetime_obj):
    """converts datetime ojbect into a string of m/d/Y format"""
    date_string = ADatetime_obj.strftime('%a %b  %d %X %Z %Y')
    return date_string

#generate current time in CST Timezone
def get_time_in_CST():
    datetime_in_CST = datetime.datetime.now(pytz.timezone("America/Chicago"))
    return datetime_in_CST