import tkinter as tk
import random

quotes = [
    "Believe in yourself!",
    "You can do anything if you put your mind to it.",
    "Every day is a second chance.",
    "Don’t stop until you’re proud.",
    "Mistakes are proof that you are trying.",
    "Push yourself, because no one else is going to do it for you.",
    "Dream it. Wish it. Do it."
]

def new_quote():
    quote_label.config(text=random.choice(quotes))

root = tk.Tk()
root.title("Daily Motivation")
root.geometry("400x200")
root.configure(bg="#2E2E2E")

quote_label = tk.Label(root, text=random.choice(quotes), wraplength=350, fg="white", bg="#2E2E2E", font=("Helvetica", 14), justify="center")
quote_label.pack(expand=True)

button = tk.Button(root, text="New Quote", command=new_quote, fg="white", bg="#4CAF50", font=("Helvetica", 12, "bold"), relief="flat", padx=10, pady=5)
button.pack(pady=10)

root.mainloop()

