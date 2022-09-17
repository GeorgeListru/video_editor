import tkinter as tk
from trim_window import replace_trim_window
from add_audio_window import replace_add_audio_window
from resources import *

def initialize_main_window():
    window = tk.Tk()
    window.title('Video Editor')
    window.geometry('705x135')
    window.resizable(False, False)

    window.configure(background=DARK)

    def get_icon(file_name: str):
        return tk.PhotoImage(file=file_name).subsample(16)
    def get_icon_button(icon, command):
        return tk.Button(window, image=icon, width=85, height=85, bg=LIGHT_GRAY, fg=BLACK, relief="ridge", command=command)
    def get_icon_label(text: str):
        return tk.Label(window, text=text, font=('Arial', 10, "bold"), fg=LIGHT_GRAY, bg=DARK)

    trim_icon = get_icon('icons/trim.png')
    trim_button = get_icon_button(trim_icon, lambda: replace_trim_window(window)).grid(row=0, column=0, padx=25, pady=(20, 0))
    trim_text = get_icon_label('TRIM').grid(row=1, column=0)

    add_sound_icon = get_icon('icons/add_sound.png')
    add_sound_button = get_icon_button(add_sound_icon, lambda: replace_add_audio_window(window)).grid(row=0, column=1, padx=25, pady=(20,0))
    add_sound_text = get_icon_label('ADD SOUND').grid(row=1, column=1)

    speed_icon = get_icon('icons/speed.png')
    speed_button = get_icon_button(speed_icon, lambda: print('speed')).grid(row=0, column=2, padx=25, pady=(20,0))
    speed_text = get_icon_label('SPEED').grid(row=1, column=2)

    volume = get_icon('icons/volume.png')
    volume_button = get_icon_button(volume, lambda: print('volume')).grid(row=0, column=3, padx=25, pady=(20,0))
    volume_text = get_icon_label('VOLUME').grid(row=1, column=3)

    resize = get_icon('icons/resize.png')
    resize_button = get_icon_button(resize, lambda: print('resize')).grid(row=0, column=4, padx=25, pady=(20,0))
    resize_text = get_icon_label('RESIZE').grid(row=1, column=4)

    window.mainloop()

initialize_main_window()