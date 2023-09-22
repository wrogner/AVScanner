#!/usr/bin/env python3

""" avscanner_ui.py

AVScanner user interface class

:author:	wolf
:created:	2023.09.22
"""

import tkinter.ttk as ttk
from customtkinter import (CTk, CTkFrame, CTkLabel, CTkButton, set_appearance_mode)


class AVscanner:

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

        self.panedwindow_1 = ttk.Panedwindow(self.avscanner, orient="horizontal")

        self.ctkframe_1 = CTkFrame(self.panedwindow_1, corner_radius=0, fg_color=("#eeeeee","#555555"))
        self.ctklabel_1 = CTkLabel(self.ctkframe_1, text=_("Sidebar"))
        self.ctklabel_1.pack(side="top", ipadx=40)
        self.ctkframe_1.pack()
        self.panedwindow_1.add(self.ctkframe_1)

        self.ctkframe_2 = CTkFrame(self.panedwindow_1, corner_radius=0, fg_color=("#ffffff", "#333333"))
        self.ctklabel_2 = CTkLabel(self.ctkframe_2, text=_("Content"))
        self.ctklabel_2.pack(side="top")
        self.ctkbutton_1 = CTkButton(self.ctkframe_2, text=_("Get Sidebar width"), command=self.get_frame_width)
        self.ctkbutton_1.pack(pady=20)
        self.ctkframe_2.pack()
        self.panedwindow_1.add(self.ctkframe_2)

        self.panedwindow_1.pack(expand=True, fill="both", side="top")

        # Main widget
        self.mainwindow = self.avscanner

    def run(self):
        self.mainwindow.mainloop()

    def get_frame_width(self):
        return self.ctkframe_1.cget("width")


if __name__ == "__main__":
    app = AVscanner()
    app.run()
