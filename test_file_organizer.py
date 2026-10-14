from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from file_organizer import get_category, get_unique_path, organize_files

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp_dir.name)
    def tearDown(self):
        self.temp_dir.cleanup()

    def test_identifies_image_categories(self):
        self.assertEqual(
            get_category(Path("photo.PNG")),
            "Images"
        )

    def test_unknown_extensions_geos_to_others(self):
        self.assertEqual(
            get_category(Path("file.xyz")),
            "Others"
        )

    def test_avoids_duplicate_file_names(self):
        destination = self.folder / "report.txt"
        destination.write_text("Existing file", encoding="utf-8")

        new_path = get_unique_path(destination)

        self.assertEqual(new_path.name, "report_1.txt")
        self.assertFalse(new_path.exists())

    def test_organizes_files_after_confirmation(self):
        python_file = self.folder / "example.py"
        text_file = self.folder / "notes.txt"

        python_file.write_text("print('Hello')", encoding="utf-8")
        text_file.write_text("Test document", encoding="utf-8")

        with patch("builtins.input", return_value="y"):
            with patch("builtins.print"):
                organize_files(self.folder)

        self.assertTrue((self.folder / "Code" / "example.py").exists())
        self.assertTrue((self.folder / "Documents" / "notes.txt").exists())

        self.assertFalse(python_file.exists())
        self.assertFalse(text_file.exists())

    def test_cancel_keeps_original_files(self):
        python_file = self.folder / "example.py"
        python_file.write_text("print('Hello')", encoding="utf-8")

        with patch("builtins.input", return_value="n"):
            with patch("builtins.print"):
                organize_files(self.folder)

        self.assertTrue(python_file.exists())
        self.assertFalse((self.folder / "Code").exists())

    def test_empty_folder_does_not_move_files(self):
        with patch("builtins.print"):
            organize_files(self.folder)

        self.assertEqual(list(self.folder.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
