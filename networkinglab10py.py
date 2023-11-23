# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:17:29 2023

@author: Phuc Anh
"""

import tkinter as tk

import random

import time

import threading

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

 

# Generator functions

def generator_x():

    return random.random()

 

def generator_y(x):

    return 10 * x + 20

 

class Display:

    def __init__(self, root):

        # ... (rest of the __init__ method remains the same)

 

        # Initialize data

        self.data = []

        self.x_data = []

 

        # Initialize figure and axis for line chart and bar chart

        self.fig = plt.Figure(figsize=(5, 4), dpi=100)

        self.ax = self.fig.add_subplot(111)

        self.ax.set_title("Temperature Daily")

        self.ax.set_ylim([0, 35])

        self.ax.set_xticks([])  # No initial x ticks

 

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

        while True:  # Infinite loop for continuous updates

            # Generate new data point

            new_x_data = generator_x()

            new_y_data = generator_y(new_x_data)

 

            # Update dataset

            self.data.append(new_y_data)

            self.x_data.append(len(self.x_data) + 1)  # Incremental x values

 

            # Update combined chart

            self.ax.clear()

            self.ax.plot(self.x_data, self.data, label='Line Chart', color='lightblue')

            self.ax.bar(self.x_data, self.data, label='Bar Chart', color='pink', alpha=0.5)

            self.ax.set_title("Temperature Daily")

            self.ax.set_ylim([0, 35])

 

            # Adjust x ticks dynamically

         #   if len(self.x_data) <= 10:
#
 #               self.ax.set_xticks(self.x_data)
#
 #           else:
#
 #               self.ax.set_xticks(np.arange(len(self.x_data) - 9, len(self.x_data) + 1, 1))

 

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
