.. _working_with_results:

Working with results
====================

.. _how_to_access_the_room_ids_in_a_results_file:

How to access the room ids in a results file
--------------------------------------------

This first opens an IES results file stored on the local computer. These are saved as *.aps* files, usually in the *vista* folder. The results file is opened using the :py:meth:`~iesve.ResultsReader.open` class method of the :py:class:`~iesve.ResultsReader` class. In the code below this is done using the ``with`` Python context manager, so the opened file is automatically closed again at the end of the ``with`` block.

Once opened, a list of the room ids within the result file can be accessed using the :py:meth:`~iesve.ResultsReader.get_room_ids` method of the :py:class:`~iesve.ResultsReader` class.

.. code-block:: python

   import iesve
   import os
   fp_in = os.path.join('vista', 'small_office.aps')  # replace this with the path to any IES results (*.aps) file.
   with iesve.ResultsReader.open(fp_in) as f:
      room_id_list = f.get_room_ids()

- `fp_in` is the filepath to a IES results file (.aps file).
- `f` is an instance of the :py:class:`~iesve.ResultsReader` class. This is returned by the :py:meth:`~iesve.ResultsReader.open` class method.
- `room_id_list` is a list of ids (str) of the rooms stored in the results file.

An example of the `room_id_list` is:

.. code-block:: python

   ['RF000000', 'NR000000', 'ST000000', 'ST000001', 'NT000000', 'WS000000']


.. _how_to_access_the_variable_information_in_a_results_file:

How to access the variable information in a results file
--------------------------------------------------------

This uses the :py:meth:`~iesve.ResultsReader.get_variables` method of the :py:class:`~iesve.ResultsReader` class to access a list of information about all the variables in a results file.

.. code-block:: python

   import iesve
   import os
   fp_in = os.path.join('vista', 'small_office.aps')  # replace this with the path to any IES results (*.aps) file.
   with iesve.ResultsReader.open(fp_in) as f:
      variables_list = f.get_variables()

- `fp_in` is the filepath to a IES results file (.aps file).
- `f` is an instance of the :py:class:`~iesve.ResultsReader` class. This is returned by the :py:meth:`~iesve.ResultsReader.open` class method.
- `variables_list` is a list of dictionaries each with information about the variables stored in the results file.

An example of a dictionary in `variables_list` might be:

.. code-block:: python 

   {
      'display_name': 'System elec. CE', 
      'aps_varname': 'System elec. CE', 
      'units_type': 'Carbon emission', 
      'model_level': 'c', 
      'subtype': 0, 
      'custom_type': iesve.VariableType.energy_meter, 
      'post_process_spec': 'u', 
      'source': iesve.VariableSource.system
   }


.. _how_to_access_the_air_temperatures_for_all_rooms_in_a_results_file:

How to access the air temperatures for all rooms in a results file
------------------------------------------------------------------

This uses the :py:meth:`~iesve.ResultsReader.get_room_results` method of the :py:class:`~iesve.ResultsReader` class to access the air temperatures stored in a results file.

.. code-block:: python

   import iesve
   import os
   fp_in = os.path.join('vista', 'small_office.aps')  # replace this with the path to any IES results (*.aps) file.
   with iesve.ResultsReader.open(fp_in) as f:
      air_temperatures_dict = {
         room_id: f.get_room_results(room_id, 'Room air temperature', 'Air temperature', 'z')
         for room_id in f.get_room_ids()
         }

- `fp_in` is the filepath to a IES results file (.aps file).
- `f` is an instance of the :py:class:`~iesve.ResultsReader` class. This is returned by the :py:meth:`~iesve.ResultsReader.open` class method.
- `air_temperatures_dict` is a dictionary with key/value pairs of {room id (str): air temperatures (numpy.array)}.


