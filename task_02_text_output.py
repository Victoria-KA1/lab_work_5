import tkinter as tk


class TextOutputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовое поле")
        self.root.geometry("400x200")

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=20)

        self.button = tk.Button(
            root, text="Показать текст", command=self.show_text
        )
        self.button.pack(pady=5)

        self.label = tk.Label(root, text="", font=("Arial", 12))
        self.label.pack(pady=10)

    def show_text(self):
        text = self.entry.get()
        if text:
            self.label.config(text=f"Вы ввели: {text}")
        else:
            self.label.config(text="Поле пустое")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextOutputApp(root)
    root.mainloop()