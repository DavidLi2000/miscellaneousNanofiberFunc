import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def od_function(x, a):
    return np.exp(-a/(1+4*(x**2/(2*np.pi*5.7))))
def plot_function_with_variable(a):
    x = np.linspace(-60, 60, 100)
    y = od_function(x, a)

    fig = Figure(figsize=(10, 6), dpi=100)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'OD Function')
    ax.grid(True)
    x_ticks = np.linspace(-60, 60, 25)  # Set 11 evenly spaced x-axis ticks
    ax.set_xticks(x_ticks)

    return fig

def update_plot(a):
    a = float(a)  # Convert the 'a' value to a float
    fig = plot_function_with_variable(a)
    canvas.figure = fig
    canvas.draw()

if __name__ == "__main__":
    plt.ion()  # Enable interactive mode

    root = tk.Tk()
    root.title("Quadratic Function Plot")

    a_slider = tk.Scale(root, label='OD:', from_=1, to=600, resolution=1, orient='horizontal',length=300, command=update_plot)
    a_slider.set(1.0)
    a_slider.pack()

    fig = plot_function_with_variable(a_slider.get())
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    def update_canvas():
        a = a_slider.get()
        update_plot(a)
        root.after(100, update_canvas)

    root.after(100, update_canvas)
    root.mainloop()
