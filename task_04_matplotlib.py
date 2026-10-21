import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math


class PlotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("График внутри Tkinter")
        self.root.geometry("600x500")

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        x_values = [i / 10 for i in range(-50, 51)]
        y_values = [math.sin(x) for x in x_values]
        self.ax.plot(x_values, y_values, color="blue")
        self.ax.set_title("y = sin(x)")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.button = tk.Button(
            root, text="Обновить график", command=self.redraw
        )
        self.button.pack(pady=5)

    def redraw(self):
        self.ax.clear()
        x_values = [i / 10 for i in range(-50, 51)]
        y_values = [math.cos(x) for x in x_values]
        self.ax.plot(x_values, y_values, color="red")
        self.ax.set_title("y = cos(x)")
        self.ax.grid(True)
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = PlotApp(root)
    root.mainloop()