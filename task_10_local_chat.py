import tkinter as tk


class ChatWindow:
    def __init__(self, root, username, other_window):
        self.root = root
        self.username = username
        self.other_window = other_window

        self.root.title(f"Чат — {username}")
        self.root.geometry("350x450")

        self.chat_log = tk.Text(root, state="disabled", wrap="word")
        self.chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(padx=10, pady=5, fill=tk.X)

        self.entry = tk.Entry(self.entry_frame)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", lambda event: self.send_message())

        self.button = tk.Button(
            self.entry_frame, text="Отправить", command=self.send_message
        )
        self.button.pack(side=tk.RIGHT, padx=5)

    def send_message(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.entry.delete(0, tk.END)

        message = f"{self.username}: {text}\n"
        self.append_to_log(self.chat_log, message)
        if self.other_window:
            self.append_to_log(self.other_window.chat_log, message)

    @staticmethod
    def append_to_log(widget, text):
        widget.config(state="normal")
        widget.insert(tk.END, text)
        widget.see(tk.END)
        widget.config(state="disabled")


def main():
    root1 = tk.Tk()
    root2 = tk.Toplevel()

    window1 = ChatWindow(root1, "Пользователь А", None)
    window2 = ChatWindow(root2, "Пользователь Б", None)

    window1.other_window = window2
    window2.other_window = window1

    root1.mainloop()


if __name__ == "__main__":
    main()