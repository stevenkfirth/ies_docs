Working with models
===================


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

