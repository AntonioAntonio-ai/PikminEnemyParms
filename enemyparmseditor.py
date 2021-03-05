import os
from constants import *
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import ttk

_initing = True
parmfile = 'N/A'

# options
adv_mode = True # advance mode

# save data
# contains changed parameter data
unsaved = {}

'''
while _initing: # the initialization process
    try:
        # get the data folder in this folder
        parmfile = os.getcwd() + '\\data'
        # ask for the enemy folder in the data folder
        parmfile = parmfile + '\\' + input('Which enemy subfolder do you wish to access? ') + '\\enemyparm.txt'
        print(parmfile)
        # let the user know where they are going and ask if they wish to go there
        _initing = input('(y/n) Is this correct? ') != 'y'
    except:
        print('_initing Failure!\nCurrent directory = ' + parmfile)

parmfile = open(parmfile, mode='r+', encoding = 'iso-8859-15')
print(parmfile,'\n')

def change_parm(parmfile, parmtype, num): # as in change_parm('fp',8) for fp08
    for line in parmfile:
        if line[2] == parmtype[0]:
            pass
'''

# this is activated when the parm_list or enemy_select have something selected
def show_parm(event):
    # getting the name
    enemy_name = name_select.get()
    # only getting the first name
    cut = enemy_name.index(' ')
    enemy_name = enemy_name[:cut]
    # only the correct names
    if enemy_name in enemynames.keys():
        # saving previous unsaved data
        unsaved.update()
        
        # get an actual file from the enemy name
        parmfile = os.getcwd() + '\\data' + '\\' + enemy_name + '\\enemyparm.txt'
        parmfile = open(parmfile, mode='r+', encoding='iso-8859-15')

        # if in advanced mode, just shove the file in there
        if adv_mode:
            # now put them in the text box
            parm_txt.delete(0.0, END)
            for line in parmfile:
                parm_txt.insert(END, line)
            
    else:
        parm_txt.delete(0.0, END)
        parm_txt.insert(END, 'Select an enemy first')

def edit_parm_type(event):
    p_type = parm_type.get()
    
    parm_list.delete(0, END)

    if p_type == 'All Parms':
        p_type = sparms + fpparms
    elif p_type == 'sParms':
        p_type = sparms
    elif p_type == 'fpParms':
        p_type = fpparms

    # this ---- is here so that when you click on it, all parms are put in box
    parm_list.insert(0, '------------')
    for parm in p_type:
        parm_list.insert(END, parm)

# tkinter init
root = tk.Tk()
root.geometry('600x425')
root.title("Pikmin 2 Enemy Parameter Editor")
frame = tk.Frame(root)
frame.pack()

# get some nice names for enemy selection
names = list(enemynames.keys())
for i in range(0,len(list(enemynames.values()))):
    names[i] += ' [{}]'.format(list(enemynames.values())[i])

# enemy selection
name_select = ttk.Combobox(frame, values=names, width=35)
name_select.set("Choose an enemy")
name_select.pack(padx = 1, pady = 5)
name_select.bind('<<ComboboxSelected>>', show_parm)

# show parameter(s)
parm_txt = tksc.ScrolledText(frame, width=50)
parm_txt.pack(side=RIGHT)

parm_scroll = tk.Scrollbar(frame) 
parm_scroll.pack(side=RIGHT, fill=Y)

parm_type = ttk.Combobox(frame, values=['All Parms', 'sParms', 'fpParms', 'Specific fpParms'])
parm_type.pack()
parm_type.set('sParms')
parm_type.bind('<<ComboboxSelected>>', edit_parm_type)

parm_list = tk.Listbox(frame, yscrollcommand=parm_scroll.set, width=24)  
# s parameters will be the first selected parameters
parm_list.insert(0, '------------')
for sparm in sparms: 
    parm_list.insert(END, sparm)
parm_list.bind('<<ListboxSelect>>', show_parm)
    
parm_list.pack(side=RIGHT, fill=BOTH)    
parm_scroll.config(command=parm_list.yview) 

'''
newparmfile = ''
for line in parmfile:
    if len(line) > 3: # checking if the line is substantial
        if line[1] == '{' and line[2] != '_': # checking if the line is not a comment line
            if line[2] == 's': # checking if the line is a s parameter
                print(line[2:6] + line[9:18] + ' ' + sparms[int(line[3:6])])
            if line[2] == 'f': # checking if the line is a fp parameter
                print(line[2:6] + line[9:18] + ' ' + fpparms[int(line[4:6])])
            newparm = input('->')
            if newparm[0] == 'r' or newparm[0].isnum(): # replace mode, standard mode
                pass
                if newparm[0] == 'q': # quick insert mode, inserts the first nth digits
                    pass
                elif newparm[0] == 'd': # move to the next parameter
                    pass
                elif newparm[0] == 'a': # move to the last parameter
                    pass
                elif newparm[0] == 'q': # quit the parameter editing, saving
                    pass
                elif newparm[0] == 'n': # end the parameter editing, not saving
                    newparmfile = parmfile # return the new parm file to the original
                    break # and get out
                elif newparm[0] == 's': # move to the s parameter inputted
                    pass
                elif newparm[0] == 'f': # move to the fp parameter inputted
                    pass
            else:
                line = line[:10] + newparm
                print(line)
                #line += newparm
                #print(line)
                if line[4:6] == '38': # break before hitting the special parameters
                    break
    newparmfile += line
'''
root.mainloop()
