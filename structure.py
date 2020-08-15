import datetime
import os
from .error import *

"""
    Structure pf database:
    {
        "meta": {
            "name": "name",
            "created": "time",
            "password": "password"
        }

        "table_name": [
            ["col_name", {attributes}, [#data]]
        ]
    }

    attributes:

    "type": ["STR", "FLT", "BOOL", "INT", "LIST", "TLP", "DICT"] any one from the given list
    "properties": ["NOT_NULL", "PRIMARY_KEY", "AUTO_INCREMENT", {"MAX": 10}, {"MIN": 10}, "{"RANGE": 10}", "{"INDEX": 2}"]

    {"INDEX": 2} : tells the arrangement of columns in dataview and CSV conversion
    {"MAX": 10} : tells the limit of maximum value of data length
    {"MIN": 10} : tells the limit of minimul value of data length
    {"RANGE": 10} : tells the limit of maximum characters allowed
    NOT_NULL : cannot be empty
    PRIMART_KEY: Reference Cell
    AUTO_INCREMENT: The value of that particular cell will be incremented or decremented on respective insertion and deletion






"""

pos_types = ["STR", "FLT", "BOOL", "INT", "LIST", "TLP", "DICT"]

def data(dataa):
    ax = {
        "meta": {
            "name": f"{dataa[0]}",
            "created": f"{datetime.datetime.now()}",
            "password": f"{dataa[1]}"
        }
    }

    return ax

def table(name):
    ax = []
    return ax

def col(name, attr, data):
    au = list(checklist([name, attr, data]))
    if au[0] == 'string' and au[1] == 'dict' and au[2] == 'list':
        ax = [f"{name}", attr, data]
        return ax
    else:
        return "Invalid type"

def ExportCSV(table):
    #will export to a csv string
    main = ""
    for x in table:
        main = main + f"{x[0]}, "
    main = main + "\n"

    max_length = 0

    for y in table:
        max_length = len(y[2])
    
    for w in range(max_length):
        for k in table:
            main = main + f"{k[2][w]}, "
        main = main + "\n"

    return main

    
