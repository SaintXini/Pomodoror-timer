import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style


# establecer el tiempo predeterminado para los intervalos de trabajo y descanso
WORK_INTERVAL = 25 * 60  # 25 minutos
SHORT_BREAK_INTERVAL = 5 * 60   # 5 minutos
LONG_BREAK_INTERVAL = 15 * 60   # 15 minutos


class PomodoroTimer:
    def __init__(self):
        self.root = tk.tk()
        self.root.geometry("200x200")
        self.root.title("Pomodoro Timer")
        self.style = Style(theme="simplex")
        self.style.theme_use()