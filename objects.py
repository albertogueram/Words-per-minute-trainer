import tkinter as tk
import time
import random


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.sample_texts = self.load_texts("sample_texts")
        self.sample_text = ""

        self.start_time = None
        self.end_time = None
        self.words_typed = 0

        # TKINTER WINDOW LAYOUT
        self.sample_text_label = tk.Label(root, text="Type the following text:")
        self.sample_text_label.pack(pady=10)

        self.sample_text_display = tk.Label(root, text=self.sample_text, font=("Courier", 12), wraplength=400)
        self.sample_text_display.pack(pady=10)

        self.text_box = tk.Text(root, height=5, width=50, wrap="word")
        self.text_box.pack(pady=10)
        self.text_box.bind("<KeyRelease>", self.check_text)  # Link Key Release Event to method "Check_Text"

        self.start_button = tk.Button(root, text="Start Typing Test", command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(root, text="Typing Speed: 0 WPM", font=("Courier", 12))
        self.result_label.pack(pady=10)

    def load_texts(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                texts = [line.strip() for line in file if line.strip()]
                return texts if texts else ["No sample texts found in file."]
        except FileNotFoundError:
            return ["Error: Text file not found."]

    def start_test(self):
        self.sample_text = random.choice(self.sample_texts)
        self.sample_text_display.config(text=self.sample_text)

        self.text_box.delete(1.0, tk.END)  # Clear any previous text
        self.start_button.config(state=tk.DISABLED)
        self.text_box.config(state=tk.NORMAL)
        self.text_box.focus()  # Focus on the text box
        self.start_time = time.time()

    def check_text(self, event):
        user_input = self.text_box.get(1.0, tk.END).strip()  # Get text from text box

        if user_input == self.sample_text:
            self.end_time = time.time()
            time_taken = self.end_time - self.start_time
            words_typed = len(user_input.split())

            wpm = (words_typed / time_taken) * 60
            self.result_label.config(text=f"Typing Speed: {round(wpm, 2)} WPM")
            self.text_box.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)

