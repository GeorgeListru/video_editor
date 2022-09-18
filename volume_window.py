from moviepy.audio.fx.volumex import volumex
from moviepy.editor import *
from resources import *
from tkinter import messagebox
import tkinter as tk

video_path = ""


def replace_volume_window(window):
    def get_video_file():
        filename = select_video_file()
        if filename:
            global video_path
            video_path = filename
            video_name = filename.split('/')[-1]
            video_name_label.config(text=video_name)
            add_video_button.config(text='CHANGE VIDEO')

    volume_window = tk.Tk()
    volume_window.title('Add Audio')
    volume_window.geometry('280x240')
    volume_window.resizable(False, False)
    volume_window.configure(background=DARK)
    window.withdraw()

    add_video_button = get_button("add a video", get_video_file, volume_window)
    add_video_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky='we', columnspan=2)

    video_name_label = get_label("No video selected", volume_window)
    video_name_label.grid(row=1, column=0, sticky='we', columnspan=2, pady=(0, 10))

    volume_label = get_label("volume (0 - 100)", volume_window)
    volume_label.grid(row=4, column=0, sticky="w", padx=10, columnspan=2)

    volume_value = tk.StringVar(volume_window, value='50')
    volume_entry = get_entry(volume_window, var=volume_value)
    volume_entry.grid(row=5, column=0, sticky="we", padx=13, columnspan=2)

    volume_value.trace("w", lambda name, index, mode, sv=volume_value: validate_volume(volume_entry, sv))

    volume_window.grid_columnconfigure(1, weight=1)
    volume_window.grid_columnconfigure(0, weight=1)

    def replace_main_window():
        volume_window.destroy()
        window.deiconify()

    back_button = get_button("back", replace_main_window, volume_window, height=1)
    back_button.grid(row=6, column=0, padx=10, sticky="we", pady=(50, 0))

    def change_volume():
        if video_path:
            try:
                video = VideoFileClip(video_path)
                volume = float(volume_value.get()) / 100
                video = video.fx(volumex, volume)
                video.write_videofile(
                    os.path.expanduser("~") + f"/videos/{video_path.split('/')[-1]}_changed_volume.mp4")
                messagebox.showinfo("Success", "Volume changed successfully")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "No video selected")

    render_button = get_button("render", command=change_volume, window=volume_window, height=1)
    render_button.grid(row=6, column=1, padx=10, sticky="we", pady=(50, 0))
