import tkinter as tk
from tkinter import filedialog


class FileDialogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Выбор файла")
        self.root.geometry("500x200")

        self.button = tk.Button(
            root, text="Выбрать файл", command=self.choose_file
        )
        self.button.pack(pady=20)

        self.label = tk.Label(root, text="Файл не выбран", wraplength=450)
        self.label.pack(pady=10)

    def choose_file(self):
        filepath = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Все файлы", "*.*"), ("Python", "*.py"), ("Текст", "*.txt")]
        )
        if filepath:
            self.label.config(text=f"Выбран файл:\n{filepath}")
        else:
            self.label.config(text="Файл не выбран")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileDialogApp(root)
    root.mainloop()