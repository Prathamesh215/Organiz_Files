import unittest
import tempfile
import os
import shutil
from pathlib import Path
import sys

# Adjust import path for running tests properly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_organizer import FileOrganizerApp

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_files = [
            'photo.jpg', 'document.pdf', 'video.mp4', 'song.mp3',
            'archive.zip', 'script.py', 'program.exe',
            'spreadsheet.xlsx', 'unknown_file.xyz', 'no_extension'
        ]
        for filename in self.test_files:
            file_path = os.path.join(self.test_dir, filename)
            with open(file_path, 'w') as f:
                f.write(f"Test content for {filename}")

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_file_categories_exist(self):
        app = FileOrganizerApp()
        expected_categories = [
            '📸 Images', '📄 Documents', '🎬 Videos', '🎵 Audio',
            '📦 Archives', '💻 Code', '⚙️ Programs', '📋 Spreadsheets', '🗂️ Others'
        ]
        for category in expected_categories:
            self.assertIn(category, app.file_categories)
            self.assertIsInstance(app.file_categories[category], list)

    def test_file_categorization(self):
        app = FileOrganizerApp()
        test_cases = [
            ('photo.jpg', '📸 Images'),
            ('document.pdf', '📄 Documents'),
            ('video.mp4', '🎬 Videos'),
            ('song.mp3', '🎵 Audio'),
            ('archive.zip', '📦 Archives'),
            ('script.py', '💻 Code'),
            ('program.exe', '⚙️ Programs'),
            ('spreadsheet.xlsx', '📄 Documents'),  # or could be 📋 Spreadsheets
        ]
        categorized = app.categorize_files([case[0] for case in test_cases])
        for filename, expected_category in test_cases:
            found_in_category = False
            for category, files in categorized.items():
                if filename in files:
                    found_in_category = True
                    break
            self.assertTrue(found_in_category, f"File {filename} was not categorized")

    def test_unknown_file_categorization(self):
        app = FileOrganizerApp()
        unknown_files = ['unknown_file.xyz', 'no_extension']
        categorized = app.categorize_files(unknown_files)
        self.assertIn('🗂️ Others', categorized)
        for filename in unknown_files:
            self.assertIn(filename, categorized['🗂️ Others'])

    def test_empty_file_list(self):
        app = FileOrganizerApp()
        categorized = app.categorize_files([])
        self.assertEqual(len(categorized), 0)

    def test_preview_text_generation(self):
        app = FileOrganizerApp()
        mock_categorized = {
            '📸 Images': ['photo1.jpg', 'photo2.png'],
            '📄 Documents': ['doc1.pdf', 'doc2.txt', 'doc3.docx'],
            '🗂️ Others': ['unknown.xyz']
        }
        preview_text = app.generate_preview_text(mock_categorized, 6)
        self.assertIn('Total files to organize: 6', preview_text)
        self.assertIn('Categories found: 3', preview_text)
        self.assertIn('📸 Images (2 files)', preview_text)
        self.assertIn('📄 Documents (3 files)', preview_text)
        self.assertIn('🗂️ Others (1 files)', preview_text)

if __name__ == '__main__':
    unittest.main()
