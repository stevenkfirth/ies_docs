Quick Start
===========

Installation
------------

Download and install the `IES-VE software <https://www.iesve.com/software/virtual-environment>`__. There is no need to install Python separately, as a version of Python is included in the IES-VE software.

Open the VEScript Python Editor
-------------------------------

In the IES-VE software, select the menu items `Tools/VE Scripts`. This will open a separate window where you can create and run IES Python scripts.

Create a IES Python script
--------------------------

- Click on the `New` button.
- Click on the `Save` button and save the (empty) script as a file on your computer.
- Type the following text into the (currently empty) Code Box.

.. code-block:: python

   import iesve
   print(iesve.get_application_folder())

Run the Python script
---------------------

- With the cursor inside the Code Box, press `F5`.
- You should see something like the following text appear in the Output Box.

.. code-block::

     >>> Run start, Sun Aug 24 07:20:24 2025
   C:\Program Files\IES\VE 2023\apps\
     >>> Runtime: 0.01 seconds

This has printed out the folder where the IES-VE software is installed on your computer.

Next steps
----------

- See the :ref:`code-snippets` page for demonstrations of how to achieve small individual actions using IES Python scripts.

- See the :ref:`example-scripts` page for examples of complete IES Python scripts.

- See the :ref:`api-reference` page for the documentation of the Python classes and methods made available by the IES-VE Python API.

