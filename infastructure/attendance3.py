#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Dec 31, 2020 04:30:03 PM +0200  platform: Windows NT

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

import attendance3_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    attendance3_support.set_Tk_var()
    top = Toplevel1 (root)
    attendance3_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    attendance3_support.set_Tk_var()
    top = Toplevel1 (w)
    attendance3_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
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
        top.title("נוכחות כיתה ג")
        top.configure(background="#fef1b4")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.submit = tk.Button(top)
        self.submit.place(relx=0.385, rely=0.879, height=93, width=456)
        self.submit.configure(activebackground="#ececec")
        self.submit.configure(activeforeground="#000000")
        self.submit.configure(background="#f5cb03")
        self.submit.configure(cursor="hand2")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.submit.configure(foreground="#000000")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="black")
        self.submit.configure(pady="0")
        self.submit.configure(text='''הגשת נוכחות''')

        self.stud1 = tk.Checkbutton(top)
        self.stud1.place(relx=0.385, rely=0.13, relheight=0.061, relwidth=0.181)
        self.stud1.configure(activebackground="#ececec")
        self.stud1.configure(activeforeground="#000000")
        self.stud1.configure(background="#fef1b4")
        self.stud1.configure(disabledforeground="#a3a3a3")
        self.stud1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud1.configure(foreground="#000000")
        self.stud1.configure(highlightbackground="#d9d9d9")
        self.stud1.configure(highlightcolor="black")
        self.stud1.configure(justify='left')
        self.stud1.configure(text='''ישראל אביחיל 302144070''')
        self.stud1.configure(variable=attendance3_support.che47)

        self.stud2 = tk.Checkbutton(top)
        self.stud2.place(relx=0.38, rely=0.181, relheight=0.061, relwidth=0.169)
        self.stud2.configure(activebackground="#ececec")
        self.stud2.configure(activeforeground="#000000")
        self.stud2.configure(background="#fef1b4")
        self.stud2.configure(disabledforeground="#a3a3a3")
        self.stud2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud2.configure(foreground="#000000")
        self.stud2.configure(highlightbackground="#d9d9d9")
        self.stud2.configure(highlightcolor="black")
        self.stud2.configure(justify='left')
        self.stud2.configure(text='''טלי תבלין 123090942''')
        self.stud2.configure(variable=attendance3_support.che49)

        self.stud3 = tk.Checkbutton(top)
        self.stud3.place(relx=0.37, rely=0.238, relheight=0.061, relwidth=0.201)
        self.stud3.configure(activebackground="#ececec")
        self.stud3.configure(activeforeground="#000000")
        self.stud3.configure(background="#fef1b4")
        self.stud3.configure(disabledforeground="#a3a3a3")
        self.stud3.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud3.configure(foreground="#000000")
        self.stud3.configure(highlightbackground="#d9d9d9")
        self.stud3.configure(highlightcolor="black")
        self.stud3.configure(justify='left')
        self.stud3.configure(text='''הדס חסידים 012345678''')
        self.stud3.configure(variable=attendance3_support.che50)

        self.stud4 = tk.Checkbutton(top)
        self.stud4.place(relx=0.358, rely=0.3, relheight=0.061, relwidth=0.213)
        self.stud4.configure(activebackground="#ececec")
        self.stud4.configure(activeforeground="#000000")
        self.stud4.configure(background="#fef1b4")
        self.stud4.configure(disabledforeground="#a3a3a3")
        self.stud4.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud4.configure(foreground="#000000")
        self.stud4.configure(highlightbackground="#d9d9d9")
        self.stud4.configure(highlightcolor="black")
        self.stud4.configure(justify='left')
        self.stud4.configure(text='''מאי חג'בי 204857673''')
        self.stud4.configure(variable=attendance3_support.che51)

        self.stud5 = tk.Checkbutton(top)
        self.stud5.place(relx=0.354, rely=0.362, relheight=0.051, relwidth=0.218)

        self.stud5.configure(activebackground="#ececec")
        self.stud5.configure(activeforeground="#000000")
        self.stud5.configure(background="#fef1b4")
        self.stud5.configure(disabledforeground="#a3a3a3")
        self.stud5.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud5.configure(foreground="#000000")
        self.stud5.configure(highlightbackground="#d9d9d9")
        self.stud5.configure(highlightcolor="black")
        self.stud5.configure(justify='left')
        self.stud5.configure(text='''שי סרוסי 012234567''')
        self.stud5.configure(variable=attendance3_support.che52)

        self.stud6 = tk.Checkbutton(top)
        self.stud6.place(relx=0.37, rely=0.41, relheight=0.061, relwidth=0.202)
        self.stud6.configure(activebackground="#ececec")
        self.stud6.configure(activeforeground="#000000")
        self.stud6.configure(background="#fef1b4")
        self.stud6.configure(disabledforeground="#a3a3a3")
        self.stud6.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud6.configure(foreground="#000000")
        self.stud6.configure(highlightbackground="#d9d9d9")
        self.stud6.configure(highlightcolor="black")
        self.stud6.configure(justify='left')
        self.stud6.configure(text='''אירינה לרמן 001122334''')
        self.stud6.configure(variable=attendance3_support.che53)

        self.stud7 = tk.Checkbutton(top)
        self.stud7.place(relx=0.37, rely=0.47, relheight=0.052, relwidth=0.201)
        self.stud7.configure(activebackground="#ececec")
        self.stud7.configure(activeforeground="#000000")
        self.stud7.configure(background="#fef1b4")
        self.stud7.configure(disabledforeground="#a3a3a3")
        self.stud7.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud7.configure(foreground="#000000")
        self.stud7.configure(highlightbackground="#d9d9d9")
        self.stud7.configure(highlightcolor="black")
        self.stud7.configure(justify='left')
        self.stud7.configure(text='''נמרוד קריגר 098098098''')
        self.stud7.configure(variable=attendance3_support.che54)

        self.stud8 = tk.Checkbutton(top)
        self.stud8.place(relx=0.365, rely=0.514, relheight=0.062, relwidth=0.206)

        self.stud8.configure(activebackground="#ececec")
        self.stud8.configure(activeforeground="#000000")
        self.stud8.configure(background="#fef1b4")
        self.stud8.configure(disabledforeground="#a3a3a3")
        self.stud8.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud8.configure(foreground="#000000")
        self.stud8.configure(highlightbackground="#d9d9d9")
        self.stud8.configure(highlightcolor="black")
        self.stud8.configure(justify='left')
        self.stud8.configure(text='''נפתלי פרץ 204444099''')
        self.stud8.configure(variable=attendance3_support.che55)

        self.stud9 = tk.Checkbutton(top)
        self.stud9.place(relx=0.375, rely=0.571, relheight=0.051, relwidth=0.196)

        self.stud9.configure(activebackground="#ececec")
        self.stud9.configure(activeforeground="#000000")
        self.stud9.configure(background="#fef1b4")
        self.stud9.configure(disabledforeground="#a3a3a3")
        self.stud9.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud9.configure(foreground="#000000")
        self.stud9.configure(highlightbackground="#d9d9d9")
        self.stud9.configure(highlightcolor="black")
        self.stud9.configure(justify='left')
        self.stud9.configure(text='''רפאל בן קימון 111122111''')
        self.stud9.configure(variable=attendance3_support.che56)

        self.stud10 = tk.Checkbutton(top)
        self.stud10.place(relx=0.381, rely=0.628, relheight=0.05, relwidth=0.181)

        self.stud10.configure(activebackground="#ececec")
        self.stud10.configure(activeforeground="#000000")
        self.stud10.configure(background="#fef1b4")
        self.stud10.configure(disabledforeground="#a3a3a3")
        self.stud10.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud10.configure(foreground="#000000")
        self.stud10.configure(highlightbackground="#d9d9d9")
        self.stud10.configure(highlightcolor="black")
        self.stud10.configure(justify='left')
        self.stud10.configure(text='''גינדה סולצמן 001122333''')
        self.stud10.configure(variable=attendance3_support.che57)

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.333, rely=0.02, relheight=0.1, relwidth=0.311)

        self.Message1.configure(background="#fef1b4")
        self.Message1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''אנא סמנו את התלמידים הנוכחים''')
        self.Message1.configure(width=597)

        self.mainmenu = tk.Button(top)
        self.mainmenu.place(relx=0.01, rely=0.913, height=73, width=176)
        self.mainmenu.configure(activebackground="#ececec")
        self.mainmenu.configure(activeforeground="#000000")
        self.mainmenu.configure(background="#f5cb03")
        self.mainmenu.configure(cursor="hand2")
        self.mainmenu.configure(disabledforeground="#a3a3a3")
        self.mainmenu.configure(foreground="#000000")
        self.mainmenu.configure(highlightbackground="#d9d9d9")
        self.mainmenu.configure(highlightcolor="black")
        self.mainmenu.configure(pady="0")
        self.mainmenu.configure(text='''תפריט ראשי''')

if __name__ == '__main__':
    vp_start_gui()




