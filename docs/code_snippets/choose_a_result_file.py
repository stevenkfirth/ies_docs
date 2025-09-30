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



