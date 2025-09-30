
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
x['doc'] = "The iesve module\n----------------\n\nThis module contains classes and functions for working with the IES software.\n\nThe classes which are instantiated directly are:\n\n* :py:class:`~iesve.ApacheSim`\n* :py:class:`~iesve.VESankey`\n\nThe classes which are instantiated using their own class methods are:\n\n* :py:class:`~iesve.VEProject` using :py:meth:`~iesve.VEProject.get_current_project`\n\n* :py:class:`~iesve.WeatherFileReader` using :py:meth:`~iesve.WeatherFileReader.open_weather_file`\n\n* :py:class:`~iesve.ResultsReader` using :py:meth:`~iesve.ResultsReader.open`\n\n* :py:class:`~iesve.VECdbDatabase` using :py:meth:`~iesve.VECdbDatabase.get_current_database`\n\nThe classes which are never instantiated and only provide class methods are:\n\n* :py:class:`~iesve.ImportGBXML`\n\n* :py:class:`~iesve.VELocate`\n\n* :py:class:`~iesve.VERenewables`\n\n* :py:class:`~iesve.RoomGroups`\n\n* :py:class:`~iesve.PRM`\n\n* :py:class:`~iesve.Mv2`\n\n* :py:class:`~iesve.IECC`\n\n* :py:class:`~iesve.TariffsEngine`\n\n* :py:class:`~iesve.HVACNetwork`\n\n* :py:class:`~iesve.EnergySources`\n\nFor where to start with these classes, I would recommend the :ref:`code-snippets` page and the helpful diagram in the official IES documentation `here <https://www.iesve.com/support/faq/pdf/vescriptsguide/iiesve-class-structure-summary.pdf>`__.\n\nNote: text in *italics* has been reproduced verbatim from the original text used in the IES-VE Python API online help guide or Python docstrings. Where I have replaced this with my own text, this is in non-italics."

# AirExchange
x = result['iesve']['classes']['AirExchange']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEThermalTemplate` using :py:meth:`~iesve.VEThermalTemplate.get_air_exchanges`\n\n' + x['doc']

# VEApacheSystem
x = result['iesve']['classes']['VEApacheSystem']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEProject` using :py:meth:`~iesve.VEProject.apache_systems`\n\n' + x['doc']


# CasualGain
x = result['iesve']['classes']['CasualGain']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEThermalTemplate` using :py:meth:`~iesve.VEThermalTemplate.get_casual_gains`\n\n' + x['doc']

# CompactProfile
x = result['iesve']['classes']['CompactProfile']
x['doc'] = 'Subclass of: :py:class:`~iesve.GroupProfile`\n\n' + x['doc']

# DailyProfile
x = result['iesve']['classes']['DailyProfile']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEProject` using :py:meth:`~iesve.VEProject.profiles`\n\n' + x['doc']

# FreeFormProfile
x = result['iesve']['classes']['FreeFormProfile']
x['doc'] = 'Subclass of: :py:class:`~iesve.GroupProfile`\n\n' + x['doc']

# GroupProfile
x = result['iesve']['classes']['GroupProfile']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEProject` using :py:meth:`~iesve.VEProject.profiles`\n\nSubclasses: :py:class:`~iesve.CompactProfile` and :py:class:`~iesve.FreeFormProfile`\n\n' + x['doc']




# ResultsReader
# Support for reading simulation result files (APS files). Basic usage:
# f = iesve.ResultsReader() f.open_aps_data(filename) x = f.get_results(‘Total electricity’, ‘e’) f.close()
# or
# f = iesve.ResultsReader.open(filename) x = f.get_results(‘Total electricity’, ‘e’) f.close()
x = result['iesve']['classes']['ResultsReader']
x['doc'] = "Instantiated by: :py:class:`~iesve.ResultsReader` using class method :py:meth:`~iesve.ResultsReader.open`\n\nA class used to access the results of a simulation as stored in an *.aps* file in the *vista* folder.\n\nSee also: :ref:`working_with_results`"

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
x['classname'] = ':py:class:`~iesve.ResultsReader`'


# RoomAirExchange
x = result['iesve']['classes']['RoomAirExchange']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VERoomData` using :py:meth:`~iesve.VERoomData.get_air_exchanges`\n\n' + x['doc']

