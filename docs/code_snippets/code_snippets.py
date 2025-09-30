# HOW TOS

print('--- How to access the current project ---')
import iesve
currentproject = iesve.VEProject.get_current_project()
print(currentproject)

print('--- How to access the real model ---')
import iesve
currentproject = iesve.VEProject.get_current_project()
realmodel = currentproject.models[0]
print(realmodel)

print('--- How to access the bodies in the real model ---')
import iesve
currentproject = iesve.VEProject.get_current_project()
realmodel = currentproject.models[0]
bodies = realmodel.get_bodies(False)
print(bodies)

print('--- How to access the room bodies in the real model ---')
import iesve
currentproject = iesve.VEProject.get_current_project()
realmodel = currentproject.models[0]
bodies = realmodel.get_bodies(False)
roombodies = [x for x in bodies if x.type == iesve.VEBody_type.room]
print(roombodies)

print('--- How to access the path of the current project ---')
import iesve
import os
currentproject = iesve.VEProject.get_current_project()
dir_currentproject = currentproject.path
# Exit if no path exists
if dir_currentproject == '':
  root = Tk()
  root.withdraw()
  messagebox.showinfo('User action required', 'Please save the IES-VE project.', parent = root)
  root.destroy()
  quit()
print(currentproject.path)


print('--- How to access the room data for all rooms in the real model ---')
import iesve
import os
import iesve
currentproject = iesve.VEProject.get_current_project()
realmodel = currentproject.models[0]
bodies = realmodel.get_bodies(False)  # SelectedOnly = False; used to select all bodies in the model.
roombodies = [x for x in bodies if x.type == iesve.VEBody_type.room]  # iesve.VEBody_type.room has an integer value of 1.
roombodies_room_data_dict = {body.id: body.get_room_data(type = iesve.attribute_type.real_attributes) for body in bodies}
print(roombodies_room_data_dict)
# for k,v in roombodies_room_data_dict.items(): print(k, v)

print('--- How to access the room general information for all rooms ---')
import iesve
import os
import iesve
currentproject = iesve.VEProject.get_current_project()
realmodel = currentproject.models[0]
bodies = realmodel.get_bodies(False)  # SelectedOnly = False; used to select all bodies in the model.
roombodies = [x for x in bodies if x.type == iesve.VEBody_type.room]  # iesve.VEBody_type.room has an integer value of 1.
roombodies_room_data_dict = {body.id: body.get_room_data(type = iesve.attribute_type.real_attributes) for body in bodies}
roombodies_room_data_general_dict = {body_id: room_data.get_general() for body_id, room_data in roombodies_room_data_dict.items()}
print(roombodies_room_data_general_dict)
print(roombodies_room_data_general_dict['RF000000'])

print('--- How to access the room ids in a results file ---')
import iesve
import os
fp_in = os.path.join(os.pardir, os.pardir, '_ies_model', 'small_office', 'vista', 'small_office.aps')  # replace this with the path to any IES results (*.aps) file.
with iesve.ResultsReader.open(fp_in) as f:
    room_id_list = f.get_room_ids()
print(room_id_list)

print('--- How to access the variable information in a results file ---')
import iesve
import os
fp_in = os.path.join(os.pardir, os.pardir, '_ies_model', 'small_office', 'vista', 'small_office.aps')  # replace this with the path to any IES results (*.aps) file.
with iesve.ResultsReader.open(fp_in) as f:
    variables_list = f.get_variables()
print(variables_list)
print(variables_list[0])

print('--- How to access the air temperatures for all rooms in a results file ---')
import iesve
import os
fp_in = os.path.join(os.pardir, os.pardir, '_ies_model', 'small_office', 'vista', 'small_office.aps')  # replace this with the path to any IES results (*.aps) file.
with iesve.ResultsReader.open(fp_in) as f:
   air_temperatures_dict = {
      room_id: f.get_room_results(room_id, 'Room air temperature', 'Air temperature', 'z')
      for room_id in f.get_room_ids()
      }
air_temperatures_dict = {k:v for k,v in air_temperatures_dict.items() if not v is None}  # removes any dictionary items if the value is None
print(list(air_temperatures_dict))
print(air_temperatures_dict['RF000000'])
    
    
    




db = iesve.VECdbDatabase.get_current_database()
print(db.get_projects())
project = db.get_projects()[iesve.project_types.project][0]
print(project.title)
print(project.get_construction_ids(iesve.construction_class.none))
construction = project.get_construction('ALUMP', iesve.construction_class.none)
print(construction.get_layers())
layer = construction.get_layers()[0]
print(layer.get_material(True))
quit()










