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


dir_vista = os.path.join(currentproject.path, 'vista')

print(dir_vista)

quit()



print('--- How to ask the user to choose a IES-VE result file ---')
import iesve
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import os
currentproject = iesve.VEProject.get_current_project()
dir_currentproject = currentproject.path.replace('\\','/')
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
print('fp_in: ', fp_in)



