#!/usr/bin/env python3

""" avscanner_ui.py

AVScanner user interface class

:author:	wolf
:created:	2023.09.22
"""

import tkinter as tk
import tkinter.ttk as ttk
from customtkinter import (CTk, CTkFrame, CTkLabel, CTkButton, set_appearance_mode)

# class Sidebar(CTkFrame):

#     def __init__(self, master=None, **kwargs):
#         if master is None:
#             master = app
#         super().__init__(master, **kwargs)

#         self.sb_heading_lbl = CTkLabel(self, text="Configuration")
#         self.sb_heading_lbl.pack(side="top", ipadx=40, pady=(0,20))
#         self.sb_config_btn = CTkButton(self, text="Scan")
#         self.sb_config_btn.pack()



class AVscanner():

    def __init__(self, master=None, translator=None):
        _ = translator
        if translator is None:
            def _(x): return x
        # general ui
        self.avscanner = CTk(None)
        set_appearance_mode("system")
        self.avscanner.geometry("640x480")
        self.avscanner.minsize(500, 400)
        self.avscanner.title("AVScanner")

        self.sidebar_width = tk.StringVar(value="")
        self.panedwindow_1 = ttk.Panedwindow(self.avscanner, orient="horizontal")

        # SIDEBAR
        # if subcomponents need be put into separate classes
        # self.ctkframe_1 = Sidebar(master=self.panedwindow_1, corner_radius=0, fg_color=("#eeeeee","#555555"))
        self.frame_sidebar = CTkFrame(self.panedwindow_1, corner_radius=0, fg_color=("#eeeeee","#555555"))
        self.frame_sidebar.pack()
        self.label_sb_heading = CTkLabel(self.frame_sidebar, text=_("AVScanner"))
        self.label_sb_heading.pack(side="top", ipadx=40, pady=(0, 20))
        self.button_scan = CTkButton(self.frame_sidebar, text=_("Scan"))
        self.button_scan.pack(pady=10, padx=20)
        self.button_parameters = CTkButton(self.frame_sidebar, text=_("Parameters"))
        self.button_parameters.pack(pady=10)
        self.panedwindow_1.add(self.frame_sidebar)

        # CONTENT FRAME
        self.frame_content = CTkFrame(self.panedwindow_1, corner_radius=0, fg_color=("#ffffff", "#333333"))
        self.frame_content.pack()
        self.label_content_heading = CTkLabel(self.frame_content, text=_("Content"))
        self.label_content_heading.pack(side="top")
        self.panedwindow_1.add(self.frame_content)

        self.panedwindow_1.pack(expand=True, fill="both", side="top")

        # PARAMETER FRAME
        self.frame_parameters = CTkFrame(self.panedwindow_1, corner_radius=0, fg_color=("#ffffff", "#333333"))
        self.frame_parameters.pack()
        self.label_content_heading = CTkLabel(self.frame_parameters, text=_("Parameters"))
        self.label_content_heading.pack(side="top")
        self.ctklabel_3 = CTkLabel(self.frame_parameters, textvariable=self.sidebar_width)
        self.ctklabel_3.pack(pady=20)
        self.ctkbutton_1 = CTkButton(self.frame_parameters, text=_("Get Sidebar width"), command=self.get_frame_width)
        self.ctkbutton_1.pack(pady=20)


        # Main widget
        self.mainwindow = self.avscanner

    def run(self):
        self.mainwindow.mainloop()

    def get_frame_width(self):
        sidebar_width = self.frame_content.cget("width")
        self.ctklabel_3.configure(text=sidebar_width)
        self.sidebar_width.set(sidebar_width)
        return sidebar_width


if __name__ == "__main__":
    app = AVscanner()
    app.run()
