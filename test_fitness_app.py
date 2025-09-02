import pytest
import tkinter as tk
from unittest.mock import patch, MagicMock
from ACEest_Fitness import FitnessTrackerApp  # replace with actual filename

@pytest.fixture
def app():
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    yield app
    root.destroy()  # close the window after test

def test_add_workout_success(app):
    app.workout_entry.insert(0, "Pushups")
    app.duration_entry.insert(0, "30")

    with patch("tkinter.messagebox.showinfo") as mock_info:
        app.add_workout()
        assert len(app.workouts) == 1
        assert app.workouts[0]["workout"] == "Pushups"
        assert app.workouts[0]["duration"] == 30
        mock_info.assert_called_once()

def test_add_workout_missing_fields(app):
    app.workout_entry.delete(0, tk.END)
    app.duration_entry.delete(0, tk.END)

    with patch("tkinter.messagebox.showerror") as mock_error:
        app.add_workout()
        assert len(app.workouts) == 0
        mock_error.assert_called_once_with("Error", "Please enter both workout and duration.")

def test_add_workout_invalid_duration(app):
    app.workout_entry.insert(0, "Running")
    app.duration_entry.insert(0, "abc")  # invalid duration

    with patch("tkinter.messagebox.showerror") as mock_error:
        app.add_workout()
        assert len(app.workouts) == 0
        mock_error.assert_called_once_with("Error", "Duration must be a number.")

def test_view_workouts_with_entries(app):
    app.workouts = [
        {"workout": "Situps", "duration": 20},
        {"workout": "Jogging", "duration": 40}
    ]
    expected_msg = "Logged Workouts:\n1. Situps - 20 minutes\n2. Jogging - 40 minutes\n"

    with patch("tkinter.messagebox.showinfo") as mock_info:
        app.view_workouts()
        mock_info.assert_called_once_with("Workouts", expected_msg)

def test_view_workouts_empty(app):
    app.workouts = []

    with patch("tkinter.messagebox.showinfo") as mock_info:
        app.view_workouts()
        mock_info.assert_called_once_with("Workouts", "No workouts logged yet.")
