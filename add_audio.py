import os
from moviepy.editor import *
from resources import *
from tkinter import filedialog as fd, messagebox
import tkinter as tk

video_path=""
audio_path=""


def validate_volume(volume_entry, sv):
    if sv.get().isdigit():
        if int(sv.get()) > 100:
            sv.set("100")
    else:
        sv.set("")


def replace_add_audio_window(window):
    window.withdraw()

    def get_video_file():
        filename = select_video_file()
        if filename:
            global video_path
            video_path = filename
            video_name = filename.split('/')[-1]
            video_name_label.config(text=video_name)
            add_video_button.config(text='CHANGE VIDEO')
    def get_audio_file():
        filename = select_audio_file()
        if filename:
            global audio_path
            audio_path = filename
            audio_name = filename.split('/')[-1]
            audio_name_label.config(text=audio_name)
            add_audio_button.config(text='CHANGE AUDIO')

    add_audio_window = tk.Tk()
    add_audio_window.title('Add Audio')
    add_audio_window.geometry('280x360')
    add_audio_window.resizable(False, False)
    add_audio_window.configure(background=DARK)

    add_video_button = get_button("add a video", get_video_file, add_audio_window)
    add_video_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky='we', columnspan=2)
    add_audio_window.grid_columnconfigure(0, weight=1)

    video_name_label = get_label("No video selected", add_audio_window)
    video_name_label.grid(row=1, column=0, sticky='we', columnspan=2, pady=(0, 10))

    add_audio_button = get_button("add audio", get_audio_file, add_audio_window)
    add_audio_button.grid(row=2, column=0, padx=10, pady=(10, 5), sticky='we', columnspan=2)

    audio_name_label = get_label("No audio selected", add_audio_window)
    audio_name_label.grid(row=3, column=0, sticky='we', columnspan=2, pady=(0, 15))

    begin_label = get_label("volume (1-100)", add_audio_window)
    begin_label.grid(row=4, column=0, sticky="w", padx=10)

    volume_value = tk.StringVar()
    volume_entry = get_entry(add_audio_window, placeholder="100", var=volume_value)
    volume_entry.grid(row=5, column=0, sticky="w", padx=13)

    volume_value.trace("w", lambda name, index, mode, sv=volume_value: validate_volume(volume_entry, sv))

    empty_label = get_label("", add_audio_window)
    empty_label.grid(row=5, column=1, sticky='w', pady=(0, 15))

    def replace_main_window():
        add_audio_window.destroy()
        window.deiconify()

    def add_audio():
        if not video_path:
            messagebox.showerror("Error", "No video selected")
            return
        if not audio_path:
            messagebox.showerror("Error", "No audio selected")
            return
        if not volume_value.get():
            messagebox.showerror("Error", "No volume value entered")
            return
        try:
            volume = int(volume_value.get())
        except ValueError:
            messagebox.showerror("Error", "Volume must be a number")
            return
        if volume < 1 or volume > 100:
            messagebox.showerror("Error", "Volume must be between 1 and 100")
            return

        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        audio = audio.volumex(volume/100)
        video = video.set_audio(audio)
        video.write_videofile("output.mp4")
        messagebox.showinfo("Success", "Audio added successfully")


        replace_main_window()

    back_button = get_button("back", replace_main_window, add_audio_window, height=1)
    back_button.grid(row=6, column=0, sticky="we", padx=10, pady=(50, 0))

    render_button = get_button("render", command=add_audio, window=add_audio_window, height=1)
    render_button.grid(row=6, column=1, sticky="we", padx=10, pady=(50, 0))


    add_audio_window.mainloop()