# RoomInternalGain
x = result['iesve']['classes']['RoomInternalGain']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VERoomData` using :py:meth:`~iesve.VERoomData.get_internal_gains`\n\n' + x['doc']


# WeatherFileReader
x = result['iesve']['classes']['WeatherFileReader']
x['doc'] = "Instantiated by: :py:class:`~iesve.WeatherFileReader` using class method :py:meth:`~iesve.WeatherFileReader.open_weather_file`\n\n" + x['doc']

# WeatherFileReader.open_weather_file
x = result['iesve']['classes']['WeatherFileReader']['methods_and_attributes']['open_weather_file']
x['isclassmethod'] = True
x['classname'] = ':py:class:`~iesve.WeatherFileReader`'


# VEAdjacency
x = result['iesve']['classes']['VEAdjacency']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VESurface` using :py:meth:`~iesve.VESurface.get_adjacencies`\n\n' + x['doc']

# VEBody
x = result['iesve']['classes']['VEBody']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEModel` using :py:meth:`~iesve.VEModel.get_bodies`, :py:meth:`~iesve.VEModel.get_bodies_and_ids`, :py:meth:`~iesve.VEModel.get_bodies_for_umhl` or :py:meth:`~iesve.VEModel.get_get_excluded_bodies_for_umlh`\n\nCan instantiate:\n\n* :py:class:`~iesve.VEComponentProcess` using :py:meth:`~iesve.VEBody.get_processes`\n* :py:class:`~iesve.VERoomData` using :py:meth:`~iesve.VEBody.get_room_data`\n* :py:class:`~iesve.VESurface` using :py:meth:`~iesve.VEBody.get_surfaces`\n\nRepresents a room of the building or another feature such as adjacent_building, topographical shade, local_shade or tree.\n\nSee :py:class:`~iesve.VEBody_type` for all options.'

# VEBody.get_processes
x = result['iesve']['classes']['VEBody']['methods_and_attributes']['get_processes']
x['classname'] = ':py:class:`~iesve.VEComponentProcess`'

# VEBody.get_room_data
x = result['iesve']['classes']['VEBody']['methods_and_attributes']['get_room_data']
x['name'] = "get_room_data(type = iesve.attribute_type.real_attributes)"
x['doc'] = ":param type: The type of :py:class:`~iesve.VERoomData` instance to return. Options are :py:attr:`iesve.attribute_type.real_attributes` (default value), :py:attr:`iesve.attribute_type.ncm_attributes` (NCM), :py:attr:`iesve.attribute_type.bprm_attributes` (PRM) and :py:attr:`iesve.attribute_type.t_24` (Title 24).: \n\n:type type: iesve.attribute_type\n\n:returns: The :py:class:`~iesve.VERoomData` instance of the :py:class:`~iesve.VEBody`."
x['classname'] = ':py:class:`~iesve.VERoomData`'

# VEBody.get_surfaces
x = result['iesve']['classes']['VEBody']['methods_and_attributes']['get_surfaces']
x['classname'] = 'list[:py:class:`~iesve.VESurface`]'

# VEBody.type
x = result['iesve']['classes']['VEBody']['methods_and_attributes']['type']
x['doc'] = ':returns: The type of the VEBody.'
x['classname'] = 'iesve.VEBody_type'

# VECdbConstruction
x = result['iesve']['classes']['VECdbConstruction']
x['doc'] = "Instantiated by: :py:class:`~iesve.VECdbProject` using :py:meth:`~iesve.VECdbProject.get_construction`\n\nCan instantiate:\n\n* :py:class:`~iesve.VECdbLayer` using :py:meth:`~iesve.VECdbConstruction.get_layers`\n\n\n" + x['doc']

# VECdbConstruction.get_layers
x = result['iesve']['classes']['VECdbConstruction']['methods_and_attributes']['get_layers']
x['classname'] = 'list[:py:class:`~iesve.VECdbLayer`]'


# VECdbDatabase
x = result['iesve']['classes']['VECdbDatabase']
x['doc'] = "Instantiated by: :py:class:`~iesve.VECdbDatabase` using class method :py:meth:`~iesve.VECdbDatabase.get_current_database`\n\nCan instantiate:\n\n* :py:class:`~iesve.VECdbProject` using :py:meth:`~iesve.VECdbDatabase.get_projects`\n\n\n" + x['doc']

# VECdbDatabase.get_current_database
x = result['iesve']['classes']['VECdbDatabase']['methods_and_attributes']['get_current_database']
x['isclassmethod'] = True
x['classname'] = ':py:class:`~iesve.VECdbDatabase`'

# VECdbDatabase.get_projects
x = result['iesve']['classes']['VECdbDatabase']['methods_and_attributes']['get_projects']
x['doc'] = "Returns a dictionary with the following optional keys:\n\n* :py:attr:`iesve.project_types.project` (integer value = 0)\n* :py:attr:`iesve.project_types.system` (integer value = 1)\n* :py:attr:`iesve.project_types.manufacturer` (integer value = 2)\n\n" + x['doc']
x['classname'] = 'dict[:py:class:`~iesve.project_types`, list[:py:class:`~iesve.VECdbProject`]]'

# VECdbLayer
x = result['iesve']['classes']['VECdbLayer']
x['doc'] = "Instantiated by: :py:class:`~iesve.VECdbConstruction` using :py:meth:`~iesve.VECdbConstruction.get_layers`\n\nCan instantiate:\n\n* :py:class:`~iesve.VECdbMaterial` using :py:meth:`~iesve.VECdbLayer.get_material`\n\n\n" + x['doc']

# VECdbLayer.get_material
x = result['iesve']['classes']['VECdbLayer']['methods_and_attributes']['get_material']
x['classname'] = ':py:class:`~iesve.VECdbMaterial`'

# VECdbMaterial
x = result['iesve']['classes']['VECdbMaterial']
x['doc'] = "Instantiated by: :py:class:`~iesve.VECdbProject` using :py:meth:`~iesve.VECdbProject.get_material`, or :py:class:`~iesve.VECdbLayer` using :py:meth:`~iesve.VECdbLayer.get_material`\n\n" + x['doc']


# VECdbProject
x = result['iesve']['classes']['VECdbProject']
x['doc'] = "Instantiated by: :py:class:`~iesve.VECdbDatabase` using :py:meth:`~iesve.VECdbDatabase.get_projects`\n\nCan instantiate:\n\n* :py:class:`~iesve.VECdbConstruction` using :py:meth:`~iesve.VECdbProject.get_construction`\n* :py:class:`~iesve.VECdbMaterial` using :py:meth:`~iesve.VECdbProject.get_material`\n\n" + x['doc']

# VECdbProject.get_construction
x = result['iesve']['classes']['VECdbProject']['methods_and_attributes']['get_construction']
x['name'] = 'get_construction(construction_id, construction_type)'
x['doc'] = ":param str construction_id: The id of the construction. \n:param construction_type: The type of construction.\n:type construction_type: iesve.construction_class\n\n" + x['doc']
x['classname'] = ':py:class:`~iesve.VECdbConstruction`'

# VECdbProject.get_construction_ids
x = result['iesve']['classes']['VECdbProject']['methods_and_attributes']['get_construction_ids']
x['name'] = 'get_construction_ids(construction_type)'
x['doc'] = ":param construction_type: The type of construction.\n:type construction_type: iesve.construction_class\n\n" + x['doc']
x['classname'] = 'list[str]'

# VECdbProject.get_material
x = result['iesve']['classes']['VECdbProject']['methods_and_attributes']['get_material']
x['name'] = 'get_material(material_id)'
x['doc'] = ":param str material_id: The id of the material.\n\n" + x['doc']
x['classname'] = ':py:class:`~iesve.VECdbMaterial`'

# VECdbProject.get_material_ids
x = result['iesve']['classes']['VECdbProject']['methods_and_attributes']['get_material_ids']
x['name'] = 'get_material_ids(material_category)'
x['doc'] = ":param material_category: The category of the material.\n:type material_category: iesve.material_categories\n\n" + x['doc']
x['classname'] = 'list[str]'


# VEComponentProcess
# Provides access to the object process data for a component process.
x = result['iesve']['classes']['VEComponentProcess']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEBody` using :py:meth:`~iesve.VEBody.get_processes`\n\n' + x['doc']

