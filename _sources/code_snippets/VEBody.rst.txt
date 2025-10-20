Working with bodies
===================


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
- `roombodies` is a list of :py:class:`~iesve.VEBody` instances of type :py:attr:`iesve.VEBody_type.room`.


