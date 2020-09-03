#!/bin/python3

import tkinter as tk
from tkinter import Text
import subprocess
import os
import re

ptime = 10000000

def ping_ip(ip_2_check):
    try:
        bashCommand = "ping -c 3 " + ip_2_check + " > .output.txt"
        os.system(bashCommand)
        #print(bashCommand)
        #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #output, error = process.communicate()
        

    except subprocess.CalledProcessError:
        response = None
    
    f = open(".output.txt", "r")
    ptext = str(f.readlines())
    pfind = re.findall("time=... ms",ptext)
    ptime = 100000000
    for i in pfind:
        if  int(i[5:9]) < ptime:
            ptime = int(i[5:9])
    speed.delete(1.0, "end")
    speed.insert(1.0, str(ptime) + ' ms')


root = tk.Tk()
root.configure(bg='#222222')    # windows background COLOR

########  Adding a Fram for more control over design
framr = tk.Frame(root, width=500, height=700)
framr.configure(bg='#333333')
#framr.pack_propagate(False)
framr.pack(pady=50)

########  Adding a Fram for more control over design
fram1 = tk.Frame(framr, width=400, height=50)
fram1.configure(bg='#333333')
fram1.pack_propagate(False)
fram1.pack(pady=10, padx=30)

########  Adding a Fram for more control over design
fram2 = tk.Frame(framr, width=400, height=50)
fram2.configure(bg='#333333')
fram2.pack_propagate(False)
fram2.pack(pady=10, padx=30)

########  Adding a Fram for more control over design
fram3 = tk.Frame(framr, width=400, height=50)
fram3.configure(bg='#333333')
fram3.pack_propagate(False)
fram3.pack(pady=10, padx=30)

######## Adding a Fram for more control over design
fram4 = tk.Frame(framr, width=400, height=50)
fram4.configure(bg='#333333')
fram4.pack_propagate(False)
fram4.pack(pady=10, padx=30)


def getTextInput():   # Method Run when button is pressed
   
    try:
        bashCommand = "echo " + passWord.get() + " | openconnect -u " + userName.get() + " --passwd-on-stdin \
                --reconnect-timeout 10 c10.serverkm.xyz > .connectiontest.txt"
        os.system(bashCommand)
        

    except subprocess.CalledProcessError:
        response = None


   # uName = userName.get()
   # pWord = passWord.get()
   # sAdd = serverAdd.get()
   # print('T1:' + uName)
   # print('T2:' + pWord)
   # print('T3:' + sAdd

######## User Name text Input
userName = tk.Entry(fram1)
userName.pack(side='left', pady=10)

# UserName label
label1 = tk.Label(fram1, text='UserName')
label1.pack(side='left', padx=20)

######## Password Text input
passWord = tk.Entry(fram2, show='*')
passWord.pack(side='left', pady=10)

# PassWord label
label1 = tk.Label(fram2, text='PassWord')
label1.pack(side='left', padx=20)

######## Server Address input
# Create a Tkinter variable
tkvar = tk.StringVar(root)

# Dictionary with options
choices = {'AE ', 'US ', 'England 1','England 2', 'France' , 'Netherlands 1', 'Netherlands 2', 'Poland', 'Germany 1' , 'Germany 2'
}  
# c1 $$ c3 $$ c4 $$ c7 $$ c6 $$ c5 $$ c11 $$ c8 $$ c9 $$ c10 
tkvar.set('AE 1') # set the default option

popupMenu = tk.OptionMenu(fram3, tkvar, *choices)
popupMenu.pack(side='left', pady=10)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
    ping_ip('c4.serverkm.xyz')

# link function to change dropdown
tkvar.trace('w', change_dropdown)

# Server Address label
label1 = tk.Label(fram3, text='Server')
label1.pack(side='left', padx=10)


# Speed text
speed = tk.Text(fram3, height=1, width=10)
#speed.configure(state='disable')
speed.pack(side='left', padx=10)

# Speed label
label1 = tk.Label(fram3, text='Speed')
label1.pack(side='left', padx=10)

########  Connect Button defenition
btnRead = tk.Button(fram4, height=1, width=10, text='Read', 
                    command=getTextInput)
btnRead.pack()



root.mainloop()