# VEGeometry
x = result['iesve']['classes']['VEGeometry']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VESurface` using :py:meth:`~iesve.VESurface.get_opening_by_id` or :py:meth:`~iesve.VESurface.get_openings`\n\n' + x['doc']


# VEMacroFlo
x = result['iesve']['classes']['VEMacroFlo']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEProject` using :py:meth:`~iesve.VEProject.get_macro_flo_opening_by_id` or :py:meth:`~iesve.VEProject.get_macro_flo_opening_types`\n\n' + x['doc']


# VEModel
x = result['iesve']['classes']['VEModel']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEProject` using :py:attr:`~iesve.VEProject.models`\n\nCan Instantiate:\n\n* :py:class:`~iesve.VEBody` using :py:meth:`~iesve.VEModel.get_bodies`, :py:meth:`~iesve.VEModel.get_bodies_and_ids`, :py:meth:`~iesve.VEModel.get_bodies_for_umhl` or :py:meth:`~iesve.VEModel.get_get_excluded_bodies_for_umlh`\n* :py:class:`~iesve.VESuncast` using :py:meth:`~iesve.VEModel.suncast`\n\nRepresents a building and its systems as modelled by the user in the IES-VE software.'

# VEModel.get_bodies
x = result['iesve']['classes']['VEModel']['methods_and_attributes']['get_bodies']
x['name'] = 'get_bodies(selectedOnly)'
x['doc'] = ':param bool selectedOnly: Use `True` to return only the bodies already selected by the user in the IES-VE software; use `False` to return all bodies.\n\n:returns: A list of "body" instances.'
x['classname'] = 'list[:py:class:`~iesve.VEBody`]'

# VEModel.get_bodies_and_ids
x = result['iesve']['classes']['VEModel']['methods_and_attributes']['get_bodies_and_ids']
x['classname'] = 'dict[room_id (str): :py:class:`~iesve.VEBody`]'

# VEModel.get_bodies_for_umlh
x = result['iesve']['classes']['VEModel']['methods_and_attributes']['get_bodies_for_umlh']
x['classname'] = 'list[:py:class:`~iesve.VEBody`]'

# VEModel.get_excluded_bodies_for_umlh
x = result['iesve']['classes']['VEModel']['methods_and_attributes']['get_excluded_bodies_for_umlh']
x['classname'] = 'list[:py:class:`~iesve.VEBody`]'

# VEModel.suncast
x = result['iesve']['classes']['VEModel']['methods_and_attributes']['suncast']
x['classname'] = ':py:class:`~iesve.VESuncast`'


# VERoomData
# Interface for VERoomData object.
x = result['iesve']['classes']['VERoomData']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEBody` using :py:meth:`~iesve.VEBody.get_room_data`\n\nCan instantiate:\n\n* :py:class:`~iesve.RoomAirExchange` using :py:meth:`~iesve.VERoomData.get_air_exchanges`\n* :py:class:`~iesve.RoomInternalGain` using :py:meth:`~iesve.VERoomData.get_internal_gains`\n\n'

