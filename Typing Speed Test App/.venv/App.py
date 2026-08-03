import tkinter as tk
from time import time
import random

# Sample Texts
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "A wizard's job is to vex chumps quickly in fog.",
    "Sphinx of black quartz, judge my vow.",
    "The five boxing wizards jump quickly."
]


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.sample_text = random.choice(texts)
        self.start_time = None

        # UI Elements
        self.label = tk.Label(root, text="Type the text below:", font=("Arial", 15))
        self.label.pack(pady=10)

        self.text_label = tk.Label(root, text=self.sample_text, font=("Arial", 15), wraplength=400)
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 13), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)
        self.entry.bind("<Return>", self.check_result)

        self.result_label = tk.Label(root, text="", font=("Arial", 13))
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time()

    def check_result(self, event):
        if self.start_time is None:
            self.result_label.config(text="Click the box and start typing first!")
            return

        end_time = time()
        typed_text = self.entry.get()
        time_taken = end_time - self.start_time

        if time_taken <= 0:
            self.result_label.config(text="Type something before pressing Enter!")
            return

        words = len(typed_text.split())
        wpm = words / (time_taken / 60)  # true division, not floor division

        # calculate accuracy
        correct_chars = sum(1 for a, b in zip(typed_text, self.sample_text) if a == b)
        accuracy = (correct_chars / len(self.sample_text)) * 100

        self.result_label.config(
            text=f"WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%\nTime: {time_taken:.2f}s"
        )

    def reset(self):
        self.sample_text = random.choice(texts)
        self.text_label.config(text=self.sample_text)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None


# Run the application
root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()