import tkinter as tk
import time


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        # Sample text for the user to type
        self.sample_text = ("The quick brown fox jumps over the lazy dog. "
                            "This is a common pangram used to test typing speed.")

        # Time tracking variables
        self.start_time = None
        self.end_time = None
        self.words_typed = 0

        # Create a label for the sample text
        self.sample_text_label = tk.Label(root, text="Type the following text:")
        self.sample_text_label.pack(pady=10)

        self.sample_text_display = tk.Label(root, text=self.sample_text, font=("Courier", 12), wraplength=400)
        self.sample_text_display.pack(pady=10)

        # Create a text box for the user to type in
        self.text_box = tk.Text(root, height=5, width=50, wrap="word")
        self.text_box.pack(pady=10)
        self.text_box.bind("<KeyRelease>", self.check_text)

        # Create a button to start the test
        self.start_button = tk.Button(root, text="Start Typing Test", command=self.start_test)
        self.start_button.pack(pady=10)

        # Create a label for displaying results
        self.result_label = tk.Label(root, text="Typing Speed: 0 WPM", font=("Courier", 12))
        self.result_label.pack(pady=10)

    def start_test(self):
        self.text_box.delete(1.0, tk.END)  # Clear any previous text
        self.start_button.config(state=tk.DISABLED)  # Disable the start button
        self.text_box.config(state=tk.NORMAL)  # Enable text box for typing
        self.text_box.focus()  # Focus on the text box
        self.start_time = time.time()  # Record start time

    def check_text(self, event):
        user_input = self.text_box.get(1.0, tk.END).strip()  # Get text from text box

        # Check if the typed text matches the sample text
        if user_input == self.sample_text:
            self.end_time = time.time()  # Record end time
            time_taken = self.end_time - self.start_time
            words_typed = len(user_input.split())

            # Calculate Words Per Minute (WPM)
            wpm = (words_typed / time_taken) * 60
            self.result_label.config(text=f"Typing Speed: {round(wpm, 2)} WPM")
            self.text_box.config(state=tk.DISABLED)  # Disable text box after completion
            self.start_button.config(state=tk.NORMAL)  # Re-enable start button for another attempt

