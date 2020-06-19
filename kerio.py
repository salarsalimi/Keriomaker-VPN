
import tkinter as tk
from tkinter import Text

root = tk.Tk()
root.configure(bg='#222222')    # windows background COLOR

# Adding a Fram for more control over design
framr = tk.Frame(root, width=500, height=700)
framr.configure(bg='#333333')
#framr.pack_propagate(False)
framr.pack(pady=50)

# Adding a Fram for more control over design
fram1 = tk.Frame(framr, width=400, height=50)
fram1.configure(bg='#333333')
fram1.pack_propagate(False)
fram1.pack(pady=10, padx=30)

# Adding a Fram for more control over design
fram2 = tk.Frame(framr, width=400, height=50)
fram2.configure(bg='#333333')
fram2.pack_propagate(False)
fram2.pack(pady=10, padx=30)

# Adding a Fram for more control over design
fram3 = tk.Frame(framr, width=400, height=50)
fram3.configure(bg='#333333')
fram3.pack_propagate(False)
fram3.pack(pady=10, padx=30)

# Adding a Fram for more control over design
fram4 = tk.Frame(framr, width=400, height=50)
fram4.configure(bg='#333333')
fram4.pack_propagate(False)
fram4.pack(pady=10, padx=30)


def getTextInput():   # Method Run when button is pressed
    uName = userName.get()
    pWord = passWord.get()
    sAdd = serverAdd.get()
    print('T1:' + uName)
    print('T2:' + pWord)
    print('T3:' + sAdd)

# User Name text Input
userName = tk.Entry(fram1)
userName.pack(side='left', pady=10)

# UserName label
label1 = tk.Label(fram1, text='UserName')
label1.pack(side='left', padx=20)

# Password Text input
passWord = tk.Entry(fram2, show='*')
passWord.pack(side='left', pady=10)

# PassWord label
label1 = tk.Label(fram2, text='PassWord')
label1.pack(side='left', padx=20)

# Server Address input
serverAdd = tk.Entry(fram3)
serverAdd.pack(side='left', pady=10)

# Server Address label
label1 = tk.Label(fram3, text='Server Address')
label1.pack(side='left', padx=20)

# Connect Button defenition
btnRead = tk.Button(fram4, height=1, width=10, text='Read', 
                    command=getTextInput)
btnRead.pack()



root.mainloop()