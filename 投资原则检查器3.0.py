import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk, ImageDraw, ImageFont
import random

class InvestmentPrincipleChecker:
    def __init__(self, master):
        self.master = master
        self.master.title("投资原则检查器")
        self.master.geometry("500x400")
        self.master.configure(bg="#F0F4F8")  # 浅蓝灰背景色

        self.principles = [
            "要谋定而后动",
            "控制风险",
            "长期投资",
            "分散投资",
            "了解自己的投资",
        ]
        self.checked_principles = [None] * len(self.principles)

        self.setup_fonts()
        self.create_widgets()

        self.current_principle = -1

    def setup_fonts(self):
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.principle_font = font.Font(family="Helvetica", size=14)
        self.button_font = font.Font(family="Helvetica", size=12)
        self.progress_font = font.Font(family="Helvetica", size=10)

    def create_widgets(self):
        title_label = tk.Label(self.master, text="投资原则检查器", font=self.title_font, bg="#F0F4F8", fg="#2C3E50")
        title_label.pack(pady=20)

        self.principle_label = tk.Label(self.master, text="", wraplength=400, font=self.principle_font, bg="#F0F4F8", fg="#34495E")
        self.principle_label.pack(pady=20)

        button_frame = tk.Frame(self.master, bg="#F0F4F8")
        button_frame.pack(pady=10)

        self.yes_button = self.create_button(button_frame, "已完成", "#27AE60", lambda: self.check_principle(True))
        self.no_button = self.create_button(button_frame, "未完成", "#E74C3C", lambda: self.check_principle(False))

        self.invest_button = tk.Button(self.master, text="开始投资检查", command=self.start_check,
                                       font=self.button_font, bg="#3498DB", fg="white", 
                                       activebackground="#2980B9", activeforeground="white",
                                       relief=tk.FLAT, padx=20, pady=10)
        self.invest_button.pack(pady=20)

        self.progress_label = tk.Label(self.master, text="", font=self.progress_font, bg="#F0F4F8", fg="#7F8C8D")
        self.progress_label.pack()

    def create_button(self, parent, text, color, command):
        button = tk.Button(parent, text=text, command=command, 
                           font=self.button_font, bg=color, fg="white",
                           activebackground=color, activeforeground="white",
                           relief=tk.FLAT, padx=20, pady=10)
        button.pack(side=tk.LEFT, padx=10)
        return button

    def start_check(self):
        self.current_principle = 0
        self.show_principle()

    def show_principle(self):
        if self.current_principle < len(self.principles):
            self.principle_label.config(text=self.principles[self.current_principle])
            self.yes_button.config(state=tk.NORMAL)
            self.no_button.config(state=tk.NORMAL)
            self.update_progress()
        else:
            self.finish_check()

    def check_principle(self, completed):
        self.checked_principles[self.current_principle] = completed
        self.current_principle += 1
        self.show_principle()

    def update_progress(self):
        completed = sum(1 for p in self.checked_principles if p is True)
        total = len(self.principles)
        self.progress_label.config(text=f"进度: {completed}/{total}")

    def finish_check(self):
        if all(self.checked_principles):
            self.show_fireworks()
        else:
            unchecked = [self.principles[i] for i, checked in enumerate(self.checked_principles) if not checked]
            messagebox.showwarning("警告", f"您还没有完成以下原则的检查：\n{', '.join(unchecked)}\n\n只有做好全部的准备才能够做好投资。")

    def show_fireworks(self):
        fireworks_window = tk.Toplevel(self.master)
        fireworks_window.title("祝贺")
        fireworks_window.geometry("400x300")
        fireworks_window.configure(bg="#F0F4F8")

        canvas = tk.Canvas(fireworks_window, width=400, height=200, bg="#F0F4F8", highlightthickness=0)
        canvas.pack(pady=20)

        for _ in range(50):
            x, y = random.randint(0, 400), random.randint(0, 200)
            color = random.choice(["#3498DB", "#E74C3C", "#2ECC71", "#F1C40F", "#9B59B6"])
            canvas.create_oval(x, y, x+5, y+5, fill=color, outline=color)

        label = tk.Label(fireworks_window, text="你现在可以去执行了，\n无论结果怎么样，你都是对的！", 
                         font=self.principle_font, bg="#F0F4F8", fg="#2C3E50")
        label.pack()

root = tk.Tk()
app = InvestmentPrincipleChecker(root)
root.mainloop()
