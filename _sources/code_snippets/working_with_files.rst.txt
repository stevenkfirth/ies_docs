Working with files
==================

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




