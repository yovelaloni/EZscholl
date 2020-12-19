#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Nov 29, 2020 09:43:22 PM +0200  platform: Windows NT

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

import Secretarymainmenu_support
import webbrowser
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = secretarypage (root)
    Secretarymainmenu_support.init(root, top)
    root.mainloop()

w = None
def create_secretarypage(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_secretarypage(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = secretarypage (w)
    Secretarymainmenu_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_secretarypage():
    global w
    w.destroy()
    w = None

class secretarypage:
    def openforum(self):
        webbrowser.open("https://talsh16.wixsite.com/ezschool")
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
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("Secretary main menu")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.student_schedule = tk.Button(top)
        self.student_schedule.place(relx=0.219, rely=0.171, height=93, width=186)

        self.student_schedule.configure(activebackground="#ececec")
        self.student_schedule.configure(activeforeground="#000000")
        self.student_schedule.configure(background="#d9d9d9")
        self.student_schedule.configure(disabledforeground="#a3a3a3")
        self.student_schedule.configure(foreground="#000000")
        self.student_schedule.configure(highlightbackground="#d9d9d9")
        self.student_schedule.configure(highlightcolor="black")
        self.student_schedule.configure(pady="0")
        self.student_schedule.configure(text='''עדכון מערכת שעות תלמיד''')

        self.teacher_schedule = tk.Button(top)
        self.teacher_schedule.place(relx=0.344, rely=0.17, height=93, width=186)
        self.teacher_schedule.configure(activebackground="#ececec")
        self.teacher_schedule.configure(activeforeground="#000000")
        self.teacher_schedule.configure(background="#d9d9d9")
        self.teacher_schedule.configure(disabledforeground="#a3a3a3")
        self.teacher_schedule.configure(foreground="#000000")
        self.teacher_schedule.configure(highlightbackground="#d9d9d9")
        self.teacher_schedule.configure(highlightcolor="black")
        self.teacher_schedule.configure(pady="0")
        self.teacher_schedule.configure(text='''עדכון מערכת שעות מורה''')

        self.health = tk.Button(top)
        self.health.place(relx=0.474, rely=0.171, height=93, width=186)
        self.health.configure(activebackground="#ececec")
        self.health.configure(activeforeground="#000000")
        self.health.configure(background="#d9d9d9")
        self.health.configure(disabledforeground="#a3a3a3")
        self.health.configure(foreground="#000000")
        self.health.configure(highlightbackground="#d9d9d9")
        self.health.configure(highlightcolor="black")
        self.health.configure(pady="0")
        self.health.configure(text='''הצהרת בריאות''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.meetings = tk.Button(top)
        self.meetings.place(relx=0.609, rely=0.171, height=93, width=186)
        self.meetings.configure(activebackground="#ececec")
        self.meetings.configure(activeforeground="#000000")
        self.meetings.configure(background="#d9d9d9")
        self.meetings.configure(disabledforeground="#a3a3a3")
        self.meetings.configure(foreground="#000000")
        self.meetings.configure(highlightbackground="#d9d9d9")
        self.meetings.configure(highlightcolor="black")
        self.meetings.configure(pady="0")
        self.meetings.configure(text='''יומן פגישות''')

        self.work_clock = tk.Button(top)
        self.work_clock.place(relx=0.74, rely=0.171, height=93, width=186)
        self.work_clock.configure(activebackground="#ececec")
        self.work_clock.configure(activeforeground="#000000")
        self.work_clock.configure(background="#d9d9d9")
        self.work_clock.configure(disabledforeground="#a3a3a3")
        self.work_clock.configure(foreground="#000000")
        self.work_clock.configure(highlightbackground="#d9d9d9")
        self.work_clock.configure(highlightcolor="black")
        self.work_clock.configure(pady="0")
        self.work_clock.configure(text='''שעון עבודה''')

        self.inventory_payment = tk.Button(top)
        self.inventory_payment.place(relx=0.219, rely=0.324, height=93
                , width=186)
        self.inventory_payment.configure(activebackground="#ececec")
        self.inventory_payment.configure(activeforeground="#000000")
        self.inventory_payment.configure(background="#d9d9d9")
        self.inventory_payment.configure(disabledforeground="#a3a3a3")
        self.inventory_payment.configure(foreground="#000000")
        self.inventory_payment.configure(highlightbackground="#d9d9d9")
        self.inventory_payment.configure(highlightcolor="black")
        self.inventory_payment.configure(pady="0")
        self.inventory_payment.configure(text='''גביית תשלום - ציוד''')

        self.tuition_fee = tk.Button(top)
        self.tuition_fee.place(relx=0.344, rely=0.324, height=93, width=186)
        self.tuition_fee.configure(activebackground="#ececec")
        self.tuition_fee.configure(activeforeground="#000000")
        self.tuition_fee.configure(background="#d9d9d9")
        self.tuition_fee.configure(disabledforeground="#a3a3a3")
        self.tuition_fee.configure(foreground="#000000")
        self.tuition_fee.configure(highlightbackground="#d9d9d9")
        self.tuition_fee.configure(highlightcolor="black")
        self.tuition_fee.configure(pady="0")
        self.tuition_fee.configure(text='''גביית תשלום - שכר לימוד''')

        self.teachers_survey = tk.Button(top)
        self.teachers_survey.place(relx=0.474, rely=0.324, height=93, width=186)
        self.teachers_survey.configure(activebackground="#ececec")
        self.teachers_survey.configure(activeforeground="#000000")
        self.teachers_survey.configure(background="#d9d9d9")
        self.teachers_survey.configure(disabledforeground="#a3a3a3")
        self.teachers_survey.configure(foreground="#000000")
        self.teachers_survey.configure(highlightbackground="#d9d9d9")
        self.teachers_survey.configure(highlightcolor="black")
        self.teachers_survey.configure(pady="0")
        self.teachers_survey.configure(text='''סקר מורים''')

        self.forum = tk.Button(top)
        self.forum.place(relx=0.609, rely=0.324, height=93, width=186)
        self.forum.configure(activebackground="#ececec")
        self.forum.configure(activeforeground="#000000")
        self.forum.configure(background="#d9d9d9")
        self.forum.configure(disabledforeground="#a3a3a3")
        self.forum.configure(foreground="#000000")
        self.forum.configure(highlightbackground="#d9d9d9")
        self.forum.configure(highlightcolor="black")
        self.forum.configure(pady="0")
        self.forum.configure(text='''פורום''')
        self.forum.configure(command=self.openforum)

        self.inventory_manage = tk.Button(top)
        self.inventory_manage.place(relx=0.74, rely=0.324, height=93, width=186)
        self.inventory_manage.configure(activebackground="#ececec")
        self.inventory_manage.configure(activeforeground="#000000")
        self.inventory_manage.configure(background="#d9d9d9")
        self.inventory_manage.configure(disabledforeground="#a3a3a3")
        self.inventory_manage.configure(foreground="#000000")
        self.inventory_manage.configure(highlightbackground="#d9d9d9")
        self.inventory_manage.configure(highlightcolor="black")
        self.inventory_manage.configure(pady="0")
        self.inventory_manage.configure(text='''ניהול מלאי ציוד משרדי''')

if __name__ == '__main__':
    vp_start_gui()