# VERoomData.get_air_exchanges
x = result['iesve']['classes']['VERoomData']['methods_and_attributes']['get_air_exchanges']
x['classname'] = ':py:class:`~iesve.RoomAirExchange`'

# VERoomData.get_internal_gains
x = result['iesve']['classes']['VERoomData']['methods_and_attributes']['get_internal_gains']
x['classname'] = ':py:class:`~iesve.RoomInternalGain`'

# VEProfile
x = result['iesve']['classes']['VEProject']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEProject` using :py:meth:`~iesve.VEProject.profiles`\n\nCan instantiate:\n\n* :py:class:`~iesve.RoomAirExchange` using :py:meth:`~iesve.VERoomData.get_air_exchanges`\n* :py:class:`~iesve.RoomInternalGain` using :py:meth:`~iesve.VERoomData.get_internal_gains`\n\n' + x['doc']


# VEProject
x = result['iesve']['classes']['VEProject']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEProject` using class method :py:meth:`~iesve.VEProject.get_current_project`\n\nCan instantiate:\n\n* :py:class:`~iesve.VEModel` using :py:attr:`~iesve.VEProject.models`\n* :py:class:`~iesve.VEThermalTemplate` using :py:meth:`~iesve.VEProject.thermal_templates`\n* :py:class:`~iesve.VEProfile` using :py:meth:`~iesve.VEProject.profiles`\n* :py:class:`~iesve.VEApacheSystem` using :py:meth:`~iesve.VEProject.apache_systems`\n* :py:class:`~iesve.VEMacroFlo` using :py:meth:`~iesve.VEProject.get_macro_flo_opening_by_id` or :py:meth:`~iesve.VEProject.get_macro_flo_opening_types`\n\nRepresents all information and features relating to the modelling project in the IES-VE software.'

# VEProject.apache_systems
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['apache_systems']
x['classname'] = 'list[:py:class:`~iesve.VEApacheSystem`]'

# VEProject.get_current_project
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['get_current_project']
x['doc'] = ':returns: The project currently loaded in the VE.'
x['isclassmethod'] = True
x['classname'] = ':py:class:`~iesve.VEProject`'

# VEProject.get_macro_flo_opening_by_id
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['get_macro_flo_opening_by_id']
x['classname'] = ':py:class:`~iesve.VEMacroFlo`'

