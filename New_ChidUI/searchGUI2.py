#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 11, 2022 11:14:50 PM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import searchGUI2_support

from PIL import Image, ImageTk
from tkcalendar import DateEntry

import system

def changePage(oldpage,newpage):
        oldpage.destroy()
        root = tk.Tk()
        newpage(root)

class search_page:

#     def SearchFlight(self):
#         self.top.destroy()
#         root = tk.Tk()
#         Toplevel1(self.combobox.get(), self.combobox1.get(), self.combobox2.get(),root)

    def __init__(self, top=None):
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

        top.geometry("800x600+588+204")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Search Flight")
        top.configure(background="#6fc4d2")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()
        self.combobox1 = tk.StringVar()
        self.combobox2 = tk.StringVar()

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=-0.004, rely=0.0, height=600, width=803)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = Image.open("Searching103.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')

        self.Button_searchpage = tk.Button(self.top)
        self.Button_searchpage.place(relx=0.388, rely=0.083, height=44
                , width=137)
        self.Button_searchpage.configure(activebackground="#145954")
        self.Button_searchpage.configure(activeforeground="white")
        self.Button_searchpage.configure(activeforeground="#ffffff")
        self.Button_searchpage.configure(background="#145954")
        self.Button_searchpage.configure(compound='left')
        self.Button_searchpage.configure(disabledforeground="#a3a3a3")
        self.Button_searchpage.configure(font="-family {Trebuchet MS} -size 19 -weight bold")
        self.Button_searchpage.configure(foreground="#ffffff")
        self.Button_searchpage.configure(highlightbackground="#d9d9d9")
        self.Button_searchpage.configure(highlightcolor="black")
        self.Button_searchpage.configure(pady="0")
        self.Button_searchpage.configure(relief="flat")
        self.Button_searchpage.configure(text='''Search''')
        # self.Button_search.configure(command=self.SearchFlight)
      

        self.Button_historypage = tk.Button(self.top)
        self.Button_historypage.place(relx=0.569, rely=0.083, height=44
                , width=137)
        self.Button_historypage.configure(activebackground="#145954")
        self.Button_historypage.configure(activeforeground="white")
        self.Button_historypage.configure(activeforeground="#ffffff")
        self.Button_historypage.configure(background="#c0c0c0")
        self.Button_historypage.configure(compound='left')
        self.Button_historypage.configure(disabledforeground="#a3a3a3")
        self.Button_historypage.configure(font="-family {Trebuchet MS} -size 19 -weight bold")
        self.Button_historypage.configure(foreground="#ffffff")
        self.Button_historypage.configure(highlightbackground="#d9d9d9")
        self.Button_historypage.configure(highlightcolor="black")
        self.Button_historypage.configure(pady="0")
        self.Button_historypage.configure(relief="flat")
        self.Button_historypage.configure(text='''History''')
        

        self.Button_logout = tk.Button(self.top)
        self.Button_logout.place(relx=0.75, rely=0.083, height=44, width=137)
        self.Button_logout.configure(activebackground="#145954")
        self.Button_logout.configure(activeforeground="white")
        self.Button_logout.configure(activeforeground="#ffffff")
        self.Button_logout.configure(background="#c0c0c0")
        self.Button_logout.configure(compound='left')
        self.Button_logout.configure(disabledforeground="#a3a3a3")
        self.Button_logout.configure(font="-family {Trebuchet MS} -size 19 -weight bold")
        self.Button_logout.configure(foreground="#ffffff")
        self.Button_logout.configure(highlightbackground="#d9d9d9")
        self.Button_logout.configure(highlightcolor="black")
        self.Button_logout.configure(pady="0")
        self.Button_logout.configure(relief="flat")
        self.Button_logout.configure(text='''Logout''')

        self.Button_search = tk.Button(self.top)
        self.Button_search.place(relx=0.488, rely=0.767, height=44, width=227)
        self.Button_search.configure(activebackground="#ececec")
        self.Button_search.configure(activeforeground="#000000")
        self.Button_search.configure(background="#145954")
        self.Button_search.configure(compound='left')
        self.Button_search.configure(disabledforeground="#a3a3a3")
        self.Button_search.configure(font="-family {Trebuchet MS} -size 19 -weight bold")
        self.Button_search.configure(foreground="#ffffff")
        self.Button_search.configure(highlightbackground="#d9d9d9")
        self.Button_search.configure(highlightcolor="black")
        self.Button_search.configure(pady="0")
        self.Button_search.configure(relief="flat")
        self.Button_search.configure(text='''Search Flights''')

        self.TCombobox_origin = ttk.Combobox(self.top, values=system.Source.getAllSource())
        self.TCombobox_origin.place(relx=0.45, rely=0.317, relheight=0.035
                , relwidth=0.35)
        self.TCombobox_origin.configure(textvariable=self.combobox)
        self.TCombobox_origin.configure(takefocus="")

        self.TCombobox_destination = ttk.Combobox(self.top, values=system.Flight.getAllDestination())
        self.TCombobox_destination.place(relx=0.45, rely=0.483, relheight=0.035
                , relwidth=0.35)
        self.TCombobox_destination.configure(textvariable=self.combobox1)
        self.TCombobox_destination.configure(takefocus="")

        self.Entry_date = ttk.Combobox(self.top)
        self.Entry_date=DateEntry(selectmode='day',background= "darkturquoise")
        self.Entry_date.place(relx=0.45, rely=0.642, relheight=0.035
                , relwidth=0.35)
        self.Entry_date.configure(textvariable=self.combobox2)
        self.Entry_date.configure(takefocus="")


def start_up():
    searchGUI2_support.main()

if __name__ == '__main__':
    searchGUI2_support.main()




