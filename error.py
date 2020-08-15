def check(type_C):
    a = []
    b = ()
    c = {}
    d = 1
    e = 1.1
    f = 'Hi'
    g = True

    if type(type_C) == type(a):
        return "list"
    elif type(type_C) == type(b):
        return "tuple"
    elif type(type_C) == type(c):
        return "dict"
    elif type(type_C) == type(d):
        return "integer"
    elif type(type_C) == type(e):
        return "float"
    elif type(type_C) == type(f):
        return "string"
    elif type(type_C) == type(g):
        return "boolean"
    else:
        return "Invalid_type"

def checklist(ls):
    az = check(ls)
    mainf = []
    if az == 'list':
        if len(ls) > 0:
            for x in ls:
                mainf.append(check(x))
            return mainf
        else:
            return "No data to check"
    else:
        return "Invalid type"