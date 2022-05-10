#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 08, 2022 11:29:11 PM +07  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import GUI

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = GUI.Search_page(_top1)
    # Creates a toplevel widget.
    # global _top2, _w2
    # _top2 = tk.Toplevel(root)
    # _w2 = GUI.Flight_page(_top2)
    # # Creates a toplevel widget.
    # global _top3, _w3
    # _top3 = tk.Toplevel(root)
    # _w3 = GUI.Login_page(_top3)
    # # Creates a toplevel widget.
    # global _top4, _w4
    # _top4 = tk.Toplevel(root)
    # _w4 = GUI.Register_page(_top4)
    # # Creates a toplevel widget.
    # global _top5, _w5
    # _top5 = tk.Toplevel(root)
    # _w5 = GUI.Book_page(_top5)
    # # Creates a toplevel widget.
    # global _top6, _w6
    # _top6 = tk.Toplevel(root)
    # _w6 = GUI.Payment_page(_top6)
    # # Creates a toplevel widget.
    # global _top7, _w7
    # _top7 = tk.Toplevel(root)
    # _w7 = GUI.History_page(_top7)
    
    root.mainloop()

if __name__ == '__main__':
    GUI.start_up()




