#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 29, 2020 09:44:48 PM +0200  platform: Windows NT

import sys
import pymongo
sys.path.append('..')

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

import Teachermainmenu_support
import webbrowser
import HealthPageTeacher
import GamesForTeacher
import classesTeacher
import classesattendance
import ScheForOneTeacher
import TransWorkClock

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = teacherpage (root)
    Teachermainmenu_support.init(root, top)
    root.mainloop()

w = None
def create_teacherpage(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_teacherpage(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = teacherpage (w)
    Teachermainmenu_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_teacherpage():
    global w
    w.destroy()
    w = None

class teacherpage:
    def OpenWork(self):
        TransWorkClock.vp_start_gui()
    def OpenGames(self):
        root.destroy()
        GamesForTeacher.vp_start_gui()
    def openHealth(self):
        root.destroy()
        HealthPageTeacher.vp_start_gui()
    def openforum(self):
        webbrowser.open("https://talsh16.wixsite.com/ezschool")

    def openzoom(self):
        root.destroy()
        classesTeacher.vp_start_gui()

    def openattendance(self):
        root.destroy()
        classesattendance.vp_start_gui()

    def openSchedule(self):
        root.destroy()
        ScheForOneTeacher.vp_start_gui()



    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1920x1051+-9+-9")
        top.minsize(148, 1)
        top.maxsize(1550, 900)
        top.resizable(1,  1)
        top.title("תפריט ראשי מורה")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.teach_sched = tk.Button(top)
        self.teach_sched.place(relx=0.219, rely=0.171, height=93, width=186)
        self.teach_sched.configure(activebackground="#ececec")
        self.teach_sched.configure(activeforeground="#000000")
        self.teach_sched.configure(background="#d9d9d9")
        self.teach_sched.configure(disabledforeground="#a3a3a3")
        self.teach_sched.configure(foreground="#000000")
        self.teach_sched.configure(highlightbackground="#d9d9d9")
        self.teach_sched.configure(highlightcolor="black")
        self.teach_sched.configure(pady="0")
        self.teach_sched.configure(text='''מערכת שעות''')
        self.teach_sched.configure(command=self.openSchedule)


        self.zoom = tk.Button(top)
        self.zoom.place(relx=0.344, rely=0.17, height=93, width=186)
        self.zoom.configure(activebackground="#ececec")
        self.zoom.configure(activeforeground="#000000")
        self.zoom.configure(background="#d9d9d9")
        self.zoom.configure(disabledforeground="#a3a3a3")
        self.zoom.configure(foreground="#000000")
        self.zoom.configure(highlightbackground="#d9d9d9")
        self.zoom.configure(highlightcolor="black")
        self.zoom.configure(pady="0")
        self.zoom.configure(text='''ZOOM''')
        self.zoom.configure(command=self.openzoom)

        self.teach_health = tk.Button(top)
        self.teach_health.place(relx=0.474, rely=0.171, height=93, width=186)
        self.teach_health.configure(activebackground="#ececec")
        self.teach_health.configure(activeforeground="#000000")
        self.teach_health.configure(background="#d9d9d9")
        self.teach_health.configure(disabledforeground="#a3a3a3")
        self.teach_health.configure(foreground="#000000")
        self.teach_health.configure(highlightbackground="#d9d9d9")
        self.teach_health.configure(highlightcolor="black")
        self.teach_health.configure(pady="0")
        self.teach_health.configure(text='''הצהרת בריאות''')
        self.teach_health.configure(command= self.openHealth)


        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.games_teach = tk.Button(top)
        self.games_teach.place(relx=0.609, rely=0.171, height=93, width=186)
        self.games_teach.configure(activebackground="#ececec")
        self.games_teach.configure(activeforeground="#000000")
        self.games_teach.configure(background="#d9d9d9")
        self.games_teach.configure(disabledforeground="#a3a3a3")
        self.games_teach.configure(foreground="#000000")
        self.games_teach.configure(highlightbackground="#d9d9d9")
        self.games_teach.configure(highlightcolor="black")
        self.games_teach.configure(pady="0")
        self.games_teach.configure(text='''העלאת משחקי חשיבה''')
        self.games_teach.configure(command=self.OpenGames)


        self.shop = tk.Button(top)
        self.shop.place(relx=0.219, rely=0.324, height=93, width=186)
        self.shop.configure(activebackground="#ececec")
        self.shop.configure(activeforeground="#000000")
        self.shop.configure(background="#d9d9d9")
        self.shop.configure(disabledforeground="#a3a3a3")
        self.shop.configure(foreground="#000000")
        self.shop.configure(highlightbackground="#d9d9d9")
        self.shop.configure(highlightcolor="black")
        self.shop.configure(pady="0")
        self.shop.configure(text='''הזמנת ציוד משרדי''')

        self.teach_work = tk.Button(top)
        self.teach_work.place(relx=0.344, rely=0.324, height=93, width=186)
        self.teach_work.configure(activebackground="#ececec")
        self.teach_work.configure(activeforeground="#000000")
        self.teach_work.configure(background="#d9d9d9")
        self.teach_work.configure(disabledforeground="#a3a3a3")
        self.teach_work.configure(foreground="#000000")
        self.teach_work.configure(highlightbackground="#d9d9d9")
        self.teach_work.configure(highlightcolor="black")
        self.teach_work.configure(pady="0")
        self.teach_work.configure(text='''שעון עבודה''')
        self.teach_work.configure(command=self.OpenWork)

        self.presents = tk.Button(top)
        self.presents.place(relx=0.474, rely=0.324, height=93, width=186)
        self.presents.configure(activebackground="#ececec")
        self.presents.configure(activeforeground="#000000")
        self.presents.configure(background="#d9d9d9")
        self.presents.configure(disabledforeground="#a3a3a3")
        self.presents.configure(foreground="#000000")
        self.presents.configure(highlightbackground="#d9d9d9")
        self.presents.configure(highlightcolor="black")
        self.presents.configure(pady="0")
        self.presents.configure(text='''נוכחות תלמידים''')
        self.presents.configure(command=self.openattendance)

        self.teach_forum = tk.Button(top)
        self.teach_forum.place(relx=0.609, rely=0.324, height=93, width=186)
        self.teach_forum.configure(activebackground="#ececec")
        self.teach_forum.configure(activeforeground="#000000")
        self.teach_forum.configure(background="#d9d9d9")
        self.teach_forum.configure(disabledforeground="#a3a3a3")
        self.teach_forum.configure(foreground="#000000")
        self.teach_forum.configure(highlightbackground="#d9d9d9")
        self.teach_forum.configure(highlightcolor="black")
        self.teach_forum.configure(pady="0")
        self.teach_forum.configure(text='''פורום''')
        self.teach_forum.configure(command=self.openforum)

        self.courses = tk.Button(top)
        self.courses.place(relx=0.745, rely=0.171, height=93, width=186)
        self.courses.configure(activebackground="#ececec")
        self.courses.configure(activeforeground="#000000")
        self.courses.configure(background="#d9d9d9")
        self.courses.configure(disabledforeground="#a3a3a3")
        self.courses.configure(foreground="#000000")
        self.courses.configure(highlightbackground="#d9d9d9")
        self.courses.configure(highlightcolor="black")
        self.courses.configure(pady="0")
        self.courses.configure(text='''מקצועות''')

if __name__ == '__main__':
    vp_start_gui()





