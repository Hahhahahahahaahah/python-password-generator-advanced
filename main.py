import tkinter as tk
import generate_password

def on_button_clicked():
    website = website_entry.get()
    Login_ID = Login_entry2.get()
    include_uppercase = numbers_var_1.get()
    include_lowercase = numbers_var_2.get()
    include_Special_Characters = numbers_var_3.get()
    include_numbers = numbers_var_4.get()
#Window
window = tk.Tk()
window.title("Password Generator")
tk.Pack()
#Website(Entry)
tk.Label(window,text="Website").pack()
website_entry = tk.Entry(window)
website_entry.pack(padx=20)
#Login ID(Entry)
tk.Label(window,text="Login ID").pack()
Login_entry2 = tk.Entry(window)
Login_entry2.pack()
# True or False
numbers_var_1 = tk.BooleanVar()
numbers_var_2 = tk.BooleanVar()
numbers_var_3 = tk.BooleanVar()
numbers_var_4 = tk.BooleanVar()
#Max Len
Len_var = tk.IntVar()
slider = tk.Scale(window, variable = Len_var, from_ = 8, to = 12 , orient = tk.HORIZONTAL)
#Checkbutton "Include Numbers"
Checkbutton = tk.Checkbutton(window, text="Include?", variable = numbers_var_1)
tk.Label(window,text="Include Numbers").pack()
Checkbutton.pack(padx=20)
#Checkbutton "Include Uppercase"
Checkbutton2 = tk.Checkbutton(window, text="Include?", variable = numbers_var_2)
tk.Label(window,text="Include Uppercase").pack()
Checkbutton2.pack(padx=20)
#Checkbutton "Include Lowercase"
Checkbutton3 = tk.Checkbutton(window, text="Include?", variable = numbers_var_3)
tk.Label(window,text="Include Lowercase").pack()
Checkbutton3.pack(padx=20)
#Checkbutton "Include Special Characters"
Checkbutton4 = tk.Checkbutton(window, text="Include?", variable = numbers_var_4)
tk.Label(window,text="Include Special Characters").pack()
Checkbutton4.pack(padx=20)
#Password length(Entry)
tk.Label(window,text="Password Length").pack()
slider.pack()
# Generate password
generte_button = tk.Button(window , text = "Generate password")
generte_button.pack()
window.mainloop()