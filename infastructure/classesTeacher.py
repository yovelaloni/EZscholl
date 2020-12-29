#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 26, 2020 02:08:18 PM +0200  platform: Windows NT

import sys

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

import classesTeacher_support
import Teachermainmenu
import zoomlinksTeacher
import zoomlinksTeacher2
import zoomlinksTeacher3
import zoomlinksTeacher4
import zoomlinksTeacher5
import zoomlinksTeacher6

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = classesTeacher (root)
    classesTeacher_support.init(root, top)
    root.mainloop()

w = None
def create_classesTeacher(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_classesTeacher(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = classesTeacher (w)
    classesTeacher_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_classesTeacher():
    global w
    w.destroy()
    w = None

class classesTeacher:
    def back(self):
        root.destroy()
        Teachermainmenu.vp_start_gui()
    def classnumber1(self):
        root.destroy()
        zoomlinksTeacher.vp_start_gui()

    def classnumber2(self):
            root.destroy()
            zoomlinksTeacher2.vp_start_gui()

    def classnumber3(self):
                root.destroy()
                zoomlinksTeacher3.vp_start_gui()
    def classnumber4(self):
        root.destroy()
        zoomlinksTeacher4.vp_start_gui()
    def classnumber5(self):
        root.destroy()
        zoomlinksTeacher5.vp_start_gui()
    def classnumber6(self):
        root.destroy()
        zoomlinksTeacher6.vp_start_gui()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x443+289+156")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("כיתות")
        top.configure(background="#fbffd9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.class1 = tk.Button(top)
        self.class1.place(relx=0.367, rely=0.133, height=44, width=137)
        self.class1.configure(activebackground="#ececec")
        self.class1.configure(activeforeground="#f9f2ff")
        self.class1.configure(background="#f1fa85")
        self.class1.configure(cursor="hand2")
        self.class1.configure(disabledforeground="#a3a3a3")
        self.class1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.class1.configure(foreground="#000000")
        self.class1.configure(highlightbackground="#d9d9d9")
        self.class1.configure(highlightcolor="black")
        self.class1.configure(pady="0")
        self.class1.configure(text='''כיתה א''')
        self.class1.configure(command= self.classnumber1)

        self.class2 = tk.Button(top)
        self.class2.place(relx=0.367, rely=0.266, height=44, width=137)
        self.class2.configure(activebackground="#ececec")
        self.class2.configure(activeforeground="#000000")
        self.class2.configure(background="#f1fa85")
        self.class2.configure(cursor="hand2")
        self.class2.configure(disabledforeground="#a3a3a3")
        self.class2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.class2.configure(foreground="#000000")
        self.class2.configure(highlightbackground="#d9d9d9")
        self.class2.configure(highlightcolor="black")
        self.class2.configure(pady="0")
        self.class2.configure(text='''כיתה ב''')
        self.class2.configure(command= self.classnumber2)

        self.class3 = tk.Button(top)
        self.class3.place(relx=0.367, rely=0.4, height=44, width=137)
        self.class3.configure(activebackground="#ececec")
        self.class3.configure(activeforeground="#000000")
        self.class3.configure(background="#f1fa85")
        self.class3.configure(cursor="hand2")
        self.class3.configure(disabledforeground="#a3a3a3")
        self.class3.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.class3.configure(foreground="#000000")
        self.class3.configure(highlightbackground="#d9d9d9")
        self.class3.configure(highlightcolor="black")
        self.class3.configure(pady="0")
        self.class3.configure(text='''כיתה ג''')
        self.class3.configure(command= self.classnumber3)

        self.class4 = tk.Button(top)
        self.class4.place(relx=0.367, rely=0.533, height=44, width=137)
        self.class4.configure(activebackground="#ececec")
        self.class4.configure(activeforeground="#000000")
        self.class4.configure(background="#f1fa85")
        self.class4.configure(cursor="hand2")
        self.class4.configure(disabledforeground="#a3a3a3")
        self.class4.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.class4.configure(foreground="#000000")
        self.class4.configure(highlightbackground="#d9d9d9")
        self.class4.configure(highlightcolor="black")
        self.class4.configure(pady="0")
        self.class4.configure(text='''כיתה ד''')
        self.class4.configure(command= self.classnumber4)

        self.class5 = tk.Button(top)
        self.class5.place(relx=0.367, rely=0.666, height=44, width=137)
        self.class5.configure(activebackground="#ececec")
        self.class5.configure(activeforeground="#000000")
        self.class5.configure(background="#f1fa85")
        self.class5.configure(cursor="hand2")
        self.class5.configure(disabledforeground="#a3a3a3")
        self.class5.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.class5.configure(foreground="#000000")
        self.class5.configure(highlightbackground="#d9d9d9")
        self.class5.configure(highlightcolor="black")
        self.class5.configure(pady="0")
        self.class5.configure(text='''כיתה ה''')
        self.class5.configure(command= self.classnumber5)


        self.class6 = tk.Button(top)
        self.class6.place(relx=0.367, rely=0.799, height=44, width=137)
        self.class6.configure(activebackground="#ececec")
        self.class6.configure(activeforeground="#000000")
        self.class6.configure(background="#f1fa85")
        self.class6.configure(cursor="hand2")
        self.class6.configure(disabledforeground="#a3a3a3")
        self.class6.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.class6.configure(foreground="#000000")
        self.class6.configure(highlightbackground="#d9d9d9")
        self.class6.configure(highlightcolor="black")
        self.class6.configure(pady="0")
        self.class6.configure(text='''כיתה ו''')
        self.class6.configure(command= self.classnumber6)


        self.mainmenu = tk.Button(top)
        self.mainmenu.place(relx=0.067, rely=0.867, height=44, width=117)
        self.mainmenu.configure(activebackground="#ececec")
        self.mainmenu.configure(activeforeground="#000000")
        self.mainmenu.configure(background="#f1fa85")
        self.mainmenu.configure(cursor="hand2")
        self.mainmenu.configure(disabledforeground="#a3a3a3")
        self.mainmenu.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.mainmenu.configure(foreground="#000000")
        self.mainmenu.configure(highlightbackground="#d9d9d9")
        self.mainmenu.configure(highlightcolor="black")
        self.mainmenu.configure(pady="0")
        self.mainmenu.configure(text='''תפריט ראשי''')
        self.mainmenu.configure(command= self.back)

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.467, rely=0.023, relheight=0.072
                , relwidth=0.517)
        self.Message1.configure(background="#fbffd9")
        self.Message1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''נא לבחור כיתה''')
        self.Message1.configure(width=310)

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





