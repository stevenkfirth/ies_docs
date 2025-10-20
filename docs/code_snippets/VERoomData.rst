Working with room data
======================


.. _how-to-access-the-room-data-of-rooms-in-the-real-model:

How to access the room data of rooms in the real model
------------------------------------------------------

The "room data" here refers to the :py:class:`~iesve.VERoomData` class which allows access to information about a room and also methods to make changes to the room. These are accessed using the :py:meth:`~iesve.VEBody.get_room_data` method of the :py:class:`~iesve.VEBody` class. 

The code below uses a Python dictionary comprehension statement to create a Python dictionary ``roombodies_room_data_dict`` to hold the :py:class:`~iesve.VERoomData` instances for all rooms.

.. code-block:: python

   import iesve
   import os
   import iesve
   currentproject = iesve.VEProject.get_current_project()
   realmodel = currentproject.models[0]
   bodies = realmodel.get_bodies(False)  # SelectedOnly = False; used to select all bodies in the model.
   roombodies = [x for x in bodies if x.type == iesve.VEBody_type.room]  # iesve.VEBody_type.room has an integer value of 1.
   roombodies_room_data_dict = {body.id: body.get_room_data() for body in bodies}


- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.
- `realmodel` is an instance of the :py:class:`~iesve.VEModel` class.
- `bodies` is a list of :py:class:`~iesve.VEBody` instances.
- `roombodies` is a list of :py:class:`~iesve.VEBody` instances of type :py:attr:`iesve.VEBody_type.room`.
- `roombodies_room_data_dict` is a dictionary of {:py:attr:`iesve.VEBody.id`: :py:class:`~iesve.VERoomData` instances}. :py:attr:`iesve.VEBody.id` is the id of the room as seen in the ModelIT section.


How to access the room general information for all rooms
--------------------------------------------------------

This code uses the :py:meth:`~iesve.VERoomData.get_general` method of the :py:class:`~iesve.VERoomData` class to access the general information about a room such as its name, area and volume.

.. code-block:: python

   import iesve
   import os
   import iesve
   currentproject = iesve.VEProject.get_current_project()
   realmodel = currentproject.models[0]
   bodies = realmodel.get_bodies(False)  # SelectedOnly = False; used to select all bodies in the model.
   roombodies = [x for x in bodies if x.type == iesve.VEBody_type.room]  # iesve.VEBody_type.room has an integer value of 1.
   roombodies_room_data_dict = {body.id: body.get_room_data(type = iesve.attribute_type.real_attributes) for body in bodies}
   roombodies_room_data_general_dict = {body_id: room_data.get_general() for body_id, room_data in roombodies_room_data_dict.items()}

- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.
- `realmodel` is an instance of the :py:class:`~iesve.VEModel` class.
- `bodies` is a list of :py:class:`~iesve.VEBody` instances.
- `roombodies` is a list of :py:class:`~iesve.VEBody` instances of type :py:attr:`iesve.VEBody_type.room`.
- `roombodies_room_data_dict` is a dictionary of {:py:attr:`iesve.VEBody.id`: :py:class:`~iesve.VERoomData` instances}. :py:attr:`iesve.VEBody.id` is the id of the room as seen in the ModelIT section.
- `roombodies_room_data_general_dict` is a dictionary of {:py:attr:`iesve.VEBody.id`: dictionary as returned by the :py:meth:`iesve.VERoomData.get_general` method}. 

An example of a :py:meth:`iesve.VERoomData.get_general` return value is: 

.. code-block:: python

   {
      'name': 'ROOF', 
      'general_template': 1, 
      'general_template_name': 'default', 
      'thermal_template': 4, 
      'thermal_template_name': 'Void', 
      'id': 'RF000000', 
      'volume': 714.7855251355139, 
      'facade_area': 0.0, 
      'floor_area': 0.0, 
      'included_in_building_floor_area': True, 
      'included_in_building_floor_area_from_template': True, 
      'lettable_perc': 100, 
      'lettable_perc_from_template': True, 
      'circ_perc': 0, 
      'circ_perc_from_template': True
   }


