#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 24, 2020 09:23:05 PM +0200  platform: Windows NT

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

import zoomlinksTeacher_support
import webbrowser
import classesTeacher
from tkinter import messagebox

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = zoom_links_teacher (root)
    zoomlinksTeacher_support.init(root, top)
    root.mainloop()

w = None
def create_zoom_links_teacher(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_zoom_links_teacher(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = zoom_links_teacher (w)
    zoomlinksTeacher_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_zoom_links_teacher():
    global w
    w.destroy()
    w = None

class zoom_links_teacher:
    def openBible(self):
        webbrowser.open("https://sce-ac-il.zoom.us/j/84840441076")

    def openHistory(self):
        webbrowser.open("https://sce-ac-il.zoom.us/j/84840441076")

    def openMath(self):
        webbrowser.open("https://sce-ac-il.zoom.us/j/84840441076")

    def openHebrew(self):
        webbrowser.open("https://sce-ac-il.zoom.us/j/84840441076")

    def back(self):
        root.destroy()
        classesTeacher.vp_start_gui()

    def newBible(self):
        txt=self.zoom_link_bible.get()
        if not txt:
            tk.messagebox.showwarning('zoomlinks', 'הקישור לא נקלט')
        else:
            f=open("newBible1.txt","w")
            f.write(txt)
            f.close()
            tk.messagebox.showinfo('zoomlinks', 'הקישור נקלט בהצלחה')

    def newHebrew(self):
        txt=self.zoom_link_hebrew.get()
        if not txt:
            tk.messagebox.showwarning('zoomlinks', 'הקישור לא נקלט')
        else:
            f=open("newHebrew1.txt","w")
            f.write(txt)
            f.close()
            tk.messagebox.showinfo('zoomlinks', 'הקישור נקלט בהצלחה')
    def newMath(self):
        txt=self.zoom_link_math.get()
        if not txt:
            tk.messagebox.showwarning('zoomlinks', 'הקישור לא נקלט')
        else:
            f=open("newMath1.txt","w")
            f.write(txt)
            f.close()
            tk.messagebox.showinfo('zoomlinks', 'הקישור נקלט בהצלחה')

    def newHistory(self):
        txt=self.zoom_link_history.get()
        txt = self.zoom_link_math.get()
        if not txt:
            tk.messagebox.showwarning('zoomlinks', 'הקישור לא נקלט')
        else:
            f = open("newHistory1.txt", "w")
            f.write(txt)
            f.close()
            tk.messagebox.showinfo('zoomlinks', 'הקישור נקלט בהצלחה')


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("קישורי זום למורה-כיתה א")
        top.configure(background="#ccfaff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.zoom_math = tk.Button(top)
        self.zoom_math.place(relx=0.617, rely=0.111, height=53, width=156)
        self.zoom_math.configure(activebackground="#ececec")
        self.zoom_math.configure(activeforeground="#000000")
        self.zoom_math.configure(background="#28eaff")
        self.zoom_math.configure(cursor="hand2")
        self.zoom_math.configure(disabledforeground="#a3a3a3")
        self.zoom_math.configure(foreground="#000000")
        self.zoom_math.configure(highlightbackground="#d9d9d9")
        self.zoom_math.configure(highlightcolor="black")
        self.zoom_math.configure(pady="0")
        self.zoom_math.configure(text='''קישור לשיעור מתמטיקה''')
        self.zoom_math.configure(command= self.openMath)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.zoom_history = tk.Button(top)
        self.zoom_history.place(relx=0.617, rely=0.267, height=53, width=156)
        self.zoom_history.configure(activebackground="#ececec")
        self.zoom_history.configure(activeforeground="#000000")
        self.zoom_history.configure(background="#28eaff")
        self.zoom_history.configure(cursor="hand2")
        self.zoom_history.configure(disabledforeground="#a3a3a3")
        self.zoom_history.configure(foreground="#000000")
        self.zoom_history.configure(highlightbackground="#d9d9d9")
        self.zoom_history.configure(highlightcolor="black")
        self.zoom_history.configure(pady="0")
        self.zoom_history.configure(text='''קישור לשיעור היסטוריה''')
        self.zoom_history.configure(command= self.openHistory)

        self.zoom_bible = tk.Button(top)
        self.zoom_bible.place(relx=0.617, rely=0.444, height=53, width=156)
        self.zoom_bible.configure(activebackground="#ececec")
        self.zoom_bible.configure(activeforeground="#000000")
        self.zoom_bible.configure(background="#28eaff")
        self.zoom_bible.configure(cursor="hand2")
        self.zoom_bible.configure(disabledforeground="#a3a3a3")
        self.zoom_bible.configure(foreground="#000000")
        self.zoom_bible.configure(highlightbackground="#d9d9d9")
        self.zoom_bible.configure(highlightcolor="black")
        self.zoom_bible.configure(pady="0")
        self.zoom_bible.configure(text='''קישור לשיעור תנך''')
        self.zoom_bible.configure(command=self.openBible)


        self.zoom_hebrew = tk.Button(top)
        self.zoom_hebrew.place(relx=0.617, rely=0.622, height=53, width=156)
        self.zoom_hebrew.configure(activebackground="#ececec")
        self.zoom_hebrew.configure(activeforeground="#000000")
        self.zoom_hebrew.configure(background="#28eaff")
        self.zoom_hebrew.configure(cursor="hand2")
        self.zoom_hebrew.configure(disabledforeground="#a3a3a3")
        self.zoom_hebrew.configure(foreground="#000000")
        self.zoom_hebrew.configure(highlightbackground="#d9d9d9")
        self.zoom_hebrew.configure(highlightcolor="black")
        self.zoom_hebrew.configure(pady="0")
        self.zoom_hebrew.configure(text='''קישור לשיעור עברית''')
        self.zoom_hebrew.configure(command=self.openHebrew)

        self.zoom_link_math = tk.Entry(top)
        self.zoom_link_math.place(relx=0.05, rely=0.111, height=34
                , relwidth=0.523)
        self.zoom_link_math.configure(background="white")
        self.zoom_link_math.configure(cursor="fleur")
        self.zoom_link_math.configure(disabledforeground="#a3a3a3")
        self.zoom_link_math.configure(font="TkFixedFont")
        self.zoom_link_math.configure(foreground="#000000")
        self.zoom_link_math.configure(highlightbackground="#d9d9d9")
        self.zoom_link_math.configure(highlightcolor="black")
        self.zoom_link_math.configure(insertbackground="black")
        self.zoom_link_math.configure(selectbackground="blue")
        self.zoom_link_math.configure(selectforeground="white")

        self.zoom_label = tk.Label(top)
        self.zoom_label.place(relx=0.25, rely=0.022, height=26, width=172)
        self.zoom_label.configure(activebackground="#f9f9f9")
        self.zoom_label.configure(activeforeground="black")
        self.zoom_label.configure(background="#ccfaff")
        self.zoom_label.configure(disabledforeground="#a3a3a3")
        self.zoom_label.configure(font="-family {Segoe UI} -size 10 -weight bold -underline 1")
        self.zoom_label.configure(foreground="#000000")
        self.zoom_label.configure(highlightbackground="#d9d9d9")
        self.zoom_label.configure(highlightcolor="black")
        self.zoom_label.configure(text='''הוספת קישור ידנית''')

        self.entry_math = tk.Button(top)
        self.entry_math.place(relx=0.4, rely=0.2, height=23, width=96)
        self.entry_math.configure(activebackground="#ececec")
        self.entry_math.configure(activeforeground="#000000")
        self.entry_math.configure(background="#28eaff")
        self.entry_math.configure(cursor="fleur")
        self.entry_math.configure(disabledforeground="#a3a3a3")
        self.entry_math.configure(foreground="#000000")
        self.entry_math.configure(highlightbackground="#d9d9d9")
        self.entry_math.configure(highlightcolor="black")
        self.entry_math.configure(pady="0")
        self.entry_math.configure(text='''הוספה''')
        self.entry_math.configure(command=self.newMath)

        self.zoom_link_history = tk.Entry(top)
        self.zoom_link_history.place(relx=0.05, rely=0.267, height=30
                , relwidth=0.523)
        self.zoom_link_history.configure(background="white")
        self.zoom_link_history.configure(cursor="fleur")
        self.zoom_link_history.configure(disabledforeground="#a3a3a3")
        self.zoom_link_history.configure(font="TkFixedFont")
        self.zoom_link_history.configure(foreground="#000000")
        self.zoom_link_history.configure(insertbackground="black")

        self.zoom_link_bible = tk.Entry(top)
        self.zoom_link_bible.place(relx=0.05, rely=0.444, height=30
                , relwidth=0.523)
        self.zoom_link_bible.configure(background="white")
        self.zoom_link_bible.configure(disabledforeground="#a3a3a3")
        self.zoom_link_bible.configure(font="TkFixedFont")
        self.zoom_link_bible.configure(foreground="#000000")
        self.zoom_link_bible.configure(insertbackground="black")

        self.zoom_link_hebrew = tk.Entry(top)
        self.zoom_link_hebrew.place(relx=0.05, rely=0.644, height=30
                , relwidth=0.523)
        self.zoom_link_hebrew.configure(background="white")
        self.zoom_link_hebrew.configure(cursor="fleur")
        self.zoom_link_hebrew.configure(disabledforeground="#a3a3a3")
        self.zoom_link_hebrew.configure(font="TkFixedFont")
        self.zoom_link_hebrew.configure(foreground="#000000")
        self.zoom_link_hebrew.configure(insertbackground="black")

        self.Entry_bible = tk.Button(top)
        self.Entry_bible.place(relx=0.383, rely=0.533, height=24, width=107)
        self.Entry_bible.configure(activebackground="#ececec")
        self.Entry_bible.configure(activeforeground="#000000")
        self.Entry_bible.configure(background="#28eaff")
        self.Entry_bible.configure(disabledforeground="#a3a3a3")
        self.Entry_bible.configure(foreground="#000000")
        self.Entry_bible.configure(highlightbackground="#d9d9d9")
        self.Entry_bible.configure(highlightcolor="black")
        self.Entry_bible.configure(pady="0")
        self.Entry_bible.configure(text='''הוספה''')
        self.Entry_bible.configure(command=self.newBible)

        self.Entry_history = tk.Button(top)
        self.Entry_history.place(relx=0.383, rely=0.356, height=24, width=107)
        self.Entry_history.configure(activebackground="#ececec")
        self.Entry_history.configure(activeforeground="#000000")
        self.Entry_history.configure(background="#28eaff")
        self.Entry_history.configure(disabledforeground="#a3a3a3")
        self.Entry_history.configure(foreground="#000000")
        self.Entry_history.configure(highlightbackground="#d9d9d9")
        self.Entry_history.configure(highlightcolor="black")
        self.Entry_history.configure(pady="0")
        self.Entry_history.configure(text='''הוספה''')
        self.Entry_history.configure(command=self.newHistory)


        self.Entry_hebrew = tk.Button(top)
        self.Entry_hebrew.place(relx=0.383, rely=0.733, height=24, width=107)
        self.Entry_hebrew.configure(activebackground="#ececec")
        self.Entry_hebrew.configure(activeforeground="#000000")
        self.Entry_hebrew.configure(background="#28eaff")
        self.Entry_hebrew.configure(disabledforeground="#a3a3a3")
        self.Entry_hebrew.configure(foreground="#000000")
        self.Entry_hebrew.configure(highlightbackground="#d9d9d9")
        self.Entry_hebrew.configure(highlightcolor="black")
        self.Entry_hebrew.configure(pady="0")
        self.Entry_hebrew.configure(text='''הוספה''')
        self.Entry_hebrew.configure(command=self.newHebrew)

        self.menu = tk.Button(top)
        self.menu.place(relx=0.05, rely=0.867, height=44, width=167)
        self.menu.configure(activebackground="#ececec")
        self.menu.configure(activeforeground="#000000")
        self.menu.configure(background="#28eaff")
        self.menu.configure(disabledforeground="#a3a3a3")
        self.menu.configure(foreground="#000000")
        self.menu.configure(highlightbackground="#d9d9d9")
        self.menu.configure(highlightcolor="black")
        self.menu.configure(pady="0")
        self.menu.configure(text='''חזרה לכיתות''')
        self.menu.configure(command= self.back)


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





