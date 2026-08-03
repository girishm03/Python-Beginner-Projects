import tkinter as tk
from tkinter import messagebox

def create_story():
    #retrieve inputs from the entry field
    place = place_entry.get()
    adjective = adjective_entry.get()
    noun = noun_entry.get()
    verb1 = verb1_entry.get()
    adverb = adverb_entry.get()
    adjective2 = adjective2_entry.get()
    verb2 = verb2_entry.get()
    body_part = body_part_entry.get()
    
    #validate inputs
    if not all([place, adjective, noun, verb1, adverb, adjective2, verb2, body_part]):
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return
    
    #story template
    story_template = (
        f"Today, I went to {place}, I saw a {adjective}, {noun} that was {verb1} {adverb}. "
        f"It was so {adjective2} that everyone started to {verb2}. I couldn't believe my {body_part}!"
    )
    
    #display the story in a message box
    messagebox.showinfo("Your Madlib Story", story_template)

# Create the main window
root = tk.Tk()
root.title("Madlib Story Generator")
root.geometry("400x600")

#Title lebel
title_label = tk.Label(root, text="Madlib Story Generator", font=("Arial", 19, "bold"), pady=10)
title_label.pack()

#input fields
field = [
    ("Enter a place:", "place"),
    ("Enter an adjective:", "adjective"),
    ("Enter a noun:", "noun"),
    ("Enter a verb ending in 'ing':", "verb1"),
    ("Enter an adverb:", "adverb"),
    ("Enter another adjective:", "adjective2"),
    ("Enter another verb:", "verb2"),
    ("Enter a body part:", "body_part")
]

#Dictionary to hold entry widgets
entries = {}

for label_text, key in field:
    label = tk.Label(root, text=label_text, font=("Arial", 13))
    label.pack()
    entry = tk.Entry(root, font=("Arial", 13))
    entry.pack(pady=10)
    entries[key] = entry

#Assigning entries to variables
place_entry = entries["place"]
adjective_entry = entries["adjective"]
noun_entry = entries["noun"]    
verb1_entry = entries["verb1"]
adverb_entry = entries["adverb"]
adjective2_entry = entries["adjective2"]
verb2_entry = entries["verb2"]
body_part_entry = entries["body_part"]

#Submit button  
submit_button = tk.Button(root, text="Create Story", font=("Arial", 15), command=create_story)
submit_button.pack(pady=25)

#Run the application
root.mainloop()