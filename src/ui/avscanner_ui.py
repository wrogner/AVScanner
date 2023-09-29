#!/usr/bin/env python3

""" avscanner_ui.py

AVScanner user interface class

:author:	wolf
:created:	2023.09.22
"""

import tkinter as tk
import tkinter.ttk as ttk
from customtkinter import (CTk, CTkFrame, CTkLabel, CTkButton, set_appearance_mode)


class AVscanner():

    def __init__(self, master=None, translator=None):
        _ = translator
        if translator is None:
            def _(x): return x
        # build ui
        self.avscanner = CTk(None)
        set_appearance_mode("system")
        self.avscanner.geometry("640x480")
        self.avscanner.minsize(500, 400)
        self.avscanner.title("AVScanner")

        self.sidebar_width = tk.StringVar(value="")
        self.panedwindow_1 = ttk.Panedwindow(self.avscanner, orient="horizontal")

        self.ctkframe_1 = CTkFrame(self.panedwindow_1, corner_radius=0, fg_color=("#eeeeee","#555555"))
        self.ctkframe_1.pack()
        # self.ctkframe_1.grid(row=0, column=0, sticky="nsw")
        self.ctklabel_1 = CTkLabel(self.ctkframe_1, text=_("Sidebar"))
        self.ctklabel_1.pack(side="top", ipadx=40)
        # self.ctklabel_1.grid(row=0, column=0, sticky="n", ipadx=40)
        self.panedwindow_1.add(self.ctkframe_1)

        self.ctkframe_2 = CTkFrame(self.panedwindow_1, corner_radius=0, fg_color=("#ffffff", "#333333"))
        self.ctkframe_2.pack()
        # self.ctkframe_2.grid(row=0, column=0, sticky="nse")
        self.ctklabel_2 = CTkLabel(self.ctkframe_2, text=_("Content"))
        self.ctklabel_2.pack(side="top")
        # self.ctklabel_2.grid(row=0, column=0)
        self.ctklabel_3 = CTkLabel(self.ctkframe_2, textvariable=self.sidebar_width)
        self.ctklabel_3.pack(pady=20)
        # self.ctklabel_3.grid(row=1, column=0)
        self.ctkbutton_1 = CTkButton(self.ctkframe_2, text=_("Get Sidebar width"), command=self.get_frame_width)
        self.ctkbutton_1.pack(pady=20)
        # self.ctkbutton_1.grid(row=2, column=0)
        self.panedwindow_1.add(self.ctkframe_2)

        self.ctkframe_1._desired_width=300

        self.panedwindow_1.pack(expand=True, fill="both", side="top")


        # Main widget
        self.mainwindow = self.avscanner

    def run(self):
        self.mainwindow.mainloop()

    def get_frame_width(self):
        sidebar_width = self.ctkframe_1.cget("width")
        self.ctklabel_3.configure(text=sidebar_width)
        self.sidebar_width.set(sidebar_width)
        return sidebar_width



if __name__ == "__main__":
    app = AVscanner()
    app.run()
