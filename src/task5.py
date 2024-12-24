#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class Ball:
    def __init__(self, root) -> None:
        self.root = root

        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="white")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(180, 140, 220, 180, fill="green")

        self.canvas.bind("<Button-1>", self.move_ball)

    def move_ball(self, event):
        target_x, target_y = event.x, event.y
        self.move_to(target_x, target_y)

    def move_to(self, target_x, target_y):
        current_coords = self.canvas.coords(self.ball)
        current_x = (current_coords[0] + current_coords[2]) / 2
        current_y = (current_coords[1] + current_coords[3]) / 2

        dx = target_x - current_x
        dy = target_y - current_y
        step_x = dx / 50
        step_y = dy / 50

        if abs(dx) > 1 or abs(dy) > 1:
            self.canvas.move(self.ball, step_x, step_y)
            root.after(10, self.move_to, target_x, target_y)


if __name__ == "__main__":
    root = tk.Tk()
    ball = Ball(root)
    root.mainloop()
