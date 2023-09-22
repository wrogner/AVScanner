#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "avscanner_ui.ui"

class AVscanner:
    def __init__(self, master=None, translator=None):
        self.builder = builder = pygubu.Builder(translator)
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("avscanner", master)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    app = AVscanner()
    app.run()
