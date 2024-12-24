#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class HouseDrawingApp:
    def __init__(self, root):
        self.root = root

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.draw_house()
        self.draw_grass()
        self.draw_sun()

    def draw_grass(self):
        for i in range(0, 400, 10):
            self.canvas.create_arc(
                i, 300, i + 8, 360, fill="green", outline="green", width=2
            )

    def draw_house(self):
        self.canvas.create_rectangle(
            150, 200, 250, 300, fill="lightblue", outline="lightblue"
        )

        self.canvas.create_polygon(
            150, 200, 250, 200, 200, 150, fill="lightblue", outline="lightblue"
        )

    def draw_sun(self):
        self.canvas.create_oval(
            300, 50, 350, 100, fill="yellow", outline="yellow"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = HouseDrawingApp(root)
    root.mainloop()
