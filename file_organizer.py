import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import threading
import time
from datetime import datetime
class fileOrganizarApp:
    def __init__(self):
        self.root=tk.Tk()
        self.setup_window()
        self.setup_variables()
        self.setup_file_catagories()
        self.setup_modern_ui()

    def setup_window(self):
        self.root.title("File oraganizer")
        self.root.geometry("600x500")
        self.root.configure(bg="#00000000")
        self.root.resizable(True,False)

        self.center_window()

        if sys.platform.startswith('win'):
            self.root.iconbitmap('logo-image.ico')

        else:
            try:
                icon=tk.PhotoImage(file='logo-image.png')
                self.root.iconphoto(True, icon)
            except Exception as e:
                print("Icon could not be loaded:",e)

    def center_window(self):
        self.root.update_idletasks()
        width=self.root.winfo_width()
        height=self.root.winfo_height()
        x=(self.root.winfo_screenwidth()//2)-(width//2)
        y=(self.root.winfo_screenheight()//2)-(height//2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_variable(self):
        self.selected_folder=tk.StringVar()
        self.status_text=tk.StringVar()
        self.status_text.set("Ready to organize your files!")
        self.progress_var=tk.DoubleVar()

    def setup_file_catagories(self):

