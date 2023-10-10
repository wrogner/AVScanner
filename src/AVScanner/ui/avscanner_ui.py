#!/usr/bin/env python3

""" avscanner_ui.py

AVScanner user interface class

:author:	wolf
:created:	2023.09.22
"""

import os
import pathlib
from PIL import Image
import tkinter as tk
import tkinter.ttk as ttk
from customtkinter import (CTk, CTkFrame, CTkLabel, CTkButton, CTkImage, CTkFont, set_appearance_mode)

GUIPATH = os.path.dirname(os.path.realpath(__file__))
IMGPATH = pathlib.Path(GUIPATH).parent.joinpath("img")

class AVscanner(CTk):
    """Class AVscanner

    Scanner class that wraps around clamAV scanner

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.geometry("720x480")
        self.minsize(500, 400)
        self.title("AVScanner")

        self.guipath = GUIPATH
        self.imgpath = IMGPATH
        self.logo = CTkImage(Image.open(IMGPATH.joinpath("AVScanner.png")), size=(28, 28))

        # grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # NAVIGATION FRAME
        self.navigation_frame = CTkFrame(self, corner_radius=0, fg_color=("#eeeeee", "#555555"), width=200)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)


        self.logo_label = CTkLabel(self.navigation_frame, text="  AVScanner", image=self.logo, compound="left", font=CTkFont(family=".AppleSystemUIFont", size=18, weight="bold"))
        self.logo_label.grid(row=0, column=0, pady=(10, 20), padx=20, sticky="new")

        self.scan_button = CTkButton(self.navigation_frame, text="Scan", font=CTkFont(family=".AppleSystemUIFont", size=15, weight="bold"),
                                     corner_radius=0, height=40, border_spacing=20,
                                      fg_color="transparent", text_color=("gray20", "gray90"), hover_color=("gray70", "gray30"),
                                     anchor="w", command=self.click_scan_button)
        self.scan_button.grid(row=1, column=0, sticky="ew")

        self.parameter_button = CTkButton(self.navigation_frame, text="Parameters", font=CTkFont(family=".AppleSystemUIFont", size=15, weight="bold"),
                                          corner_radius=0, height=40, border_spacing=20,
                                          fg_color="transparent", text_color=("gray20", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.click_parameter_button)
        self.parameter_button.grid(row=2, column=0, sticky="ew")

        self.copyright_label = CTkLabel(self.navigation_frame, text="© 2023 by war", font=CTkFont(family=".AppleSystemUIFont", size=10))
        self.copyright_label.grid(row=4, column=0, padx=10, sticky="sw")

        # SCAN FRAME
        self.scan_frame = CTkFrame(self, corner_radius=0, fg_color=("#ffffff", "#333333"))
        self.scan_frame.grid_columnconfigure(0, weight=1)

        self.sf_label_heading = CTkLabel(self.scan_frame, text="Scanning", anchor="center")
        self.sf_label_heading.grid(row=0, column=0)

        # TODO: define scanning functionality
        # [ ] select single file to scan
        # [ ] select directory to scan
        # [ ] scan all



        # PARAMETER FRAME
        self.parameter_frame = CTkFrame(self, corner_radius=0, fg_color=("#ffffff", "#333333"))
        self.parameter_frame.grid_columnconfigure(0, weight=1)

        self.pf_label_heading = CTkLabel(self.parameter_frame, text="Parameter settings", anchor="center")
        self.pf_label_heading.grid(row=0, column=0)

        # TODO: define scanning functionality
        # [ ] update signatures
        # [ ] select clamAV scanner
        # [ ] scanning parameters (if any)

        # set SCAN_FRAME default
        self.scan_frame.grid(row=0, column=1, sticky="nsew")


    def click_scan_button(self):
        """Event handler: select scan frame"""
        self.select_frame("scan")


    def click_parameter_button(self):
        """Event handler: select parameter frame"""
        self.select_frame("parameter")


    def select_frame(self, frame_name):
        """
        Select frame, show input mask

            Parameters:
                :frame_name:		frame to select ["scan" | "parameter"]

            Returns:
                None

            Errors:
                None
        """

        # set selected button background
        self.scan_button.configure(fg_color=("gray85", "gray25") if frame_name == "scan" else "transparent")
        self.parameter_button.configure(fg_color=("gray85", "gray25") if frame_name == "parameter" else "transparent")

        # set frame visibility by grid packing, otherwise forget
        # not nice, but works
        # if frame_name == "scan":
        #     self.scan_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.scan_frame.grid_forget()

        # if frame_name == "parameter":
        #     self.parameter_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.parameter_frame.grid_forget()
        self.scan_frame.grid(row=0, column=1, sticky="nsew") if frame_name == "scan" else self.scan_frame.grid_forget()
        self.parameter_frame.grid(row=0, column=1, sticky="nsew") if frame_name == "parameter" else self.parameter_frame.grid_forget()



    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = AVscanner()
    app.run()
