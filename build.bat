@echo off
pyinstaller -DF --hidden-import=yt_dlp.compat._legacy -n MultiThreadedYTDLP-Windows main.py 