# VEProject.get_macro_flo_opening_types
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['get_macro_flo_opening_types']
x['classname'] = 'list[:py:class:`~iesve.VEMacroFlo`]'

# VEProject.models
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['models']
x['doc'] = ':returns: A list of "active model variants". The first item is always the "real model".'
x['classname'] = 'list[iesve.VEModel]'

# VEProject.path
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['path']
x['doc'] = ':returns: The path to the local directory of the IES-VE project.'
x['classname'] = 'str'

# VEProject.profiles
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['profiles']
x['classname'] = 'tuple[dict[profile_id (str): :py:class:`~iesve.DailyProfile`], dict[profile_id (str): :py:class:`~iesve.GroupProfile`]]'

# VEProject.thermal_templates
x = result['iesve']['classes']['VEProject']['methods_and_attributes']['thermal_templates']
x['classname'] = 'dict[template_handle (str): :py:class:`~iesve.VEThermalTemplate`]'


# VESuncast
x = result['iesve']['classes']['VESuncast']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEModel` using :py:meth:`~iesve.VEModel.suncast`\n\n' + x['doc']

# VESurface
x = result['iesve']['classes']['VESurface']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEBody` using :py:meth:`~iesve.VEBody.get_surfaces`\n\nCan instantiate:\n\n* :py:class:`~iesve.VEAdjacency` using :py:meth:`~iesve.VESurface.get_adjacencies`\n* :py:class:`~iesve.VEGeometry` using :py:meth:`~iesve.VESurface.get_opening_by_id` or :py:meth:`~iesve.VESurface.get_openings`\n\n' + x['doc']

# VESurface.get_adjacencies
x = result['iesve']['classes']['VESurface']['methods_and_attributes']['get_adjacencies']
x['classname'] = 'list[:py:class:`~iesve.VEAdjacency`]'

# VESurface.get_opening_by_id
x = result['iesve']['classes']['VESurface']['methods_and_attributes']['get_opening_by_id']
x['classname'] = ':py:class:`~iesve.VEGeometry`'

# VESurface.get_opening_by_id
x = result['iesve']['classes']['VESurface']['methods_and_attributes']['get_openings']
x['classname'] = 'list[:py:class:`~iesve.VEGeometry`]'





# VEThermalTemplate
x = result['iesve']['classes']['VEThermalTemplate']
x['doc'] = 'Instantiated by: :py:class:`~iesve.VEProject` using :py:meth:`~iesve.VEProject.thermal_templates`\n\nCan instantiate:\n\n* :py:class:`~iesve.AirExchange` using :py:meth:`~iesve.VEThermalTemplate.get_air_exchanges`\n* :py:class:`~iesve.CasualGain` using :py:meth:`~iesve.VEThermalTemplate.get_casual_gains`\n\n' + x['doc']



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



def obj_lines(name, obj_dict, member_of):
    ""
    lines = []
    if obj_dict['type'] == 'attribute':
        lines.append(f'.. py:property:: {obj_dict['name'] if obj_dict['name'] else name}')
        if obj_dict['isclassmethod'] == True:
            lines.append(f'   :classmethod:')
        if not obj_dict['classname'] is None:
            lines.append(f'   :type: {obj_dict['classname']}')
        lines.append('')
        if not member_of is None:
            lines.append(f'   Member of: :py:{"class:`~iesve." if not member_of == "iesve" else "mod:`"}{member_of}`')
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
        if obj_dict['type'] == 'class':
            lines.append('   Parent module: :py:mod:`iesve`')
            lines.append('')
        else:
            if not member_of is None:
                lines.append(f'   Member of: :py:{"class:`~iesve." if not member_of == "iesve" else "mod:`"}{member_of}`')
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
    
    lines.extend(obj_lines(name, obj_dict, None))

    for name1, obj_dict1 in obj_dict['methods_and_attributes'].items():
        lines.extend([f'   {x}' for x in obj_lines(name1, obj_dict1, name)])

    for name1, obj_dict1 in obj_dict['classes'].items():
        lines.extend([f'   {x}' for x in obj_lines(name1, obj_dict1, name)])
        
        for name2, obj_dict2 in obj_dict1['methods_and_attributes'].items():
            print(name2)
            lines.extend([f'      {x}' for x in obj_lines(name2, obj_dict2, name1)])

        #break



st = '\n'.join(lines)

with open('api.rst', 'w') as f:
    f.write(st)