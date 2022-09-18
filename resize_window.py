import os

from moviepy.editor import VideoFileClip

from resources import *
from tkinter import messagebox
import tkinter as tk

video_path=""
locked_aspect_ratio = True
video_width=0
video_height=0


def update_height(width_value, height_value):
    try:
        value = int(width_value.get())
        if value < 0:
            value = 0
        width_value.set(value)
        if locked_aspect_ratio:
            height_value.set(int(value * video_height / video_width))
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


def update_width(height_value, width_value):
    try:
        value = int(height_value.get())
        if value < 0:
            value = 0
        height_value.set(value)
        if locked_aspect_ratio:
            width_value.set(int(value * video_width / video_height))
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


def replace_resize_window (window):

    def get_video_file():
        filename=select_video_file()
        if filename:
            global video_path, video_width, video_height
            video_path = filename
            video_name = filename.split('/')[-1]
            video_name_label.config(text=video_name)
            add_video_button.config(text='CHANGE VIDEO')
            video_clip = VideoFileClip(video_path)
            video_width = video_clip.w
            video_height = video_clip.h
            width_value.set(video_width)
            height_value.set(video_height)

    window.withdraw()
    window.destroy()

    resize_window = tk.Tk()
    resize_window.title('Trim Video')
    resize_window.geometry('280x240')
    resize_window.resizable(False, False)
    resize_window.configure(background=DARK)

    add_video_button = get_button("add a video", get_video_file, resize_window)
    add_video_button.grid(row=0, column=0, padx=10, pady=(10,5), sticky='we',columnspan=2)
    resize_window.grid_columnconfigure(0, weight=1)
    resize_window.grid_columnconfigure(1, weight=1)

    video_name_label = get_label("No video selected", resize_window)
    video_name_label.grid(row=1, column=0, sticky='we',columnspan=2, pady=(0,25))

    def get_icon(file_name: str):
        return tk.PhotoImage(file=file_name).subsample(26)

    def get_icon_button(icon, command):
        return tk.Button(resize_window, image=icon, width=14, height=18, bg=DARK, fg=LIGHT_GRAY, relief="ridge",
                         command=command, activebackground=DARK, activeforeground=LIGHT_GRAY, bd=0)

    def lock_aspect_ratio():
        global locked_aspect_ratio
        locked_aspect_ratio = not locked_aspect_ratio
        if locked_aspect_ratio:
            lock_button.config(image=lock_icon)
        else:
            lock_button.config(image=unlock_icon)

    lock_icon = get_icon("icons/lock.png")
    unlock_icon = get_icon("icons/unlock.png")
    lock_button = get_icon_button(lock_icon, lock_aspect_ratio)
    lock_button.grid(row=3, column=0, sticky="we", columnspan=2, padx=10)

    width_label = get_label("begin", resize_window)
    width_label.grid(row=2, column=0, sticky="w", padx=10)
    height_label = get_label("end", resize_window)
    height_label.grid(row=2, column=1, sticky="e", padx=10)

    width_value = tk.StringVar(resize_window)
    width_entry = get_entry(resize_window, var=width_value)
    width_entry.grid(row=3, column=0, sticky="w", padx=13)
    width_entry.bind("<KeyRelease>", lambda event: update_height(width_value, height_value))

    height_value = tk.StringVar(resize_window)
    height_entry = get_entry(resize_window, var=height_value)
    height_entry.grid(row=3, column=1, sticky="e", padx=13)
    height_entry.bind("<KeyRelease>", lambda event: update_width(height_value, width_value))

    def replace_main_window():
        resize_window.destroy()
        window.deiconify()

    back_button = get_button("back", replace_main_window, resize_window, height=1)
    back_button.grid(row=4, column=0, sticky="we", padx=10, pady=(50, 0))

    def resize_video():
        if video_path == "":
            messagebox.showerror("Error", "Please select a video first")
            return
        try:
            width = int(width_value.get())
            height = int(height_value.get())
            if width < 0 or height < 0:
                messagebox.showerror("Error", "Please enter a positive value")
                return
            if width == 0 or height == 0:
                messagebox.showerror("Error", "Please enter a non-zero value")
                return
            video = VideoFileClip(video_path)
            video = video.resize((width, height))
            video.write_videofile(os.path.expanduser("~") + f"/videos/{video_path.split('/')[-1]}_resized.mp4")

            messagebox.showinfo("Success", "Video resized successfully")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid value")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Please enter a valid value")

    render_button = get_button("render", command=resize_video, window=resize_window, height=1)
    render_button.grid(row=4, column=1, sticky="we", padx=10, pady=(50, 0))

    resize_window.mainloop()