#!/usr/bin/env python3

""" x_test.py

CustomTkinter testfile

:author:	wolf
:created:	2023.09.21
"""


from customtkinter import *

app = CTk()
app.geometry("500x400")

btn_misc = CTkButton(master=app, text="Click Me!")
btn_misc.pack(pady=20)

if __name__ == "__main__":
    app.mainloop()