import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x250")
        self.root.configure(padx=20, pady=20)
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        
        # UI Elements
        self.title_label = tk.Label(root, text="🎯 Number Guessing Game", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)
        
        self.info_label = tk.Label(root, text="I'm thinking of a number between 1 and 100.")
        self.info_label.pack()
        
        self.guess_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
        self.guess_entry.pack(pady=10)
        
        self.guess_button = tk.Button(root, text="Guess!", command=self.check_guess, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.guess_button.pack(pady=5)
        
        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        # Bind Enter key to guess button
        self.root.bind('<Return>', lambda event: self.check_guess())

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid number.")
            return

        self.attempts += 1
        
        if guess < self.number_to_guess:
            self.feedback_label.config(text="Too low! Try again.", fg="red")
            self.guess_entry.delete(0, tk.END)
        elif guess > self.number_to_guess:
            self.feedback_label.config(text="Too high! Try again.", fg="red")
            self.guess_entry.delete(0, tk.END)
        else:
            self.feedback_label.config(text=f"🎉 You got it in {self.attempts} attempts!", fg="green")
            self.guess_button.config(state="disabled")
            
            play_again = messagebox.askyesno("You Win!", f"Congratulations! You guessed it in {self.attempts} attempts.\n\nPlay again?")
            if play_again:
                self.reset_game()
            else:
                self.root.destroy()
                
    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.guess_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
