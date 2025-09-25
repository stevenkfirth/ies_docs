
## python -m api


import json

# CREATE INTERMEDIATE JSON

with open('ies_scripts.json') as f:
    input_dict = json.load(f)

def parse(obj_dict):
    ""
    result = {}
    result['name'] = obj_dict['__name__']
    if not obj_dict['inspect.getdoc()'] is None:
        x = []
        for line in obj_dict['inspect.getdoc()'].split('\n'):
            if line == '':
                x.append('')
            else:
                i = len(line) - len(line.lstrip())  # index of first non-whitespace character
                x.append(f'{line[:i]}*{line[i:].rstrip()}*')
        result['doc'] = '\n'.join(x)
    else:
        result['doc'] = None
    if obj_dict['inspect.ismodule()'] == True:
        type_ = 'module'
    elif obj_dict['inspect.isclass()'] == True:
        type_ = 'class'
    elif obj_dict['inspect.isroutine()'] == True:
        type_ = 'method'
    else:
        type_ = 'attribute'
    result['type'] = type_
    if obj_dict['type().__name__'] == 'member_descriptor':
        classname = 'str'
    elif obj_dict['type().__name__'] == 'property':
        classname = None
    elif obj_dict['type().__name__'] == 'function':
        classname = None
    elif obj_dict['type().__name__'] == 'dict':
        classname = 'dict'
    else:
        classname = f'iesve.{obj_dict['type().__name__']}'
    result['classname'] = classname
    if type_ == 'attribute':
        if classname  in ['dict']:
            result['value'] = obj_dict['str()']
        else:
            result['value'] = obj_dict['int()']  
    else:
        result['value'] = None 
    result['methods_and_attributes'] = {}
    result['classes'] = {}
    for name1, obj_dict1 in obj_dict['members'].items():
        if name1 in dir(int):
            continue
        if len(obj_dict1) == 0:
            continue
        result1 = parse(obj_dict1)
        if result1['type'] == 'class':
            result['classes'][name1] = result1
        else:
            result['methods_and_attributes'][name1] = result1
    result['isclassmethod'] = False
    return result

result = {}
result['iesve'] = parse(input_dict)

# MANUAL ADDITIONS TO JSON

# iesve
x = result['iesve']
x['doc'] = 'Note: text in italics has been reproduced verbatim from the original text used in the IES-VE Python API online help guide or Python docstrings. Where I have replaced this with my own text, this is in non-italics.'

# VEProject
x = result['iesve']['classes']['VEProject']
x['doc'] = 'Represents all information and features relating to the modelling project in the IES-VE software.'

# VEProject.get_current_project
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['get_current_project']
x['doc'] = ':returns: The project currently loaded in the VE.'
x['isclassmethod'] = True
x['classname'] = 'iesve.VEProject'

# VEProject.models
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['models']
x['doc'] = ':returns: A list of "active model variants". The first item is always the "real model".'
x['classname'] = 'list[iesve.VEModel]'

# VEProject.path
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['path']
x['doc'] = ':returns: The path to the local directory of the IES-VE project.'
x['classname'] = 'str'


# VEModel
x = result['iesve']['classes']['VEModel']
x['doc'] = 'Represents a building and its systems as modelled by the user in the IES-VE software.'

# VEModel.bodies
x = result['iesve']['classes']['VEModel']['methods_and_attributes']['get_bodies']
x['name'] = 'get_bodies(selectedOnly)'
x['doc'] = ':param bool selectedOnly: Use `True` to return only the bodies already selected by the user in the IES-VE software; use `False` to return all bodies.\n\n:returns: A list of "body" instances.'
x['classname'] = 'list[iesve.VEBody]'

# VEBody
x = result['iesve']['classes']['VEBody']
x['doc'] = 'Represents a room of the building or another feature such as adjacent_building, topographical shade, local_shade or tree.\n\nSee iesve.VEBody_type for all options.'

# VEBody.type
x = result['iesve']['classes']['VEBody']['methods_and_attributes']['type']
x['doc'] = ':returns: The type of the VEBody.'
x['classname'] = 'iesve.VEBody_type'

# update the integer-like classes
for name, obj_dict in result['iesve']['classes'].items():
    if 'names' in obj_dict['methods_and_attributes']:  # if an integer-like class
        obj_dict['doc'] = 'This class acts like an integer class with additional attributes.'
        for name1, obj_dict1 in obj_dict['methods_and_attributes'].items():
            if name1 in ['name']:
                obj_dict1['doc'] = 'The name of the instance.'
                obj_dict1['isclassmethod'] = False
            elif name1 in ['names', 'values']:
                x = 'Returns the following dictionary:\n\n.. code-block:: python\n\n   {\n'
                for x1 in obj_dict1['value'].split('{')[1].split('}')[0].split(','):
                    x+= f'    {x1.strip()}\n'
                x += '   }'
                obj_dict1['doc'] = x
                obj_dict1['isclassmethod'] = True
            else:
                obj_dict1['doc'] = f'An instance of this class with:\n\n* a value of {obj_dict1['value']}\n* a name of "{name1}".'
                obj_dict1['isclassmethod'] = True
        

# SAVE JSON (just for viewing)
with open('api.json', 'w') as f:
    json.dump(result, f, indent = 4)


# CREATE .RST FILE

lines = []
lines.append('.. _api-reference:')
lines.append('')
lines.append('API Reference')
lines.append('=============')
lines.append('')

def obj_lines(name, obj_dict):
    ""
    lines = []
    if obj_dict['type'] == 'attribute':
        lines.append(f'.. py:property:: {obj_dict['name'] if obj_dict['name'] else name}')
        if obj_dict['isclassmethod'] == True:
            lines.append(f'   :classmethod:')
        if not obj_dict['classname'] is None:
            lines.append(f'   :type: {obj_dict['classname']}')
        lines.append('')
        if not obj_dict['doc'] is None:
            for x in obj_dict['doc'].split('\n'):
                lines.append(f'   {x}')
            lines.append('')
    else:
        lines.append(f'.. py:{obj_dict['type']}:: {obj_dict['name'] if obj_dict['name'] else name}')
        if obj_dict['isclassmethod'] == True:
            lines.append(f'   :classmethod:')
        lines.append('')
        if not obj_dict['doc'] is None:
            for x in obj_dict['doc'].split('\n'):
                lines.append(f'   {x}')
        lines.append('')
        if not obj_dict['classname'] in [None, 'iesve.class', 'iesve.module', 'iesve.type']:
            lines.append(f'   :rtype: {obj_dict['classname']}')
            lines.append('')
        
    return lines

for name, obj_dict in result.items():
    
    lines.extend(obj_lines(name, obj_dict))

    for name1, obj_dict1 in obj_dict['methods_and_attributes'].items():
        lines.extend([f'   {x}' for x in obj_lines(name1, obj_dict1)])

    for name1, obj_dict1 in obj_dict['classes'].items():
        lines.extend([f'   {x}' for x in obj_lines(name1, obj_dict1)])
        
        for name2, obj_dict2 in obj_dict1['methods_and_attributes'].items():
            print(name2)
            lines.extend([f'      {x}' for x in obj_lines(name2, obj_dict2)])

        #break



st = '\n'.join(lines)

with open('api.rst', 'w') as f:
    f.write(st)