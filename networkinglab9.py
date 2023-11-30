# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:30:21 2023

@author: Phuc Anh
"""

import random
import tkinter as tk

class DataGenerator(tk.Tk):
    def __init__(self, n=20):
        super().__init__()
        self.generated_data = self.data_in_range(n)
        self.initUI()

    def data_in_range(self, n):
        return [random.uniform(950, 1030) for _ in range(n)]

    def initUI(self):
        # Window properties
        self.geometry("600x500")
        self.title("Historical Data")
        self["bg"] = "white"
        # Grid
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=3)
        # Variables
        self.input_value = tk.IntVar()
        # Canvas
        self.my_canvas = tk.Canvas(width=400, height=300, bg="white")
        self.my_canvas.grid(column=1, row=3, pady=50)

        # Commands
        def generateChart():
            print(self.generated_data)
            self.my_canvas.delete("all")
            self.data_range_label.destroy()
            self.data_range_label = tk.Label(
                self,
                text=f"Data range: {self.input_value.get()}-{self.input_value.get() + 5}",
                font=("Arial", 15),
                width=30,
                bg="white",
            )
            self.data_range_label.grid(column=0, row=1)
            draw_chart(self.input_value.get())

        def draw_chart(input_value):
            x_coord = 50
            old_x_coord = 0
            old_y2 = 0
            bar_thickness = 30
            bar_gap = 5
            line_gap = 5
            height = 300
            input_data = self.generated_data[input_value : input_value + 6]
            max_value = max(input_data)  # Find the maximum value in the current range

            # rescale the range to fit within the box nicely
            for x, y in enumerate(input_data):
                x1 = x_coord
                x2 = x_coord + bar_thickness
                y1 = height
                y2 = height - (y - 950) / (max_value - 950) * 250  # Adjusted to fit within the box
                self.my_canvas.create_rectangle(x1, y1, x2, y2, fill="lightgreen")
                if x != 0:
                    self.my_canvas.create_line(
                        old_x_coord + line_gap,
                        old_y2,
                        x2 - ((bar_gap + bar_thickness) / 2),
                        y2,
                        fill="red",
                        width=3,
                    )
                x_coord += bar_thickness + bar_gap
                old_x_coord = x_coord - bar_thickness + bar_gap
                old_y2 = y2

            # Add grid lines
            for scale_value in range(0, 300, 50):
                # Horizontal grid lines
                self.my_canvas.create_line(
                    50, height - scale_value, x_coord, height - scale_value, fill="lightgray"
                )

            # Add scale markings
            scale_interval = 10  # Adjusted scale interval to 10
            for scale_value in range(950, 1031, scale_interval):
                self.my_canvas.create_line(
                    5,
                    height - (scale_value - 950) / (max_value - 950) * 250,
                    15,
                    height - (scale_value - 950) / (max_value - 950) * 250,
                    fill="black",
                )

            # Add scale labels
            for scale_label in range(950, 1031, scale_interval):
                self.my_canvas.create_text(
                    25,
                    height - (scale_label - 950) / (max_value - 950) * 250,
                    anchor=tk.W,
                    text=str(scale_label),
                )

        # Labels
        self.data_range_entrylabel = tk.Label(
            self, text="Data range", font=("Arial", 15), width=15, bg="white"
        )
        self.data_range_label = tk.Label(
            self,
            text=f"Data range: {self.input_value.get()}-{self.input_value.get() + 5}",
            font=("Arial", 15),
            width=30,
            bg="white",
        )
        self.data_range_entrylabel.grid(column=0, row=0, padx=25)
        self.data_range_label.grid(column=0, row=1)
        # Entry
        self.input_range = tk.Entry(self, textvariable=self.input_value)
        self.input_range.grid(column=1, row=0, padx=50)
        # Button
        self.go_button = tk.Button(
            self, text="GO", width=30, command=generateChart
        )
        self.go_button.grid(column=2, row=0)

if __name__ == "__main__":
    valuesList = []
    gen = DataGenerator()
    gen.mainloop()
