import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")  # обычный запуск

    return os.path.join(base_path, relative_path)
