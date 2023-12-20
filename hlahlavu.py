import tkinter as tk
from tkinter import filedialog
import random

class WordJumbleGame:
    def __init__(self):
        self.words = set()
        self.selected_word = ""
        self.jumbled_word = ""
        self.score = 0
        self.timer = 60
        self.timer_running = False

        self.root = tk.Tk()
        self.root.title("Mthuli Buthelezi")
        self.root.configure(bg="#cd7f32")  # Rusty bronze color

        self.choose_file_button = tk.Button(self.root, text="Khetha isigudlo", command=self.load_dictionary)
        self.choose_file_button.pack(pady=20)

        self.start_game_button = tk.Button(self.root, text="Qala Umdlalo", command=self.start_game, state=tk.DISABLED)
        self.start_game_button.pack(pady=10)

        self.label = tk.Label(self.root, text="", font=("Arial", 18), bg="#cd7f32", fg="white")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 14), state=tk.DISABLED)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Hambisa", command=self.check_word, state=tk.DISABLED)
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#cd7f32", fg="white")
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#cd7f32", fg="white")
        self.timer_label.pack(pady=10)

    def load_dictionary(self):
        file_path = filedialog.askopenfilename(title="Select Dictionary File",
                                               filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, 'r') as file:
                self.words = {word.strip().lower() for word in file.readlines()}
            if self.words:
                self.start_game_button.config(state=tk.NORMAL)

    def start_game(self):
        self.start_game_button.config(state=tk.DISABLED)
        self.score = 0
        self.timer = 60
        self.timer_running = True
        self.update_timer()
        self.display_new_word()
        self.update_clock()

    def display_new_word(self):
        self.selected_word = random.choice(list(self.words))
        self.jumbled_word = self.jumble_word(self.selected_word)
        self.label.config(text=self.jumbled_word)
        self.entry.delete(0, tk.END)
        self.entry.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.NORMAL)

    def jumble_word(self, word):
        return ''.join(random.sample(word, len(word)))

    def check_word(self):
        user_input = self.entry.get().lower()
        if user_input == self.selected_word:
            self.score += len(self.selected_word) * 10
            self.score_label.config(text=f"Score: {self.score}")
        self.display_new_word()

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer} sec")

    def update_clock(self):
        if self.timer_running and self.timer > 0:
            self.timer -= 1
            self.update_timer()
            self.root.after(1000, self.update_clock)
        else:
            self.game_over()

    def game_over(self):
        self.timer_running = False
        self.entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.score_label.config(text=f"Final Score: {self.score}")

if __name__ == "__main__":
    game = WordJumbleGame()
    game.root.mainloop()
