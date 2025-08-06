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
        self.file_categories = {
            '📸 Images': [
                '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', 
                '.webp', '.svg', '.ico', '.raw'
            ],
            '📄 Documents': [
                '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt',
                '.xls', '.xlsx', '.ppt', '.pptx', '.csv'
            ],
            '🎬 Videos': [
                '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv',
                '.webm', '.m4v', '.3gp'
            ],
            '🎵 Audio': [
                '.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma',
                '.m4a', '.opus'
            ],
            '📦 Archives': [
                '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
                '.xz', '.tar.gz', '.tar.bz2'
            ],
            '💻 Code': [
                '.py', '.js', '.html', '.css', '.java', '.cpp',
                '.c', '.php', '.rb', '.go', '.rs', '.swift'
            ],
            '⚙️ Programs': [
                '.exe', '.msi', '.deb', '.rpm', '.dmg', '.pkg',
                '.app', '.apk'
            ],
            '📋 Spreadsheets': [
                '.xls', '.xlsx', '.csv', '.ods'
            ],
            '🗂️ Others': []  # Catch-all category
        }

    def create_modern_ui(self):
        self.setup_styles()
        self.create_header()
        self.create_main_content()
        self.create_footer()

    def setup_styles(self):
        style=ttk.style()
        style.theme_use('clam')

        style.configure(
            'Modern.TButton',
            font=('Segon UI',11,'bold'),
            foreground='white',
            background="#16647e"
            borderwidth=0,
            focuscolor='none'
        )

        style.map(
            'Modern.TButton',
            background=[('active','#1e6091')]
        )

        style.configure(
            'Modern.Horizontal.TProgressbar',
            background='#16537e'
            troughcolor='#2d2d44',
            borderwidth=0,
            lightcolor='#16537e',
            darkcolor='#16537e'
        )


    def create_header(self):


    def create_main_content(self):


    def create_footer(self):



def main():
    """Entry point for the application"""
    app = fileOrganizarApp()
    app.run()

if __name__ == "__main__":
    main()