#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class TextToListApp:
    def __init__(self, root):
        self.root = root

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_to_list)

        self.listbox = tk.Listbox(root, width=40, height=15)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", self.copy_to_entry)

    def add_to_list(self, event):
        text = self.entry.get().strip()
        if text:
            self.listbox.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def copy_to_entry(self, event):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            text = self.listbox.get(selected_item_index)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextToListApp(root)
    root.mainloop()
