#!/usr/bin/env python3

""" AVScanner.py

AVScanner - a ClamAV scanner frontend in Python

:author:	wolf
:created:	2023.09.22
"""

from ui import AVscanner

if __name__ == "__main__":
    app = AVscanner()
    app.run()