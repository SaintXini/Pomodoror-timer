import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style


# establecer el tiempo predeterminado para los intervalos de trabajo y descanso
WORK_TIME = 25 * 60  # 25 minutos
SHORT_BREAK_TIME = 5 * 60   # 5 minutos
LONG_BREAK_TIME = 15 * 60   # 15 minutos


class PomodoroTimer:
    def __init__(self):
        self.root = tk.tk()
        self.root.geometry("200x200")
        self.root.title("Pomodoro Timer")
        self.style = Style(theme="simplex")
        self.style.theme_use()

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        
        self.stop_button.pack(pady=5)

        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()
    
    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Great Job!" if self.pomodoros_completed % 4 == 0 else "Time for a Break!", f"You've completed {self.pomodoros_completed} pomodoros!")
                    if self.pomodoros_completed % 4 == 0:
                        messagebox.showinfo("Great Job!", "You've completed 4 pomodoros! Take a long break!")
                    else:
                        messagebox.showinfo("Time for a Break!", "Take a short break! and stretch your legs!")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo("Break Over!", "Time to get back to work!")