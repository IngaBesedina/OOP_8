#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class ResizableTextApp:
    def __init__(self, root):
        self.root = root

        self.width_label = tk.Label(root, text="Ширина:")
        self.width_label.pack()

        self.width_entry = tk.Entry(root, width=10)
        self.width_entry.pack(pady=2)
        self.width_entry.bind("<Return>", self.resize_text)

        self.height_label = tk.Label(root, text="Высота:")
        self.height_label.pack()

        self.height_entry = tk.Entry(root, width=10)
        self.height_entry.pack()
        self.height_entry.bind("<Return>", self.resize_text)

        self.resize_button = tk.Button(
            root, text="Изменить", command=self.resize_text
        )
        self.resize_button.pack()

        self.text = tk.Text(root, bg="lightgrey", wrap=tk.WORD)
        self.text.pack(padx=10, pady=10)

        self.text.bind("<FocusIn>", lambda event: self.text.config(bg="white"))
        self.text.bind(
            "<FocusOut>", lambda event: self.text.config(bg="lightgrey")
        )

    def resize_text(self, event=None):
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            self.text.config(width=width, height=height)
        except ValueError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ResizableTextApp(root)
    root.mainloop()
