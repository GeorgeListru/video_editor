import os

from moviepy.editor import VideoFileClip

from resources import *
from tkinter import messagebox
import tkinter as tk

video_path=""

def replace_speed_window(window):
    def get_video_file():
        filename = select_video_file()
        if filename:
            global video_path
            video_path = filename
            video_name = filename.split('/')[-1]
            video_name_label.config(text=video_name)
            add_video_button.config(text='CHANGE VIDEO')

    speed_window = tk.Tk()
    speed_window.title('Add Audio')
    speed_window.geometry('280x360')
    speed_window.resizable(False, False)
    speed_window.configure(background=DARK)
    window.withdraw()

    add_video_button = get_button("add a video", get_video_file, speed_window)
    add_video_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky='we', columnspan=2)
    trim_window.grid_columnconfigure(0, weight=1)

    video_name_label = get_label("No video selected", speed_window)
    video_name_label.grid(row=1, column=0, sticky='we', columnspan=2, pady=(0, 25))