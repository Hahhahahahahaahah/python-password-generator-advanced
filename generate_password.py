#Imports
import random
import string 
from tkinter import messagebox
pun = string.punctuation
letters = string.ascii_letters
numbers = string.digits
combined = pun + letters + numbers
def generate_password(len:int):
    pw = ""
    for char in range(len):
        pw += random.choice(combined)
    return pw
    
password1 = generate_password(5)
print(password1)

def gui_generate_password(website, login_id, include_uppercase, include_lowercase, include_special_characters, include_numbers, password_length):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_special_characters:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    pwd = ""
    for i in range(password_length):
        pwd += random.choice("characters")