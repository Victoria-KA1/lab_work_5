import tkinter as tk
from tkinter import ttk


class ProgressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Прогрессбар")
        self.root.geometry("400x150")

        self.progress = ttk.Progressbar(
            root, orient="horizontal", length=300, mode="determinate"
        )
        self.progress.pack(pady=20)

        self.button = tk.Button(root, text="Запустить", command=self.start_progress)
        self.button.pack(pady=5)

        self.label = tk.Label(root, text="0%")
        self.label.pack()

    def start_progress(self):
        self.progress["value"] = 0
        self.update_progress()

    def update_progress(self):
        current = self.progress["value"]
        if current < 100:
            self.progress["value"] = current + 5
            self.label.config(text=f"{int(self.progress['value'])}%")
            self.root.after(100, self.update_progress)
        else:
            self.label.config(text="Готово!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressApp(root)
    root.mainloop()