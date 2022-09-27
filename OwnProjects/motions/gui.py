import tkinter
import motions
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

from motions import *
from reading import *
from visualization import *


root = tkinter.Tk()

root.wm_title("Embedding in Tk")

#######################################################

motion = 'linear'
path = 'descriptions.json'
plot_type = 'real'

title, x_label, y_label = read_json_plot_properties(path, motion, plot_type)

dataSet = linear_constant(10, 0, 50)
fig = plt.figure()
fig = figure_settings(title, x_label, y_label)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

#######################################################

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button_quit = tkinter.Button(master=root, text="Quit", command=root.quit)

# required to update canvas and attached toolbar!
canvas.draw()

#def update_frequency(new_val):
#    # retrieve frequency
#    f = float(new_val)
#
#    # update data
#    y = 2 * np.sin(2 * np.pi * f * t)
#    line.set_data(t, y)
#
#    



slider_update = tkinter.Scale(root, from_=1, to=5, orient=tkinter.HORIZONTAL,
                            command = dataSet, label="Frequency [Hz]")

# Packing order is important. Widgets are processed sequentially and if there
# is no space left, because the window is too small, they are not displayed.
# The canvas is rather flexible in its size, so we pack it last which makes
# sure the UI controls are displayed as long as possible.
button_quit.pack(side=tkinter.BOTTOM)
#slider_update.pack(side=tkinter.BOTTOM)
#toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()