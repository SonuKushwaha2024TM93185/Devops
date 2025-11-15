# tests/test_gui.py
import tkinter as tk
import importlib

# replace ACEst_FitnessV121 with your module name that contains the TrackerApp class
mod = importlib.import_module("ACEst_FitnessV121")

def test_gui_creates_main_window():
    root = tk.Tk()
    root.withdraw()             # hide the window in tests
    app = mod.TrackerApp(root)  # or class name used in your file
    assert hasattr(app, 'master')
    # check presence of some widget you created
    # e.g. if you created a Entry named exercise_entry:
    assert hasattr(app, 'exercise_entry')
    root.destroy()

