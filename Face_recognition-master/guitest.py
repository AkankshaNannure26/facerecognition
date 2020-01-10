# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:51:59 2019

@author: Akanksha Reddy
"""

import tkinter as tk
import os

def openCamera():
    os.startfile("pro.py")  
def openSheet():
    os.startfile("sheet.xlsx")
root = tk.Tk()
root.geometry("1540x785+0+0")


title = tk.Label(root,text="SMART ATTENDANCE THROUGH FACE RECOGNITION",bg="green")
title.config(font=("Courier",38))
title.pack()
camera = tk.Button(root,text="camera",command=openCamera,width=15,height=3).pack()

sheet = tk.Button(root,text="Excel-Sheet",command=openSheet,width=15,height=3).pack()
root.mainloop()


