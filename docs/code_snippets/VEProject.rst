
Working with projects
=====================


.. _how-to-access-the-current-project:

How to access the current project
---------------------------------

The "current project" represents all the information and features relating to the current modelling project in the IES-VE software. This is accessed using the :py:meth:`~iesve.VEProject.get_current_project` class method of the :py:class:`~iesve.VEProject` class.

.. code-block:: python

   import iesve
   currentproject = iesve.VEProject.get_current_project()

- `currentproject` is an instance of the :py:class:`~iesve.VEProject` class.


