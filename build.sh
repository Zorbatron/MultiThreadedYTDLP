#!/bin/bash
pyinstaller -DF --hidden-import=yt_dlp.compat._legacy -n MultiThreadedYTDLP-Linux main.py 