How to access the room conditions information for all rooms
-----------------------------------------------------------

This code uses the :py:meth:`~iesve.VERoomData.get_room_conditions` method of the :py:class:`~iesve.VERoomData` class to access the general information about a room such as its name, area and volume.

.. code-block:: python

   import iesve
   import os
   import iesve
   currentproject = iesve.VEProject.get_current_project()
   realmodel = currentproject.models[0]
   bodies = realmodel.get_bodies(False)  # SelectedOnly = False; used to select all bodies in the model.
   roombodies = [x for x in bodies if x.type == iesve.VEBody_type.room]  # iesve.VEBody_type.room has an integer value of 1.
   roombodies_room_data_dict = {body.id: body.get_room_data(type = iesve.attribute_type.real_attributes) for body in bodies}
   roombodies_room_data_room_conditions_dict = {body_id: room_data.get_room_conditions() for body_id, room_data in roombodies_room_data_dict.items()}

- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.
- `realmodel` is an instance of the :py:class:`~iesve.VEModel` class.
- `bodies` is a list of :py:class:`~iesve.VEBody` instances.
- `roombodies` is a list of :py:class:`~iesve.VEBody` instances of type :py:attr:`iesve.VEBody_type.room`.
- `roombodies_room_data_dict` is a dictionary of {:py:attr:`iesve.VEBody.id`: :py:class:`~iesve.VERoomData` instances}. :py:attr:`iesve.VEBody.id` is the id of the room as seen in the ModelIT section.
- `roombodies_room_data_room_conditions_dict` is a dictionary of {:py:attr:`iesve.VEBody.id`: dictionary as returned by the :py:meth:`iesve.VERoomData.get_room_conditions` method}. 

An example of a :py:meth:`iesve.VERoomData.get_room_conditions` return value is: 

.. code-block:: python

   {
      'cooling_profile': 'ON',
      'cooling_profile_from_template': True,
      'cooling_setpoint': 23.0,
      'cooling_setpoint_constant': True,
      'cooling_setpoint_from_template': True,
      'cooling_setpoint_profile': '-',
      'cooling_setpoint_type': iesve.setpoint_type.constant,
      'dhw': 0.0,
      'dhw_from_template': True,
      'dhw_linked_to_occupancy': True,
      'dhw_linked_to_occupancy_from_template': True,
      'dhw_profile': '-',
      'dhw_profile_from_template': '-',
      'dhw_room_level_setting': 1,
      'dhw_room_level_setting_from_template': 1,
      'dhw_unit': 'l/(h·pers)',
      'dhw_unit_val': 0,
      'furniture_mass_factor': 1.0,
      'furniture_mass_factor_from_template': True,
      'heating_profile': 'ON',
      'heating_profile_from_template': True,
      'heating_setpoint': 19.0,
      'heating_setpoint_constant': True,
      'heating_setpoint_from_template': True,
      'heating_setpoint_profile': '-',
      'heating_setpoint_twovalue_main_setpoint': '-',
      'heating_setpoint_twovalue_profile': '-',
      'heating_setpoint_twovalue_setback': '-',
      'heating_setpoint_type': iesve.setpoint_type.constant,
      'max_cooling_and_dehumidification': 0.0,
      'max_dehumidification': 0.0,
      'max_heating_and_humidification': 0.0,
      'max_humidification': 0.0,
      'plant_profile': 'ON',
      'plant_profile_from_template': True,
      'plant_profile_type': 0,
      'plant_profile_type_str': 'Set to heating profile',
      'sat_perc_lower': 0.0,
      'sat_perc_lower_from_template': True,
      'sat_perc_upper': 100.0,
      'sat_perc_upper_from_template': True,
      'solar_reflected_fraction': 0.05,
      'solar_reflected_fraction_from_template': True
   }


   