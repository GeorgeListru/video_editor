import os

from moviepy.editor import VideoFileClip

from resources import *
from tkinter import messagebox
import tkinter as tk

video_path=""

def replace_trim_window (window):

    def get_video_file():
        filename=select_video_file()
        if filename:
            global video_path
            video_path = filename
            video_name = filename.split('/')[-1]
            video_name_label.config(text=video_name)
            add_video_button.config(text='CHANGE VIDEO')

    window.withdraw()

    trim_window = tk.Tk()
    trim_window.title('Trim Video')
    trim_window.geometry('280x260')
    trim_window.resizable(False, False)
    trim_window.configure(background=DARK)

    add_video_button = get_button("add a video", get_video_file, trim_window)
    add_video_button.grid(row=0, column=0, padx=10, pady=(10,5), sticky='we',columnspan=2)
    trim_window.grid_columnconfigure(0, weight=1)


    video_name_label = get_label("No video selected", trim_window)
    video_name_label.grid(row=1, column=0, sticky='we',columnspan=2, pady=(0,25))

    begin_label = get_label("begin", trim_window)
    begin_label.grid(row=2, column=0, sticky="w",padx=10)
    end_label = get_label("end", trim_window)
    end_label.grid(row=2, column=1,sticky="e",padx=10)

    begin_value = tk.StringVar()
    begin_entry = get_entry(trim_window,placeholder="00:00:00", var=begin_value)
    begin_entry.grid(row=3, column=0, sticky="w",padx=13)

    end_value = tk.StringVar()
    end_entry = get_entry(trim_window,placeholder="00:00:00", var=end_value)
    end_entry.grid(row=3, column=1, sticky="e",padx=13)

    begin_value.trace("w", lambda name, index, mode, sv=begin_value: validate_time(begin_entry, sv))
    end_value.trace("w", lambda name, index, mode, sv=end_value: validate_time(end_entry, sv))

    trim_window.grid_columnconfigure(1, weight=1)

    ## create a back button to go back to main window
    def replace_main_window():
        trim_window.destroy()
        window.deiconify()

    back_button = get_button("back", replace_main_window, trim_window, height=1)
    back_button.grid(row=4, column=0, sticky="we", padx=10, pady=(50, 0))

    def trim_video():
        if video_path == "":
            return
        begin = begin_value.get()
        end = end_value.get()
        if begin == "" or end == "":
            return
        begin = begin.split(":")
        end = end.split(":")
        begin = int(begin[0]) * 3600 + int(begin[1]) * 60 + int(begin[2])
        end = int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2])
        if begin >= end:
            return
        clip = VideoFileClip(video_path)
        clip = clip.subclip(begin, end)
        clip.write_videofile(os.path.expanduser("~") + f"/videos/{video_path.split('/')[-1]}_trimmed.mp4")
        message =  messagebox.showinfo("Trim Video", "Video trimmed successfully")
        if message == "ok":
            replace_main_window()

    render_button = get_button("render", command=trim_video, window=trim_window, height=1)
    render_button.grid(row=4, column=1, sticky="we", padx=10, pady=(50, 0))

    trim_window.mainloop()