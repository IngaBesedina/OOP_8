#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class ShoppingListApp:
    def __init__(self, root) -> None:
        self.root = root

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.listbox_products = tk.Listbox(
            self.frame, selectmode=tk.EXTENDED, width=30, height=15
        )
        self.listbox_products.pack(side=tk.LEFT, padx=5, pady=5)

        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_to_purchases = tk.Button(
            self.button_frame, text="-->", command=self.move_to_purchases
        )
        self.btn_to_purchases.pack(pady=5)

        self.btn_to_products = tk.Button(
            self.button_frame, text="<--", command=self.move_to_products
        )
        self.btn_to_products.pack(pady=5)

        self.listbox_purchases = tk.Listbox(
            self.frame, selectmode=tk.EXTENDED, width=30, height=15
        )
        self.listbox_purchases.pack(side=tk.LEFT, padx=5, pady=5)

        self.products = [
            "apple",
            "bananas",
            "carrot",
            "bread",
            "butter",
            "meat",
            "potato",
            "pineapple",
            "tomato",
            "milk",
        ]
        self.populate_products()

    def populate_products(self):
        for product in self.products:
            self.listbox_products.insert(tk.END, product)

    def move_to_purchases(self):
        selected_items = self.listbox_products.curselection()
        for index in selected_items[::-1]:
            item = self.listbox_products.get(index)
            self.listbox_products.delete(index)
            self.listbox_purchases.insert(tk.END, item)

    def move_to_products(self):
        selected_items = self.listbox_purchases.curselection()
        for index in selected_items[::-1]:
            item = self.listbox_purchases.get(index)
            self.listbox_purchases.delete(index)
            self.listbox_products.insert(tk.END, item)


def main():
    root = tk.Tk()
    ShoppingListApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
