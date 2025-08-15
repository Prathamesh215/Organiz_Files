import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import threading
import time

class FileOrganizerApp:
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_variables()
        self.setup_file_categories()
        self.create_modern_ui()

    def setup_window(self):
        self.root.title("Organize File")
        self.root.geometry("700x500")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(True, False)
        self.center_window()
        # Robust, cross-platform icon loading
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ico_path = os.path.join(script_dir, 'logo/logo-image.ico')
        png_path = os.path.join(script_dir, 'logo/logo-image.png')
        if sys.platform.startswith('win'):
            try:
                self.root.iconbitmap(ico_path)
            except Exception as e:
                print(f"Icon (.ico) could not be loaded: {e}")
        else:
            try:
                icon = tk.PhotoImage(file=png_path)
                self.root.iconphoto(True, icon)
            except Exception as e:
                print(f"Icon (.png) could not be loaded: {e}")

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_variables(self):
        self.selected_folder = tk.StringVar()
        self.status_text = tk.StringVar(value="Ready to organize your files!")
        self.progress_var = tk.DoubleVar()

    def setup_file_categories(self):
        self.file_categories = {
            '📸 Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.raw'],
            '📄 Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],
            '🎬 Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.3gp'],
            '🎵 Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus'],
            '📦 Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tar.bz2'],
            '💻 Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go', '.rs', '.swift'],
            '⚙️ Programs': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.pkg', '.app', '.apk'],
            '📋 Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
            '🗂️ Others': []
        }

    def create_modern_ui(self):
        self.setup_styles()
        self.create_header()
        self.create_main_content()
        self.create_footer()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Modern.TButton', font=('Segoe UI', 11, 'bold'), foreground='white', background='#16537e', borderwidth=0, focuscolor='none')
        style.map('Modern.TButton', background=[('active', '#1e6091')])
        style.configure('Modern.Horizontal.TProgressbar', background='#16537e', troughcolor='#2d2d44', borderwidth=0, lightcolor='#16537e', darkcolor='#16537e')

    def create_header(self):
        header_frame = tk.Frame(self.root, bg='#1a1a2e')
        header_frame.pack(fill='x', padx=30, pady=(30, 20))
        title_label = tk.Label(header_frame, text="🗂️ File Organization Tool", font=('Segoe UI', 24, 'bold'), fg='#ffffff', bg='#1a1a2e')
        title_label.pack()
        subtitle_label = tk.Label(header_frame, text="Transform chaos into order with a single click", font=('Segoe UI', 12), fg='#a0a0a0', bg='#1a1a2e')
        subtitle_label.pack(pady=(5, 0))

    def create_main_content(self):
        content_frame = tk.Frame(self.root, bg='#1a1a2e')
        content_frame.pack(fill='both', expand=True, padx=30)
        self.create_folder_selection(content_frame)
        self.create_preview_section(content_frame)
        self.create_action_buttons(content_frame)
        self.create_progress_section(content_frame)

    def create_folder_selection(self, parent):
        folder_frame = tk.Frame(parent, bg='#1a1a2e')
        folder_frame.pack(fill='x', pady=(0, 20))
        folder_label = tk.Label(folder_frame, text="Choose a folder to organize:", font=('Segoe UI', 14, 'bold'), fg='#ffffff', bg='#1a1a2e')
        folder_label.pack(anchor='w', pady=(0, 10))
        path_frame = tk.Frame(folder_frame, bg='#1a1a2e')
        path_frame.pack(fill='x')
        self.path_entry = tk.Entry(path_frame, textvariable=self.selected_folder, font=('Segoe UI', 11), bg='#2d2d44', fg='#ffffff', border=0, insertbackground='#ffffff', relief='flat')
        self.path_entry.pack(side='left', fill='x', expand=True, ipady=8)
        browse_btn = ttk.Button(path_frame, text="📁 Browse", style='Modern.TButton', command=self.browse_for_folder)
        browse_btn.pack(side='right', padx=(10, 0))

    def create_preview_section(self, parent):
        preview_frame = tk.Frame(parent, bg='#1a1a2e')
        preview_frame.pack(fill='x', pady=(0, 20))
        preview_label = tk.Label(preview_frame, text="File Preview:", font=('Segoe UI', 14, 'bold'), fg='#ffffff', bg='#1a1a2e')
        preview_label.pack(anchor='w', pady=(0, 10))
        preview_text_frame = tk.Frame(preview_frame, bg='#2d2d44', relief='flat')
        preview_text_frame.pack(fill='both', expand=True)
        self.preview_text = tk.Text(preview_text_frame, height=8, font=('Consolas', 10), bg='#2d2d44', fg='#a0a0a0', border=0, wrap='word', state='disabled')
        self.preview_text.pack(fill='both', expand=True, padx=10, pady=10)
        scrollbar = tk.Scrollbar(preview_text_frame, command=self.preview_text.yview)
        self.preview_text.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

    def create_action_buttons(self, parent):
        button_frame = tk.Frame(parent, bg='#1a1a2e')
        button_frame.pack(fill='x', pady=(0, 20))
        preview_btn = ttk.Button(button_frame, text="👀 Preview Changes", style='Modern.TButton', command=self.preview_organization)
        preview_btn.pack(side='left', expand=True, fill='x', padx=(0, 10))
        organize_btn = ttk.Button(button_frame, text="✨ Organize Files", style='Modern.TButton', command=self.start_organization)
        organize_btn.pack(side='right', expand=True, fill='x', padx=(10, 0))

    def create_progress_section(self, parent):
        progress_frame = tk.Frame(parent, bg='#1a1a2e')
        progress_frame.pack(fill='x', pady=(0, 20))
        self.status_label = tk.Label(progress_frame, textvariable=self.status_text, font=('Segoe UI', 11), fg='#a0a0a0', bg='#1a1a2e')
        self.status_label.pack(anchor='w', pady=(0, 10))
        self.progress_bar = ttk.Progressbar(progress_frame, style='Modern.Horizontal.TProgressbar', variable=self.progress_var, mode='determinate')
        self.progress_bar.pack(fill='x', ipady=4)

    def create_footer(self):
        footer_frame = tk.Frame(self.root, bg='#1a1a2e')
        footer_frame.pack(fill='x', side='bottom', padx=30, pady=(0, 20))
        footer_text = tk.Label(footer_frame, text="Made with ❤️ using Python | Keep your files organized!", font=('Segoe UI', 9), fg='#666666', bg='#1a1a2e')
        footer_text.pack()

    def browse_for_folder(self):
        folder_path = filedialog.askdirectory(title="Select a folder to organize", initialdir=os.path.expanduser("~"))
        if folder_path:
            self.selected_folder.set(folder_path)
            self.update_status(f"Selected: {os.path.basename(folder_path)}")
            self.preview_organization()

    def preview_organization(self):
        folder_path = self.selected_folder.get()
        if not folder_path or not os.path.exists(folder_path):
            self.show_error("Please select a valid folder first!")
            return
        self.update_status("Analyzing files...")
        try:
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        except PermissionError:
            self.show_error("Permission denied! Please choose a different folder.")
            return
        if not files:
            self.update_preview_text("No files found in the selected folder.")
            self.update_status("No files to organize")
            return
        categorized = self.categorize_files(files)
        preview_text = self.generate_preview_text(categorized, len(files))
        self.update_preview_text(preview_text)
        self.update_status(f"Found {len(files)} files ready to organize")

    def categorize_files(self, files):
        categorized = {}
        for filename in files:
            file_ext = Path(filename).suffix.lower()
            category_found = False
            for category, extensions in self.file_categories.items():
                if file_ext in extensions:
                    if category not in categorized:
                        categorized[category] = []
                    categorized[category].append(filename)
                    category_found = True
                    break
            if not category_found:
                if '🗂️ Others' not in categorized:
                    categorized['🗂️ Others'] = []
                categorized['🗂️ Others'].append(filename)
        return categorized

    def generate_preview_text(self, categorized, total_files):
        preview_lines = [
            f"📊 ORGANIZATION PREVIEW",
            f"{'='*50}",
            f"Total files to organize: {total_files}",
            f"Categories found: {len(categorized)}",
            "",
        ]
        for category, files in categorized.items():
            preview_lines.append(f"{category} ({len(files)} files):")
            display_files = files[:3]
            for file in display_files:
                preview_lines.append(f"  • {file}")
            if len(files) > 3:
                preview_lines.append(f"  • ... and {len(files) - 3} more files")
            preview_lines.append("")
        return "\n".join(preview_lines)

    def update_preview_text(self, text):
        self.preview_text.config(state='normal')
        self.preview_text.delete(1.0, tk.END)
        self.preview_text.insert(1.0, text)
        self.preview_text.config(state='disabled')

    def start_organization(self):
        folder_path = self.selected_folder.get()
        if not folder_path or not os.path.exists(folder_path):
            self.show_error("Please select a valid folder first!")
            return
        result = messagebox.askyesno("Confirm Organization", "This will move files into category folders. Continue?", icon='question')
        if result:
            threading.Thread(target=self.organize_files, daemon=True).start()

    def organize_files(self):
        folder_path = self.selected_folder.get()
        try:
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            if not files:
                self.update_status("No files to organize!")
                return
            total_files = len(files)
            self.progress_var.set(0)
            moved_count = 0
            for i, filename in enumerate(files):
                progress = (i / total_files) * 100
                self.progress_var.set(progress)
                self.update_status(f"Processing: {filename}")
                file_ext = Path(filename).suffix.lower()
                destination_category = '🗂️ Others'
                for category, extensions in self.file_categories.items():
                    if file_ext in extensions:
                        destination_category = category
                        break
                dest_folder = os.path.join(folder_path, destination_category)
                os.makedirs(dest_folder, exist_ok=True)
                source_path = os.path.join(folder_path, filename)
                dest_path = os.path.join(dest_folder, filename)
                try:
                    counter = 1
                    original_dest = dest_path
                    while os.path.exists(dest_path):
                        name, ext = os.path.splitext(original_dest)
                        dest_path = f"{name}_{counter}{ext}"
                        counter += 1
                    shutil.move(source_path, dest_path)
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
                time.sleep(0.1)
            self.progress_var.set(100)
            self.update_status(f"✅ Success! Organized {moved_count} files")
            self.root.after(0, lambda: messagebox.showinfo(
                "Organization Complete!",
                f"Successfully organized {moved_count} files into categories!"
            ))
            self.root.after(100, self.preview_organization)
        except Exception as e:
            self.update_status(f"❌ Error: {str(e)}")
            self.root.after(0, lambda: self.show_error(f"Organization failed: {str(e)}"))

    def update_status(self, message):
        self.root.after(0, lambda: self.status_text.set(message))

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def run(self):
        self.root.mainloop()

def main():
    app = FileOrganizerApp()
    app.run()

if __name__ == "__main__":
    main()
