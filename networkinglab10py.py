# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 01:29:17 2023

@author: Huyen Anh
"""

import tkinter as tk
import random
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# USE THE PART A FOR THE BASE PLOTS AND ADD DYNAMICAL DISPLAY FUNCTION
# create a uniform random x values
def generator_x():
  return random.random()

# set y = mx + c
def generator_y(x):
    return 10 * x + 20

# number of values created
data_nums = 11

# generate x values first
x_data = [generator_x() for _ in range(data_nums)]

# create the axis X value:
days_data = list(range(data_nums))

# initialize y data:
y_data = []

# generate y values based on x values
for x in x_data:
    y = generator_y(x)
    y_data.append(y)

# DYNAMICAL DISPLAY
class Display:
    def __init__(self, root):
        self.root = root
        self.root.title("Average Temperature in Vietnam")

        # Initialize data
        self.data = []
        self.x_data = []
        # assign the first 5 values
        for i in range(5):
            self.data.append(y_data.pop(0))
            self.x_data.append(days_data.pop(0))

        # Initialize figure and axis for line chart and bar chart
        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Temparature Daily")
        self.ax.set_ylim([0, 35])
        self.ax.set_xticks(np.arange(min(self.x_data), max(self.x_data) + 1, 1))

        self.line_chart = FigureCanvasTkAgg(self.fig, master=root)
        self.line_chart.get_tk_widget().grid(row=0, column=0)

        # Initialize button
        self.go_button = tk.Button(root, text="Start", command=self.initUI)
        self.go_button.grid(row=1, column=0, columnspan=2)

        # Initialize thread for updating data
        self.update_thread = None

    def initUI(self):
        self.update_thread = threading.Thread(target=self.update_values)
        self.update_thread.daemon = True
        self.update_thread.start()

    def update_values(self):
        while y_data != []:
            # Generate new data and update dataset
            new_data = y_data.pop(0)
            self.data.append(new_data)
            self.data.pop(0)

            new_x_data = days_data.pop(0)
            self.x_data.append(new_x_data)
            self.x_data.pop(0)

            # Update combined chart
            self.ax.clear()
            self.ax.plot(self.x_data, self.data, label='Line Chart', color='lightblue')
            self.ax.bar(self.x_data, self.data, label='Bar Chart', color='pink', alpha=0.5)
            self.ax.set_title("Temparature Daily")
            self.ax.set_ylim([0, 35])
            self.ax.set_xticks(np.arange(min(self.x_data), max(self.x_data) + 1, 1))
            self.ax.legend()

            self.line_chart.draw()

            # Sleep for a short while (0.5 of a second)
            time.sleep(0.5)

    def stop_update_thread(self):
        if self.update_thread is not None:
            self.update_thread.stop()
            self.update_thread = None


if __name__ == '__main__':
    root = tk.Tk()
    app = Display(root)
    root.mainloop()
