#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 09, 2019 05:11:15 AM +0200  platform: Windows NT
##Alex
# Jira test


import os
from functools import partial
##import keyboard
from threading import Thread as thread
import GUIandDBCommunication
import LogicGui
import Forgot_password
import support
import cv2


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
    
global root
root = None
global msgDict
msgDict = {}
global flag
flag = 0

import adodbapi
conn = adodbapi.connect("PROVIDER=SQLOLEDB;Data Source={0};Database={1}; \
       trusted_connection=yes;UID={2};PWD={3};".format("DESKTOP-H3SCR5P\SQLEXPRESS","BlinkyDB","sa","1234"))
cursor = conn.cursor()



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w
    root = tk.Tk()
    top = MainPageContainer (root)
    init(root, top)
    root.mainloop()
def vpReturnToMain(a):
    global val, w
    top = MainPageContainer (a)
    init(a, top)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    
def call_keyboard(event):
    ts = thread(target=os.system, args=("osk",))
    ts.daemon = True
    ts.start()

w = None
def create_MainPageContainer(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = MainPageContainer (w)
    init(w, top, *args, **kwargs)
    return (w, top)
def destroy_MainPageContainer():
    global w
    w.destroy()
    w = None
    

class MainPageContainer:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 12"
        if top != None:
            top.geometry("961x735+509+132")
            top.title("Blinky")
            top.configure(background="#d9d9d9")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")
        self.LoginList = {}

        self.MainPageFrame = tk.Frame(top)

        self.MainPageFrame.place(relx=0.094, rely=0.027, relheight=0.857
                , relwidth=0.832)
        self.MainPageFrame.configure(relief='groove')
        self.MainPageFrame.configure(borderwidth="2")
        self.MainPageFrame.configure(relief='groove')
        self.MainPageFrame.configure(background="#d9d9d9")
        self.MainPageFrame.configure(highlightbackground="#d9d9d9")
        self.MainPageFrame.configure(highlightcolor="black")
        self.MainPageFrame.configure(width=800)

        self.Label1 = tk.Label(self.MainPageFrame)
        self.Label1.place(relx=0.3, rely=0.016, height=76, width=262)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Sitka Display} -size 21 -weight bold -underline 1")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Blinky''')
        
        action_with_args = partial(GUIandDBCommunication.GUIandDB.Logged, self, self.LoginList, top)

        self.Login = tk.Button(self.MainPageFrame, command = action_with_args)
        self.Login.place(relx=0.388, rely=0.73, height=63, width=129)
        self.Login.configure(activebackground="#ececec")
        self.Login.configure(activeforeground="#000000")
        self.Login.configure(background="#d9d9d9")
        self.Login.configure(disabledforeground="#a3a3a3")
        self.Login.configure(foreground="#000000")
        self.Login.configure(highlightbackground="#d9d9d9")
        self.Login.configure(highlightcolor="black")
        self.Login.configure(pady="0")
        self.Login.configure(text='''Login''')




        self.ForgotPassword = tk.Button(self.MainPageFrame, command=Forgot_password.Forgot_password_U)
        self.ForgotPassword.place(relx=0.375, rely=0.873, height=63, width=146)
        self.ForgotPassword.configure(activebackground="#ececec")
        self.ForgotPassword.configure(activeforeground="#000000")
        self.ForgotPassword.configure(background="#d9d9d9")
        self.ForgotPassword.configure(disabledforeground="#a3a3a3")
        self.ForgotPassword.configure(foreground="#000000")
        self.ForgotPassword.configure(highlightbackground="#d9d9d9")
        self.ForgotPassword.configure(highlightcolor="black")
        self.ForgotPassword.configure(pady="0")
        self.ForgotPassword.configure(text='''Forgot password''')


        action_with_args = partial(LogicGui.LogicGui.RegNewUserWin, self, top)
        self.RegisterNewUser = tk.Button(self.MainPageFrame, command=action_with_args)
        self.RegisterNewUser.place(relx=0.575, rely=0.302, height=73, width=126)
        self.RegisterNewUser.configure(activebackground="#ececec")
        self.RegisterNewUser.configure(activeforeground="#000000")
        self.RegisterNewUser.configure(background="#d9d9d9")
        self.RegisterNewUser.configure(disabledforeground="#a3a3a3")
        self.RegisterNewUser.configure(foreground="#000000")
        self.RegisterNewUser.configure(highlightbackground="#d9d9d9")
        self.RegisterNewUser.configure(highlightcolor="black")
        self.RegisterNewUser.configure(pady="0")
        self.RegisterNewUser.configure(text='''Register''')

        self.NewUserLabel = tk.Label(self.MainPageFrame)
        self.NewUserLabel.place(relx=0.588, rely=0.222, height=34, width=95)
        self.NewUserLabel.configure(activebackground="#f9f9f9")
        self.NewUserLabel.configure(activeforeground="black")
        self.NewUserLabel.configure(background="#d9d9d9")
        self.NewUserLabel.configure(disabledforeground="#a3a3a3")
        self.NewUserLabel.configure(font="-family {Segoe UI} -size 12")
        self.NewUserLabel.configure(foreground="#000000")
        self.NewUserLabel.configure(highlightbackground="#d9d9d9")
        self.NewUserLabel.configure(highlightcolor="black")
        self.NewUserLabel.configure(text='''New user?''')

        self.SignInLabel = tk.Label(self.MainPageFrame)
        self.SignInLabel.place(relx=0.4, rely=0.46, height=37, width=81)
        self.SignInLabel.configure(activebackground="#f9f9f9")
        self.SignInLabel.configure(activeforeground="black")
        self.SignInLabel.configure(background="#d9d9d9")
        self.SignInLabel.configure(disabledforeground="#a3a3a3")
        self.SignInLabel.configure(font="-family {Segoe UI} -size 14")
        self.SignInLabel.configure(foreground="#000000")
        self.SignInLabel.configure(highlightbackground="#d9d9d9")
        self.SignInLabel.configure(highlightcolor="black")
        self.SignInLabel.configure(text='''Sign in:''')

        self.UserNameLabel = tk.Label(self.MainPageFrame)
        self.UserNameLabel.place(relx=0.338, rely=0.524, height=34, width=106)
        self.UserNameLabel.configure(activebackground="#f9f9f9")
        self.UserNameLabel.configure(activeforeground="black")
        self.UserNameLabel.configure(background="#d9d9d9")
        self.UserNameLabel.configure(disabledforeground="#a3a3a3")
        self.UserNameLabel.configure(font="-family {Segoe UI} -size 12")
        self.UserNameLabel.configure(foreground="#000000")
        self.UserNameLabel.configure(highlightbackground="#d9d9d9")
        self.UserNameLabel.configure(highlightcolor="black")
        self.UserNameLabel.configure(text='''User Name:''')

        self.PassLabel = tk.Label(self.MainPageFrame)
        self.PassLabel.place(relx=0.338, rely=0.619, height=34, width=92)
        self.PassLabel.configure(activebackground="#f9f9f9")
        self.PassLabel.configure(activeforeground="black")
        self.PassLabel.configure(background="#d9d9d9")
        self.PassLabel.configure(disabledforeground="#a3a3a3")
        self.PassLabel.configure(font="-family {Segoe UI} -size 12")
        self.PassLabel.configure(foreground="#000000")
        self.PassLabel.configure(highlightbackground="#d9d9d9")
        self.PassLabel.configure(highlightcolor="black")
        self.PassLabel.configure(text='''Password:''')

        self.UserNameText = tk.Entry(self.MainPageFrame)
        self.UserNameText.bind("<1>", call_keyboard)

        self.UserNameText.place(relx=0.338, rely=0.571, height=24
                , relwidth=0.255)
        self.UserNameText.configure(background="white")
        self.UserNameText.configure(disabledforeground="#a3a3a3")
        self.UserNameText.configure(font="TkFixedFont")
        self.UserNameText.configure(foreground="#000000")
        self.UserNameText.configure(highlightbackground="#d9d9d9")
        self.UserNameText.configure(highlightcolor="black")
        self.UserNameText.configure(insertbackground="black")
        self.UserNameText.configure(selectbackground="#c4c4c4")
        self.UserNameText.configure(selectforeground="black")

        self.PasswordText = tk.Entry(self.MainPageFrame, show="*")
        self.PasswordText.place(relx=0.338, rely=0.667, height=24
                , relwidth=0.255)
        self.PasswordText.configure(background="white")
        self.PasswordText.configure(disabledforeground="#a3a3a3")
        self.PasswordText.configure(font="TkFixedFont")
        self.PasswordText.configure(foreground="#000000")
        self.PasswordText.configure(highlightbackground="#d9d9d9")
        self.PasswordText.configure(highlightcolor="black")
        self.PasswordText.configure(insertbackground="black")
        self.PasswordText.configure(selectbackground="#c4c4c4")
        self.PasswordText.configure(selectforeground="black")
        self.PasswordText.bind("<1>", call_keyboard)
        
        action_with_args = partial(LogicGui.LogicGui.ShowInfo,self,top)

        self.Info = tk.Button(self.MainPageFrame, command = action_with_args)
        self.Info.place(relx=0.7, rely=0.048, height=63, width=196)
        self.Info.configure(activebackground="#ececec")
        self.Info.configure(activeforeground="#000000")
        self.Info.configure(background="#d9d9d9")
        self.Info.configure(disabledforeground="#a3a3a3")
        self.Info.configure(foreground="#000000")
        self.Info.configure(highlightbackground="#d9d9d9")
        self.Info.configure(highlightcolor="black")
        self.Info.configure(pady="0")
        self.Info.configure(text='''Information and help''')
        
        action_with_args = partial(LogicGui.LogicGui.RegNewMenWin, self, top)
        
        self.RegisterNewMentor = tk.Button(self.MainPageFrame, command=action_with_args)
        self.RegisterNewMentor.place(relx=0.2, rely=0.302, height=73, width=136)
        self.RegisterNewMentor.configure(activebackground="#ececec")
        self.RegisterNewMentor.configure(activeforeground="#000000")
        self.RegisterNewMentor.configure(background="#d9d9d9")
        self.RegisterNewMentor.configure(disabledforeground="#a3a3a3")
        self.RegisterNewMentor.configure(foreground="#000000")
        self.RegisterNewMentor.configure(highlightbackground="#d9d9d9")
        self.RegisterNewMentor.configure(highlightcolor="black")
        self.RegisterNewMentor.configure(pady="0")
        self.RegisterNewMentor.configure(text='''Register''')
        self.RegisterNewMentor.configure(width=136)

        self.NewMentor = tk.Label(self.MainPageFrame)
        self.NewMentor.place(relx=0.2, rely=0.238, height=26, width=142)
        self.NewMentor.configure(background="#d9d9d9")
        self.NewMentor.configure(disabledforeground="#a3a3a3")
        self.NewMentor.configure(font=font9)
        self.NewMentor.configure(foreground="#000000")
        self.NewMentor.configure(text='''New Mentor?''')
        self.NewMentor.configure(width=142)
        
        self.LoginList["UserNameText"] = self.UserNameText
        self.LoginList["PasswordText"] = self.PasswordText
        
    
if __name__ == '__main__':
        vp_start_gui()




