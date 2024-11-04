import tkinter as tk
import pygame
import random
import os
from dotenv import load_dotenv
import openai


load_dotenv()

api_key = os.getenv("API_KEY")
openai.api_key = os.getenv("API_KEY")


def get_random_file(folder_path):
    # Get a list of files in the specified directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Check if there are any files in the folder
    if not files:
        print("No files found in the folder.")
        return None
    
    # Select a random file from the list
    random_file = random.choice(files)
    return random_file


def play_music():
    pygame.mixer.init()
    music_file = get_random_file("./music/")
    if music_file:
        pygame.mixer.music.load("./music/" + music_file)
        pygame.mixer.music.play(-1)

def submit_text():
    user_input = text_entry.get()
    print(f"User entered: {user_input}")
    text_entry.delete(0, tk.END)

    # Call OpenAI API with user input as the question
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You think you are always right, harsh and decisive. Low regard for weakness."},
            {"role": "user", "content": user_input},
        ],
    )
    
    # Extract and display the response
    reply = response.choices[0].message['content']
    response_label.config(text=f"Oracle says: {reply}")  # Update the label with the response

root = tk.Tk()
root.title("Oracle")
root.geometry("400x300")

label = tk.Label(root, text="Ask me", font=("Helvetica", 14))
label.pack(pady=20)

text_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
text_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command=submit_text)
submit_button.pack(pady=10)

# Label to display the OpenAI response
response_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=350)
response_label.pack(pady=20)

play_music()
root.mainloop()
