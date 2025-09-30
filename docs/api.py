
## python -m api


import json
import os

# CREATE INTERMEDIATE JSON

with open(os.path.join('ies_scripts', 'ies_scripts.json')) as f:
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
# Python API for the IES Virtual Environment (VE)
x = result['iesve']
x['doc'] = ""

# ResultsReader
# Support for reading simulation result files (APS files). Basic usage:
# f = iesve.ResultsReader() f.open_aps_data(filename) x = f.get_results(‘Total electricity’, ‘e’) f.close()
# or
# f = iesve.ResultsReader.open(filename) x = f.get_results(‘Total electricity’, ‘e’) f.close()
x = result['iesve']['classes']['ResultsReader']
x['doc'] = "A class used to access the results of a simulation as stored in an *.aps* file in the *vista* folder.\n\nSee also: :ref:`working_with_results`"

# ResultsReader.get_room_results()
# get_room_results(room_id, aps_var, vista_var, var_level, [start_day], [end_day]) ->
# Numpy array of floats
# Get the results for specified room + variable. See units spreadsheet for available variables and matching level. See get_results for start_day and end_day details.
x = result['iesve']['classes']['ResultsReader']['methods_and_attributes']['get_room_results']
x['name'] = "get_room_results(room_id, aps_var, vista_var, start_day = -1, end_day = -1)"
x['doc'] = ":param str room_id: The id of the room (see :py:meth:`~iesve.ResultsReader.get_room_ids`)\n\n:param str aps_var: The name of the variable as used in the .aps results file (see 'aps_varname' in :py:meth:`~iesve.ResultsReader.get_variables`.\n\n:param str vista_var: The name of the variable as used in the Vista module (see 'display_name' in :py:meth:`~iesve.ResultsReader.get_variables`).\n\n:param int start_day: The start day for the returned results (default is the first day of the simulation).\n\n:param int end_day: The end day for the returned results (default is the last day of the simulation).\n\n:returns: The values of a variable of a room in the :py:class:`~iesve.ResultsReader` instance.\n\n:rtype: numpy.array (floats)\n\nSee also: :ref:`how_to_access_the_air_temperatures_for_all_rooms_in_a_results_file`"

# ResultsReader.get_variables()
# get_variables( ) -> [ variable data ]
# Get the list of results file variables that are applicable to the loaded file. The return value is a list of dictionaries with all relevant variable data. The available data fields are:
# category, display_name, aps_varname, units_type, units_category, combine_flag, model_level, post_process, color, color_rgb, subtype, line_style, order, polarity.
x = result['iesve']['classes']['ResultsReader']['methods_and_attributes']['get_variables']
x['doc'] = ":returns: A list of dictionaries, where the dictionaries contains information about all the variables stored in a :py:class:`~iesve.ResultsReader` instance.\n\n:rtype: list\n\nEach dictionary may contain the following key/value pairs:\n\n* 'category'\n\n* 'display_name' (str): The name of the variable as used in the Vista module.\n\n* 'aps_varname' (str): The name of the variable as used in the .aps results file.\n\n* 'units_type' (str)\n\n* 'units_category'\n\n* 'combine_flag'\n\n* 'model_level' (str): One of:\n\n  * 'w': weather (used in :py:meth:`~iesve.ResultsReader.get_weather_results`)\n\n  * 'z': room level (zone) (used in :py:meth:`~iesve.ResultsReader.get_room_results`)\n\n  * 'v': apache systems misc (used in :py:meth:`~iesve.ResultsReader.get_apache_system_results`)\n\n  * 'j': apache systems energy (used in :py:meth:`~iesve.ResultsReader.get_apache_system_results`)\n\n  * 'r': apache systems carbon (used in :py:meth:`~iesve.ResultsReader.get_apache_system_results`)\n\n  * 'l': building loads (used in :py:meth:`~iesve.ResultsReader.get_results`)\n\n  * 'e': building energy (used in :py:meth:`~iesve.ResultsReader.get_results`)\n\n  * 'c': building carbon (used in :py:meth:`~iesve.ResultsReader.get_results`)\n\n  * 's': surface level (used in :py:meth:`~iesve.ResultsReader.get_surface_results`)\n\n  * 'o': opening level (used in :py:meth:`~iesve.ResultsReader.get_opening_results`)\n\n  * 'n': HVAC node level (used in :py:meth:`~iesve.ResultsReader.get_hvac_node_results`)\n\n  * 'h': HVAC component level (used in :py:meth:`~iesve.ResultsReader.get_hvac_component_results`)\n\n* 'post_process'\n\n* 'color'\n\n* 'color_rgb'\n\n* 'subtype'\n\n* 'line_style'\n\n* 'order'\n\n* 'polarity'"

# ResultsReader.open
x = result['iesve']['classes']['ResultsReader']['methods_and_attributes']['open']
x['isclassmethod'] = True
x['classname'] = 'iesve.ResultsReader'


# VEBody
x = result['iesve']['classes']['VEBody']
x['doc'] = 'Represents a room of the building or another feature such as adjacent_building, topographical shade, local_shade or tree.\n\nSee iesve.VEBody_type for all options.'

# VEBody.type
x = result['iesve']['classes']['VEBody']['methods_and_attributes']['type']
x['doc'] = ':returns: The type of the VEBody.'
x['classname'] = 'iesve.VEBody_type'

# VEBody.get_room_data
x = result['iesve']['classes']['VEBody']['methods_and_attributes']['get_room_data']
x['name'] = "get_room_data(type = iesve.attribute_type.real_attributes)"
x['doc'] = ":param type: The type of :py:class:`~iesve.VERoomData` instance to return. Options are :py:attr:`iesve.attribute_type.real_attributes` (default value), :py:attr:`iesve.attribute_type.ncm_attributes` (NCM), :py:attr:`iesve.attribute_type.bprm_attributes` (PRM) and :py:attr:`iesve.attribute_type.t_24` (Title 24).: \n\n:type type: iesve.attribute_type\n\n:returns: The :py:class:`~iesve.VERoomData` instance of the :py:class:`~iesve.VEBody`."
x['classname'] = 'iesve.VERoomData'


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

lines.append("This page shows the classes and functions for the ``iesve`` module.")
lines.append('')
lines.append("These classes are not instantiated directly, but are accessed using either class methods or regular methods on 'parent' instances. For example, to instantiate an instance of the :py:class:`~iesve.VEProject` class this is not done using ``iesve.VEProject()`` but rather by using the :py:meth:`~iesve.VEProject.get_current_project` class method, i.e. ``iesve.VEProject.get_current_project()``.")
lines.append('')
lines.append("For where to start with these classes, I would recommend the :ref:`code-snippets` page and the helpful diagram in the official IES documentation `here <https://www.iesve.com/support/faq/pdf/vescriptsguide/iiesve-class-structure-summary.pdf>`__.")
lines.append('')
lines.append("Note: text in italics has been reproduced verbatim from the original text used in the IES-VE Python API online help guide or Python docstrings. Where I have replaced this with my own text, this is in non-italics.")
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