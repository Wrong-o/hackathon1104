import tkinter as tk
import pygame

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("fell.mp3")
    pygame.mixer.music.play(-1)

def submit_text():
    user_imput = text_entry.get()
    print(f"User enterad:{user_imput}")
    text_entry.delete(0, tk.END)

root = tk.Tk()
root.title("jgf")
root.geometry("400x200")

label = tk.Label(root, text="Ask me",font=("Helvetica",14))
label.pack(pady=20)

text_entry = tk.Entry(root,font=("Helvetical",14),width=30)
text_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit",font=("Helvetica",14),command=submit_text)
submit_button.pack(pady=10)
play_music()
root.mainloop()
