.. _code-snippets:

Code Snippets
=============


.. _how-to-access-the-current-project:

How to access the current project
---------------------------------

The "current project" represents all the information and features relating to the current modelling project in the IES-VE software. This is accessed using the :py:meth:`~iesve.VEProject.get_current_project` method of the :py:class:`~iesve.VEProject` class.

.. code-block:: python

   import iesve
   currentproject = iesve.VEProject.get_current_project()

- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.


.. _how-to-access-the-real-model:

How to access the real model
----------------------------

The "real model" enables access to more detailed information such as the room data and heating system of the building in the IES project. The real model is always the first item of the :py:attr:`~iesve.VEProject.models` property of the :py:class:`~iesve.VEProject` class. 

.. code-block:: python

   import iesve
   currentproject = iesve.VEProject.get_current_project()
   realmodel = currentproject.models[0]

- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.
- `realmodel` is an instance of the :py:class:`~iesve.VEModel` class.


.. _how-to-access-the-bodies-in-the-real-model:

How to access the bodies in the real model
------------------------------------------

The "bodies" of a model are rooms or other features such as an adjacent_building, a topographical shade, a local_shade or a tree. These are accessed using the :py:meth:`~iesve.VEModel.get_bodies` method of the :py:class:`~iesve.VEModel` class. 

.. code-block:: python

   import iesve
   currentproject = iesve.VEProject.get_current_project()
   realmodel = currentproject.models[0]
   bodies = realmodel.get_bodies(False)   # SelectedOnly = False; used to select all bodies in the model.

- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.
- `realmodel` is an instance of the :py:class:`~iesve.VEModel` class.
- `bodies` is a list of :py:class:`~iesve.VEBody` instances.


.. _how-to-access-the-room-bodies-in-the-real-model:

How to access the room bodies in the real model
-----------------------------------------------

This uses the :py:meth:`~iesve.VEModel.get_bodies` method of the :py:class:`~iesve.VEModel` class to access the "bodies" in the real model. The returned list of bodies is then filtered using a Python list comprehension statement to return only those bodies which are rooms (i.e. those bodies where the :py:attr:`~iesve.VEBody.type` property is equal to the :py:attr:`iesve.VEBody_type.room` instance). 

.. code-block:: python

   import iesve
   currentproject = iesve.VEProject.get_current_project()
   realmodel = currentproject.models[0]
   bodies = realmodel.get_bodies(False)   # SelectedOnly = False; used to select all bodies in the model.
   roombodies = [x for x in bodies if x.type == iesve.VEBody_type.room]  # iesve.VEBody_type.room has an integer value of 1.

- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.
- `realmodel` is an instance of the :py:class:`~iesve.VEModel` class.
- `bodies` is a list of :py:class:`~iesve.VEBody` instances.
- `roombodies` is a list of :py:class:`~iesve.VEBody` instances.


.. _how-to-access-the-path-of-the-current-project:

How to access the path of the current project
---------------------------------------------

This gets the directory where the current IES-VE project is stored on the local computer. This is done using the :py:attr:`~iesve.VEProject.path` propoerty of the :py:class:`~iesve.VEProject` class. If no path exists, the built-in Python GUI package `Tkinter <https://docs.python.org/3/library/tkinter.html>`__ is used to display an error message box.

.. code-block:: python

   import iesve
   import os
   from tkinter import Tk, messagebox
   currentproject = iesve.VEProject.get_current_project()
   dir_currentproject = currentproject.path
   if dir_currentproject == '':  # if no path exists, show an error message box then exit.
      root = Tk()
      root.withdraw()
      messagebox.showinfo('User action required', 'Please save the IES-VE project.', parent = root)
      root.destroy()
      quit()

- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.
- `dir_currentproject` is a string of the full path to the IES-VE project as saved on the local computer.


.. _how-to-ask-the-user-to-choose-a-ies-ve-results-file:

How to ask the user to choose a IES-VE result file
--------------------------------------------------

This opens a dialog box for the user to select an IES-VE results file (an .aps file). The built-in Python GUI package `Tkinter <https://docs.python.org/3/library/tkinter.html>`__ is used to display an error message box if no file is selected or the file selected is not in the current IES-VE project.

.. code-block:: python

   import iesve
   from tkinter import Tk, messagebox
   from tkinter.filedialog import askopenfilename
   import os
   currentproject = iesve.VEProject.get_current_project()
   dir_currentproject = currentproject.path
   dir_vista = os.path.join(dir_currentproject, 'vista')
   root = Tk()
   root.withdraw()
   fp_in = askopenfilename(title = 'Select IES results file', parent = root, initialdir = dir_vista, filetypes = [("APS files","*.aps")])
   root.destroy()
   # - Exit if filepath is empty string
   if fp_in == '':
      root = Tk()
      root.withdraw()
      messagebox.showinfo('User input needed', 'Please select a .aps results file.', parent = root)
      root.destroy()
      quit()
   # - Exit if filepath is not in project filepath
   elif not dir_currentproject in fp_in:
      root = Tk()
      root.withdraw()
      messagebox.showinfo('User input needed', 'Please select a .aps results file in the current IES project.', parent = root)
      root.destroy()
      quit()
   
- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.
- `dir_currentproject` is a string of the full path to the IES-VE project as saved on the local computer.
- `dir_vista` is a string of the full path to the vista folder of the IES-VE project as saved on the local computer. This is where the .aps results files are stored.
- `fp_in` is a string of the full path to the IES-VE results file as chosen by the user.




