#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 30, 2020 03:58:13 PM +0200  platform: Windows NT

import sys
import pymongo

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import TuitionSecretaryid_support
import Secretarymainmenu
import TuitionSecretarypayment
import classesReport

from tkinter import messagebox
sys.path.append('..')
from data import user_db_init, inventory_db_init
user_db_init()
inventory_db_init()
client = pymongo.MongoClient()
mydb = client['EZSchooldb']
userobj=None

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Tuitionsec (root)
    TuitionSecretaryid_support.init(root, top)
    root.mainloop()

w = None
def create_Tuitionsec(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Tuitionsec(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Tuitionsec (w)
    TuitionSecretaryid_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Tuitionsec():
    global w
    w.destroy()
    w = None

class Tuitionsec:
    def back(self):
        root.destroy()
        Secretarymainmenu.vp_start_gui()
    def nextPage(self):
        id=self.id_entry.get()
        global userobj
        global mydb
        userobj = mydb['Users'].find_one({'id': id})
        if userobj == None or userobj['Usertype']!=3:
            tk.messagebox.showwarning('Login Page', 'התלמיד לא נמצא')
        else:
            f = open("paymentForStudent.txt", "w")
            f.seek(0)
            f.truncate()
            f.write(userobj['id'])
            f.close()
            root.destroy()
            TuitionSecretarypayment.vp_start_gui()

    def Openreport(self):
        root.destroy()
        classesReport.vp_start_gui()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("תשלום שכר לימוד")
        top.configure(background="#ffcf9f")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.report = tk.Button(top)
        self.report.place(relx=0.35, rely=0.844, height=44, width=147)
        self.report.configure(activebackground="#ececec")
        self.report.configure(activeforeground="#000000")
        self.report.configure(background="#ffb871")
        self.report.configure(disabledforeground="#a3a3a3")
        self.report.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.report.configure(foreground="#000000")
        self.report.configure(highlightbackground="#d9d9d9")
        self.report.configure(highlightcolor="black")
        self.report.configure(pady="0")
        self.report.configure(text='''הנפקת דו"ח''')
        self.report.configure(command=self.Openreport)

        self.mainmenu = tk.Button(top)
        self.mainmenu.place(relx=0.05, rely=0.844, height=44, width=147)
        self.mainmenu.configure(activebackground="#ececec")
        self.mainmenu.configure(activeforeground="#000000")
        self.mainmenu.configure(background="#ffb871")
        self.mainmenu.configure(cursor="hand2")
        self.mainmenu.configure(disabledforeground="#a3a3a3")
        self.mainmenu.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.mainmenu.configure(foreground="#000000")
        self.mainmenu.configure(highlightbackground="#d9d9d9")
        self.mainmenu.configure(highlightcolor="black")
        self.mainmenu.configure(pady="0")
        self.mainmenu.configure(text='''תפריט ראשי''')
        self.mainmenu.configure(command=self.back)


        self.nextpage = tk.Button(top)
        self.nextpage.place(relx=0.383, rely=0.422, height=34, width=127)
        self.nextpage.configure(activebackground="#ececec")
        self.nextpage.configure(activeforeground="#000000")
        self.nextpage.configure(background="#ffb871")
        self.nextpage.configure(cursor="hand2")
        self.nextpage.configure(disabledforeground="#a3a3a3")
        self.nextpage.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.nextpage.configure(foreground="#000000")
        self.nextpage.configure(highlightbackground="#d9d9d9")
        self.nextpage.configure(highlightcolor="black")
        self.nextpage.configure(pady="0")
        self.nextpage.configure(text='''המשך''')
        self.nextpage.configure(command=self.nextPage)

        self.id_entry = tk.Entry(top)
        self.id_entry.place(relx=0.367, rely=0.311, height=30, relwidth=0.257)
        self.id_entry.configure(background="white")
        self.id_entry.configure(disabledforeground="#a3a3a3")
        self.id_entry.configure(font="TkFixedFont")
        self.id_entry.configure(foreground="#000000")
        self.id_entry.configure(highlightbackground="#d9d9d9")
        self.id_entry.configure(highlightcolor="black")
        self.id_entry.configure(insertbackground="black")
        self.id_entry.configure(selectbackground="blue")
        self.id_entry.configure(selectforeground="white")

        self.userDetails = tk.Message(top)
        self.userDetails.place(relx=0.133, rely=0.2, relheight=0.118
                , relwidth=0.767)
        self.userDetails.configure(background="#ffcf9f")
        self.userDetails.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.userDetails.configure(foreground="#000000")
        self.userDetails.configure(highlightbackground="#d9d9d9")
        self.userDetails.configure(highlightcolor="black")
        self.userDetails.configure(text='''הכנס מספר תעודת זהות של התלמיד עבורו מתבצע התשלום''')
        self.userDetails.configure(width=460)

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#ececec")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="#000000")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(foreground="#000000")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





