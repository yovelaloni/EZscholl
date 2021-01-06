#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Jan 06, 2021 03:04:19 PM +0200  platform: Windows NT

import sys
sys.path.append('..')
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

import FeedBackTeacher_support
from data import getUser, connect_to_db_and_collection, connect_to_db, getSubject
import Teachermainmenu
from tkinter import messagebox,filedialog
import base64

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    FeedBackTeacher_support.set_Tk_var()
    top = FeedbackTeacher (root)
    FeedBackTeacher_support.init(root, top)
    root.mainloop()

w = None
def create_FeedbackTeacher(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_FeedbackTeacher(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    FeedBackTeacher_support.set_Tk_var()
    top = FeedbackTeacher (w)
    FeedBackTeacher_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_FeedbackTeacher():
    global w
    w.destroy()
    w = None

class FeedbackTeacher:


    def RemoveFeedback(self):
        self.MarkL.place_forget()
        self.GradeEn.place_forget()
        self.feebackL.place_forget()
        self.textBX.place_forget()
        self.uploadfeedBtn.place_forget()
        self.cancelfeedBtn.place_forget()

    def Showfeedbackwidgets(self):
        self.MarkL.place(relx=0.667, rely=0.349, height=41, width=114)
        self.GradeEn.place(relx=0.667, rely=0.479, height=30, relwidth=0.19)
        self.feebackL.place(relx=0.117, rely=0.349, height=41, width=244)
        self.textBX.place(relx=0.117, rely=0.458, relheight=0.229, relwidth=0.425)
        self.uploadfeedBtn.place(relx=0.6, rely=0.719, height=74, width=177)
        self.cancelfeedBtn.place(relx=0.29, rely=0.719, height=74, width=177)

    def openmainmenu(self):
        root.destroy()
        Teachermainmenu.vp_start_gui()

    def Reset(self):
        self.RemoveFeedback()
        self.StudListC.configure(state='normal')
        self.getstudHWbtn.configure(state='normal')
        self.AssignSB.configure(state='normal')
        self.GradeEn.delete(0,"end")
        self.textBX.delete(1.0,"end")

    def DownHW(self):
        self.chosen_user = self.StudListC.get()
        mycol = connect_to_db_and_collection('EZSchooldb', f'Assignments{self.chosen_user}')
        data = mycol.find_one({'Assignment_num': int(self.AssignSB.get())})
        if data == None:
            messagebox.showwarning('קבוץ לא קיים', 'תלמיד לא הגיש מטלה זו')
        else:
            file = filedialog.asksaveasfile(initialdir='/', title="בחר שם ומיקום להורדה", mode='wb',
                                        filetypes=[('PDF files', '*pdf'), ('RAR files', '*.rar'),
                                                   ('ZIP files', '*zip')],
                                        defaultextension='.pdf', initialfile=data['file_name'])
            if file == None:
                return
            file.write(base64.b64decode(data['Assignment_file']))
            self.StudListC.configure(state='disabled')
            self.getstudHWbtn.configure(state='disabled')
            self.AssignSB.configure(state='disable')
            self.Showfeedbackwidgets()

    def Uploadfeedback(self):
        grade = self.GradeEn.get()
        if not grade.isdigit() or not (int(grade)>=0 and int(grade)<=100):
            messagebox.showwarning('ציון', 'נא להזין ציון בין 0 ל 100')
            return
        else:
            mycol = connect_to_db_and_collection('EZSchooldb', f'Assignments{self.chosen_user}')
            mycol.update_one({'Assignment_num': int(self.AssignSB.get())},
                              {"$set": {"grade": int(self.GradeEn.get())}})
            mycol.update_one({'Assignment_num': int(self.AssignSB.get())},
                            {"$set": {"FeedBack": self.textBX.get("1.0", 'end')}})
            self.Reset()


    def __init__(self, top=None):
        self.current_subject = getSubject()
        self.user_list = []
        usercolec = connect_to_db_and_collection('EZSchooldb', 'Users')
        for user in usercolec.find({'Usertype': 3}):
            self.user_list.append(user['id'])

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x459+726+356")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("משוב לשיעורי בית")
        top.configure(background="#80ffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.FeedbL = tk.Label(top)
        self.FeedbL.place(relx=0.383, rely=0.022, height=41, width=134)
        self.FeedbL.configure(activebackground="#f9f9f9")
        self.FeedbL.configure(activeforeground="black")
        self.FeedbL.configure(background="#ff00ff")
        self.FeedbL.configure(disabledforeground="#a3a3a3")
        self.FeedbL.configure(font="-family {Segoe UI} -size 18 -weight bold -underline 1")
        self.FeedbL.configure(foreground="#000000")
        self.FeedbL.configure(highlightbackground="#d9d9d9")
        self.FeedbL.configure(highlightcolor="black")
        self.FeedbL.configure(relief="ridge")
        if self.current_subject == 'Math':
            self.FeedbL.configure(text='''משוב לחשבון''')
        elif self.current_subject == 'History':
            self.FeedbL.configure(text='''משוב להיסטוריה''')
        elif self.current_subject == 'Hebrew':
            self.FeedbL.configure(text='''משוב לעברית''')
        elif self.current_subject == 'Tanach':
            self.FeedbL.configure(text='''משוב לתנ"ך''')


        self.StudListC = ttk.Combobox(top)
        self.StudListC.place(relx=0.633, rely=0.218, relheight=0.068
                , relwidth=0.288)
        self.StudListC.configure(value= self.user_list)
        self.StudListC.configure(takefocus="")
        self.StudListC.current(0)

        self.getstudHWbtn = tk.Button(top)
        self.getstudHWbtn.place(relx=0.033, rely=0.131, height=74, width=177)
        self.getstudHWbtn.configure(activebackground="#ececec")
        self.getstudHWbtn.configure(activeforeground="#000000")
        self.getstudHWbtn.configure(background="#ff0000")
        self.getstudHWbtn.configure(disabledforeground="#a3a3a3")
        self.getstudHWbtn.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.getstudHWbtn.configure(foreground="#000000")
        self.getstudHWbtn.configure(highlightbackground="#ffffff")
        self.getstudHWbtn.configure(highlightcolor="black")
        self.getstudHWbtn.configure(pady="0")
        self.getstudHWbtn.configure(text='''להורדת שיעורי הבית''')
        self.getstudHWbtn.configure(command=self.DownHW)

        self.StudL = tk.Label(top)
        self.StudL.place(relx=0.633, rely=0.131, height=31, width=174)
        self.StudL.configure(activebackground="#f9f9f9")
        self.StudL.configure(activeforeground="black")
        self.StudL.configure(background="#0080ff")
        self.StudL.configure(disabledforeground="#a3a3a3")
        self.StudL.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.StudL.configure(foreground="#000000")
        self.StudL.configure(highlightbackground="#d9d9d9")
        self.StudL.configure(highlightcolor="black")
        self.StudL.configure(relief="ridge")
        self.StudL.configure(text='''לבחירת תלמיד''')



        self.MainMenuBtn = tk.Button(top)
        self.MainMenuBtn.place(relx=0.033, rely=0.828, height=64, width=127)
        self.MainMenuBtn.configure(activebackground="#ececec")
        self.MainMenuBtn.configure(activeforeground="#000000")
        self.MainMenuBtn.configure(background="#ffffff")
        self.MainMenuBtn.configure(disabledforeground="#a3a3a3")
        self.MainMenuBtn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.MainMenuBtn.configure(foreground="#000000")
        self.MainMenuBtn.configure(highlightbackground="#d9d9d9")
        self.MainMenuBtn.configure(highlightcolor="black")
        self.MainMenuBtn.configure(pady="0")
        self.MainMenuBtn.configure(text='''תפריט ראשי''')
        self.MainMenuBtn.configure(command=self.openmainmenu)

        self.AssignSB = tk.Spinbox(top, from_=1.0, to=100.0)
        self.AssignSB.place(relx=0.367, rely=0.24, relheight=0.041
                , relwidth=0.242)
        self.AssignSB.configure(activebackground="#f9f9f9")
        self.AssignSB.configure(background="white")
        self.AssignSB.configure(buttonbackground="#d9d9d9")
        self.AssignSB.configure(disabledforeground="#a3a3a3")
        self.AssignSB.configure(font="TkDefaultFont")
        self.AssignSB.configure(foreground="black")
        self.AssignSB.configure(highlightbackground="black")
        self.AssignSB.configure(highlightcolor="black")
        self.AssignSB.configure(insertbackground="black")
        self.AssignSB.configure(selectbackground="blue")
        self.AssignSB.configure(selectforeground="white")
        self.AssignSB.configure(values=list(range(1,11)))

        self.AssignNumL = tk.Label(top)
        self.AssignNumL.place(relx=0.367, rely=0.131, height=31, width=134)
        self.AssignNumL.configure(activeforeground="#000000")
        self.AssignNumL.configure(background="#0080ff")
        self.AssignNumL.configure(disabledforeground="#a3a3a3")
        self.AssignNumL.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.AssignNumL.configure(foreground="#000000")
        self.AssignNumL.configure(relief="ridge")
        self.AssignNumL.configure(text='''מס' מטלה''')

        self.MarkL = tk.Label(top)
        self.MarkL.configure(activebackground="#f9f9f9")
        self.MarkL.configure(activeforeground="black")
        self.MarkL.configure(background="#d9d9d9")
        self.MarkL.configure(disabledforeground="#a3a3a3")
        self.MarkL.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.MarkL.configure(foreground="#000000")
        self.MarkL.configure(highlightbackground="#d9d9d9")
        self.MarkL.configure(highlightcolor="black")
        self.MarkL.configure(relief="ridge")
        self.MarkL.configure(text='''ציון''')

        self.GradeEn = tk.Entry(top)
        self.GradeEn.configure(background="white")
        self.GradeEn.configure(disabledforeground="#a3a3a3")
        self.GradeEn.configure(font="TkFixedFont")
        self.GradeEn.configure(foreground="#000000")
        self.GradeEn.configure(highlightbackground="#d9d9d9")
        self.GradeEn.configure(highlightcolor="black")
        self.GradeEn.configure(insertbackground="black")
        self.GradeEn.configure(selectbackground="blue")
        self.GradeEn.configure(selectforeground="white")

        self.feebackL = tk.Label(top)
        self.feebackL.configure(activebackground="#f9f9f9")
        self.feebackL.configure(activeforeground="black")
        self.feebackL.configure(background="#d9d9d9")
        self.feebackL.configure(disabledforeground="#a3a3a3")
        self.feebackL.configure(font="-family {Segoe UI} -size 12 -weight bold -underline 1")
        self.feebackL.configure(foreground="#000000")
        self.feebackL.configure(highlightbackground="#d9d9d9")
        self.feebackL.configure(highlightcolor="black")
        self.feebackL.configure(relief="ridge")
        self.feebackL.configure(text='''משוב''')

        self.textBX = tk.Text(top)
        self.textBX.configure(background="white")
        self.textBX.configure(font="TkTextFont")
        self.textBX.configure(foreground="black")
        self.textBX.configure(highlightbackground="#d9d9d9")
        self.textBX.configure(highlightcolor="black")
        self.textBX.configure(insertbackground="black")
        self.textBX.configure(insertborderwidth="3")
        self.textBX.configure(selectbackground="blue")
        self.textBX.configure(selectforeground="white")
        self.textBX.configure(wrap="none")

        self.uploadfeedBtn = tk.Button(top)
        self.uploadfeedBtn.configure(activebackground="#ececec")
        self.uploadfeedBtn.configure(activeforeground="#000000")
        self.uploadfeedBtn.configure(background="#00ff40")
        self.uploadfeedBtn.configure(disabledforeground="#a3a3a3")
        self.uploadfeedBtn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.uploadfeedBtn.configure(foreground="#000000")
        self.uploadfeedBtn.configure(highlightbackground="#d9d9d9")
        self.uploadfeedBtn.configure(highlightcolor="black")
        self.uploadfeedBtn.configure(pady="0")
        self.uploadfeedBtn.configure(text='''העלאת משוב''')
        self.uploadfeedBtn.configure(command=self.Uploadfeedback)

        self.cancelfeedBtn = tk.Button(top)
        self.cancelfeedBtn.configure(activebackground="#ececec")
        self.cancelfeedBtn.configure(activeforeground="#000000")
        self.cancelfeedBtn.configure(background="#ff0000")
        self.cancelfeedBtn.configure(disabledforeground="#a3a3a3")
        self.cancelfeedBtn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.cancelfeedBtn.configure(foreground="#000000")
        self.cancelfeedBtn.configure(highlightbackground="#d9d9d9")
        self.cancelfeedBtn.configure(highlightcolor="black")
        self.cancelfeedBtn.configure(pady="0")
        self.cancelfeedBtn.configure(text='''בטל העלאה''')
        self.cancelfeedBtn.configure(command=self.Reset)



if __name__ == '__main__':
    vp_start_gui()





