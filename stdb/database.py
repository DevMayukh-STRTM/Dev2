import os
import re
import datetime
import pickle

from . import structure

class database:
    def __init__(self, attr):
        self.credintial = attr
    
    def createDatabase(self):
        #attr[0] = filename
        #attr[1] = password
        if os.path.isfile(f"{self.credintial[0]}"):
            return f"Error: Database '{self.credintial[0]}' Already Exist"
        else:
            pickle.dump(structure.data(self.credintial), open(f"{self.credintial[0]}.stdb", 'wb'))
            return f"Success: Database '{self.credintial[0]}' Created"

    def validate(self):
        if os.path.isfile(f"{self.credintial[0]}"):
            pickle.dump(structure.data(self.credintial), open(f"{self.credintial[0]}", 'wb'))
            return f"Success: Database '{self.credintial[0]}' has been validated"
        else:
            return f"Error: Database '{self.credintial[0]}' does not exists"
    
    def createTable(self, table):
        if os.path.isfile(f"{self.credintial[0]}.stdb"):
            ax = pickle.load(open(f"{self.credintial[0]}.stdb", 'rb'))
            if ax["meta"]["password"] == self.credintial[1] or ax["meta"]["password"] == 'None':
                if table in ax:
                    return "Table Already Exist"
                else:
                    ax[f"{table}"] = []
                    pickle.dump(ax, open(f"{self.credintial[0]}.stdb", 'wb'))
                    return "Created Table"
            else:
                return "Invalid Password"
        else:
            return "Invalid database"

    def createCol(self, table, name, attr):
        if os.path.isfile(f"{self.credintial[0]}.stdb"):
            ax = pickle.load(open(f"{self.credintial[0]}.stdb", 'rb'))
            if ax["meta"]["password"] == self.credintial[1] or ax["meta"]["password"] == 'None':
                if table in ax:
                    for x in ax[f"{table}"]:
                        if x[0] == name:
                            return "Column Already Exist"
                            exit()
                        else:
                            pass
                    
                    ax[f"{table}"].append(structure.col(name, attr, []))
                    pickle.dump(ax, open(f"{self.credintial[0]}.stdb", 'wb'))
                else:
                    return "Invalid Table"
            else:
                return 'Invalid Password'
        else:
            return "Invalid Database"

    def exportCSV(self, table):
        if os.path.isfile(f"{self.credintial[0]}"):
            ax = pickle.load(open(f"{self.credintial[0]}.stdb", 'rb'))
            if ax["meta"]["password"] == self.credintial[1] or ax["meta"]["password"] == 'None':
                if table in ax:
                    doc = structure.ExportCSV(table)
                    kr = open(f"{table}.csv", 'w')
                    kr.write(doc)
                    kr.close()
                else:
                    return "Invalid Table"
            else:
                return "Invalid Password"
        else:
            return "Invalid Database"