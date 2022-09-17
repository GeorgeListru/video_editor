import tkinter as tk
from tkinter import filedialog as fd
DARK = '#27272E'
LIGHT_GRAY = '#D9D9D9'
DARK_GRAY = '#3D3D44'
BLACK = "#000000"
WHITE = "#FFFFFF"

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='gray', **kwargs):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = kwargs.get('fg', 'black')
        self['bg'] = kwargs.get('bg')
        self['font'] = kwargs.get('font')
        self['fg'] = kwargs.get('fg', 'black')

        self['highlightbackground'] = kwargs.get('bg')
        self['highlightcolor'] = kwargs.get('bg')
        self['highlightthickness'] = 1
        self["borderwidth"] = kwargs.get('borderwidth')
        self["textvariable"] = kwargs.get('textvariable')

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

def convert_to_seconds(time):
    time = time.split(":")
    seconds = 0
    for i in range(len(time)):
        seconds += int(time[i]) * (60**(len(time)-i-1))
    return seconds

def select_video_file():
    filetypes = (
        ('video files', '*.mp4'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    return filename
def select_audio_file():
    filetypes = (
        ('audio files', '*.mp3'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    return filename

def get_button(text: str, command, window, height=2):
    return tk.Button(window, text=text, height=height, bg=LIGHT_GRAY, fg=BLACK, relief="ridge", command=command, font=('Arial', 10, "bold"))
def get_label(text: str,window):
    return tk.Label(window, text=text, font=('Arial', 10, "bold"), fg=WHITE, bg=DARK)
def get_placeholder_entry(window, placeholder, var):
    return EntryWithPlaceholder(window, placeholder=placeholder,textvariable=var, font=('Arial', 10, "bold"), fg=WHITE, bg=DARK_GRAY, relief="ridge", borderwidth=0)
def get_entry(window, var):
    return tk.Entry(window, textvariable=var, font=('Arial', 10, "bold"), fg=WHITE, bg=DARK_GRAY, relief="ridge", borderwidth=0)

