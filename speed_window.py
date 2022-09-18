import os

from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx
from resources import *
from tkinter import messagebox
import tkinter as tk

video_path=""


def validate_speed(volume_entry, sv):
    if (sv.get().isdigit() or not sv.get().isalnum()) and len(sv.get()) <= 3:
        if float(sv.get()) > 100:
            sv.set('100')
    else:
        sv.set('0')


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
    speed_window.geometry('280x240')
    speed_window.resizable(False, False)
    speed_window.configure(background=DARK)
    window.withdraw()

    add_video_button = get_button("add a video", get_video_file, speed_window)
    add_video_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky='we', columnspan=2)
    speed_window.grid_columnconfigure(0, weight=1)

    video_name_label = get_label("No video selected", speed_window)
    video_name_label.grid(row=1, column=0, sticky='we', columnspan=2, pady=(0, 25))

    speed_label = get_label("speed (1x - 100x)", speed_window)
    speed_label.grid(row=2, column=0, sticky="w", padx=10, columnspan=2)

    speed_value = tk.StringVar(speed_window, value='1')
    volume_entry = get_entry(speed_window, var=speed_value)
    volume_entry.grid(row=3, column=0, sticky="we", padx=13, columnspan=2)

    speed_value.trace("w", lambda name, index, mode, sv=speed_value: validate_speed(volume_entry, sv))

    speed_window.grid_columnconfigure(1, weight=1)

    def replace_main_window():
        speed_window.destroy()
        window.deiconify()

    back_button = get_button("back", replace_main_window, speed_window, height=1)
    back_button.grid(row=4, column=0, sticky="we", padx=10, pady=(50, 0))

    def change_speed():
        if float(speed_value.get()) and float(speed_value.get()) > 0:
            if video_path:
                clip = VideoFileClip(video_path)
                clip = clip.fx(vfx.speedx, float(speed_value.get()))
                clip.write_videofile(os.path.expanduser("~") + f"/videos/{video_path.split('/')[-1]}_speed.mp4")
            else:
                messagebox.showerror("Error", "No video selected")
        else:
            messagebox.showerror("Error", "Invalid speed")
    render_button = get_button("render", command=change_speed, window=speed_window, height=1)
    render_button.grid(row=4, column=1, sticky="we", padx=10, pady=(50, 0))

    speed_window.mainloop()
