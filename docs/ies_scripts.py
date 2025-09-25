# This script inspects the iesve module.
# - It iterates through all functions and classes in the module.
# - It exports a dictionary containing all the information it found.
# - This dictionary can then be used to create a .rst file for the documentation website.

print('--- Start ---')

import iesve
import inspect
import json
from pprint import pprint

print(iesve.AdjacentCondition_type.names)
print(iesve.AdjacentCondition_type.external_air.names)


result = {}
obj = iesve

def is_jsonable(x):
    try:
        json.dumps(x)
        return True
    except (TypeError, OverflowError):
        return False

def include_member(name):
    ""
    if name.startswith('__') or name in [

        ]:
        return False
    else:
        return True

def inspect_obj(obj, level):
    ""
    d = {}
    if level == 3: return d
    d['__doc__'] = obj.__doc__ if hasattr(obj, '__doc__') else None
    d['__name__'] = obj.__name__ if hasattr(obj, '__name__') else None
    d['__qualname__'] = obj.__qualname__ if hasattr(obj, '__qualname__') else None
    d['__module__'] = obj.__module__ if hasattr(obj, '__module__') else None
    d['inspect.getdoc()'] = inspect.getdoc(obj)
    d['inspect.getmembers()'] = [
        (name, result if is_jsonable(result) else str(result)) for name, result in inspect.getmembers(obj) 
        if include_member(name)
        ]
    d['inspect.ismodule()'] = inspect.ismodule(obj)
    d['inspect.isclass()'] = inspect.isclass(obj)
    d['inspect.ismethod()'] = inspect.ismethod(obj)
    d['inspect.isfunction()'] = inspect.isfunction(obj)
    d['inspect.isbuiltin()'] = inspect.isbuiltin(obj)
    d['inspect.isroutine()'] = inspect.isroutine(obj)
    d['inspect.isdatadescriptor()'] = inspect.isdatadescriptor(obj)
    d['inspect.isgetsetdescriptor()'] = inspect.isgetsetdescriptor(obj)
    d['inspect.ismemberdescriptor()'] = inspect.ismemberdescriptor(obj)
    try:
        d['int()'] = int(obj) 
    except:
        d['int()'] = None
    d['members'] = {}
    try:
        d['float()'] = float(obj) 
    except:
        d['float()'] = None
    d['str()'] = str(obj)
    d['type()'] = str(type(obj))
    d['type().__name__'] = str(type(obj).__name__)
    

    for name, type_ in inspect.getmembers(obj):
        if hasattr(obj, name) and not name.startswith('__'):
            obj1 = getattr(obj, name)
            d['members'][name] = inspect_obj(obj1, level + 1)
        
        
    return d

result = inspect_obj(iesve, 0)

with open('ies_scripts.json', 'w') as f:
    json.dump(result, f, indent = 4)

print('--- End ---')

quit()

iesve_dict = {}
iesve_dict['__doc__'] = obj.__doc__
iesve_dict['__name__'] = obj.__name__
iesve_dict['inspect.getdoc()'] = inspect.getdoc(obj)
iesve_dict['inspect.getmembers()'] = str(inspect.getmembers(iesve))
iesve_dict['inspect.ismodule()'] = str(inspect.getmembers(iesve))
iesve_dict['members'] = {}
iesve_dict['str()'] = str(iesve)
iesve_dict['type()'] = str(type(obj))

for name, type_ in inspect.getmembers(iesve):
    print(name, type_)
    #if not name == 'VEProject': continue
    d = {}
    obj = getattr(iesve,name)
    d['__doc__'] = obj.__doc__
    d['__name__'] = obj.__name__
    d['__qualname__'] = obj.__qualname__
    d['__module__'] = obj.__module__
    d['inspect.getdoc()'] = inspect.getdoc(obj)
    d['inspect.getmembers()'] = str(inspect.getmembers(obj))
    d['members'] = {}
    d['str()'] = str(obj)
    d['type()'] = str(type(obj))
    
    for name1, type1_ in inspect.getmembers(obj):
        print(name1, type1_)
        d1 = {}
        obj1 = getattr(obj, name1)
        d1['__doc__'] = obj1.__doc__ if hasattr(obj1, '__doc__') else None
        d1['__name__'] = obj1.__name__ if hasattr(obj1, '__name__') else None
        d1['inspect.getdoc()'] = inspect.getdoc(obj1)
        d1['inspect.getmembers()'] = str(inspect.getmembers(obj1))
        d1['type()'] = str(type(obj1))
        d1['str()'] = str(obj1)
        
        d['members'][name1] = d1
        
    iesve_dict['members'][name] = d
    
    break
    
result['iesve'] = iesve_dict



#print(result['iesve'])

