import random
import string 
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
