#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 29, 2020 09:44:10 PM +0200  platform: Windows NT


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

import Studentmainmenu_support
import webbrowser
import HealthPage
import classes
import Seker1
global userobj
import TuitionStudent
import classesSche
import GamesForStudent


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = studentpage(root)
    Studentmainmenu_support.init(root,top)
    root.mainloop()



w = None
def create_studentpage(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_studentpage(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = studentpage (w)
    Studentmainmenu_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_studentpage():
    global w
    w.destroy()
    w = None

class studentpage:
    def open_classes(self):
        root.destroy()
        classesSche.vp_start_gui()

    def open_classes(self):
        root.destroy()
        classesSche.vp_start_gui()

    def openGames(self):
        root.destroy()
        GamesForStudent.vp_start_gui()
    def opensurvey(self):
        f = open("isSekerOpen.txt")
        flag=f.read()
        f.close()
        if flag == "0":
            tk.messagebox.showwarning('Seker', 'הסקר אינו זמין כרגע')
        else:
             root.destroy()
             Seker1.vp_start_gui()

    def paymentTuition(self):
        root.destroy()
        TuitionStudent.vp_start_gui()

    def opensurvey(self):
        root.destroy()
        Seker.vp_start_gui()

    def openforum(self):
        webbrowser.open("https://talsh16.wixsite.com/ezschool")
    def openHealth(self):
        root.destroy()
        HealthPage.vp_start_gui()
    def openzoom(self):
        root.destroy()
        classes.vp_start_gui()

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
        top.title("Student main menu")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.stud_sched = tk.Button(top)
        self.stud_sched.place(relx=0.219, rely=0.171, height=93, width=186)
        self.stud_sched.configure(activebackground="#ececec")
        self.stud_sched.configure(activeforeground="#000000")
        self.stud_sched.configure(background="#d9d9d9")
        self.stud_sched.configure(disabledforeground="#a3a3a3")
        self.stud_sched.configure(foreground="#000000")
        self.stud_sched.configure(highlightbackground="#d9d9d9")
        self.stud_sched.configure(highlightcolor="black")
        self.stud_sched.configure(pady="0")
        self.stud_sched.configure(text='''מערכת שעות''')
        self.stud_sched.configure(command=self.open_classes)

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

        self.stud_health = tk.Button(top)
        self.stud_health.place(relx=0.474, rely=0.171, height=93, width=186)
        self.stud_health.configure(activebackground="#ececec")
        self.stud_health.configure(activeforeground="#000000")
        self.stud_health.configure(background="#d9d9d9")
        self.stud_health.configure(disabledforeground="#a3a3a3")
        self.stud_health.configure(foreground="#000000")
        self.stud_health.configure(highlightbackground="#d9d9d9")
        self.stud_health.configure(highlightcolor="black")
        self.stud_health.configure(pady="0")
        self.stud_health.configure(text='''הצהרת בריאות''')

        self.stud_health.configure(command= self.openHealth)


        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.meeting_sched = tk.Button(top)
        self.meeting_sched.place(relx=0.609, rely=0.171, height=93, width=186)
        self.meeting_sched.configure(activebackground="#ececec")
        self.meeting_sched.configure(activeforeground="#000000")
        self.meeting_sched.configure(background="#d9d9d9")
        self.meeting_sched.configure(disabledforeground="#a3a3a3")
        self.meeting_sched.configure(foreground="#000000")
        self.meeting_sched.configure(highlightbackground="#d9d9d9")
        self.meeting_sched.configure(highlightcolor="black")
        self.meeting_sched.configure(pady="0")
        self.meeting_sched.configure(text='''פגישת מזכירה''')
        self.meeting_sched.configure(wraplength="-1")

        self.games = tk.Button(top)
        self.games.place(relx=0.74, rely=0.171, height=93, width=186)
        self.games.configure(activebackground="#ececec")
        self.games.configure(activeforeground="#000000")
        self.games.configure(background="#d9d9d9")
        self.games.configure(disabledforeground="#a3a3a3")
        self.games.configure(foreground="#000000")
        self.games.configure(highlightbackground="#d9d9d9")
        self.games.configure(highlightcolor="black")
        self.games.configure(pady="0")
        self.games.configure(text='''משחקי חשיבה''')
        self.games.configure(command=self.openGames)

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

        self.payment_tuit = tk.Button(top)
        self.payment_tuit.place(relx=0.344, rely=0.324, height=93, width=186)
        self.payment_tuit.configure(activebackground="#ececec")
        self.payment_tuit.configure(activeforeground="#000000")
        self.payment_tuit.configure(background="#d9d9d9")
        self.payment_tuit.configure(disabledforeground="#a3a3a3")
        self.payment_tuit.configure(foreground="#000000")
        self.payment_tuit.configure(highlightbackground="#d9d9d9")
        self.payment_tuit.configure(highlightcolor="black")
        self.payment_tuit.configure(pady="0")
        self.payment_tuit.configure(text='''תשלום שכר לימוד''')
        self.payment_tuit.configure(command=self.paymentTuition)


        self.survey = tk.Button(top)
        self.survey.place(relx=0.474, rely=0.324, height=93, width=186)
        self.survey.configure(activebackground="#ececec")
        self.survey.configure(activeforeground="#000000")
        self.survey.configure(background="#d9d9d9")
        self.survey.configure(cursor="hand2")
        self.survey.configure(disabledforeground="#a3a3a3")
        self.survey.configure(foreground="#000000")
        self.survey.configure(highlightbackground="#d9d9d9")
        self.survey.configure(highlightcolor="black")
        self.survey.configure(pady="0")
        self.survey.configure(text='''סקר מורים''')
        self.survey.configure(command=self.opensurvey)

        self.stud_forum = tk.Button(top)
        self.stud_forum.place(relx=0.609, rely=0.324, height=93, width=186)
        self.stud_forum.configure(activebackground="#ececec")
        self.stud_forum.configure(activeforeground="#000000")
        self.stud_forum.configure(background="#d9d9d9")
        self.stud_forum.configure(disabledforeground="#a3a3a3")
        self.stud_forum.configure(foreground="#000000")
        self.stud_forum.configure(highlightbackground="#d9d9d9")
        self.stud_forum.configure(highlightcolor="black")
        self.stud_forum.configure(pady="0")
        self.stud_forum.configure(text='''פורום''')
        self.stud_forum.configure(command=self.openforum)

        self.courses = tk.Button(top)
        self.courses.place(relx=0.74, rely=0.324, height=93, width=186)
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





