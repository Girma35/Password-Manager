# importing 
from random import choice, randint, shuffle 
import tkinter as tk
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    pass_number  = [choice(numbers) for i in range(nr_numbers)]
    pass_letter = [choice(letters) for i in range(nr_letters)]
    pass_symbol = [choice(symbols) for i in range(nr_symbols)]
    password_list = pass_number + pass_letter + pass_symbol
    shuffle(password_list)
    password = ''.join(password_list)

    p_entry.insert(0, password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = w_entry.get()
    email = e_entry.get()
    password = p_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password      
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Warning", "Please enter all fields.")
    else:
        is_ok = messagebox.askokcancel("Details", f"{website} \nEmail: {email} \nPassword: {password}\nIs this ok to save?")
        if is_ok:
            try:
                with open("password.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            except json.JSONDecodeError:
                data = {}
            data.update(new_data)
            try:
                with open("password.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            except IOError as e:
                messagebox.showerror("Error", f"Failed to save data: {e}")
            else:
                messagebox.showinfo(title="Success", message="Password saved successfully")
                w_entry.delete(0, 'end')  # Clear the website field
                p_entry.delete(0, 'end')  # Clear the password field

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = w_entry.get()
    if len(website) == 0:
        messagebox.showinfo("Warning", "Please enter the website field.")
        return
    try:
        with open("password.json", "r") as data_file:
            data = json.load(data_file)
        try:
            choose = data[website]
            email = choose["email"]
            password = choose["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        except KeyError:
            messagebox.showinfo(title="Empty", message=f"No data stored for {website}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    finally:
      w_entry.delete(0,'end')  

# ---------------------------- UI SETUP ------------------------------- #

# Initialize the main window
window = tk.Tk()
window.config(padx=40, pady=40)

# Create and configure the canvas
canvas = tk.Canvas(window, width=200, height=200, bg='white')
img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0, columnspan=2, pady=(20, 20))  # Add padding below the canvas

# Create and configure the label and entry widgets
w_label = tk.Label(window, text="Website:")
w_label.grid(column=0, row=1)
w_entry = tk.Entry(window)
w_entry.focus()
w_entry.grid(column=1, row=1, sticky='ew')

e_label = tk.Label(window, text="Email/Username:")
e_label.grid(column=0, row=2)
e_entry = tk.Entry(window)
e_entry.insert(0, "Girmawakeyo@gamil.com")
e_entry.grid(column=1, row=2, sticky='ew')

p_label = tk.Label(window, text="Password:")
p_label.grid(column=0, row=3)

# Search button
search_button = tk.Button(window, text="Search", width=37, bg="#5783db", command=search)
search_button.grid(column=2, row=1)

# Password Generate button and password field
generate_password = tk.Button(window, text="Generate", width=35, bg="#5783db", command=pass_generator)
generate_password.grid(column=2, row=3)
p_entry = tk.Entry(window)
p_entry.grid(column=1, row=3, sticky='ew')

add_button = tk.Button(window, text="Add", width=60, bg="#5783db", command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

# Start the Tkinter main loop
window.mainloop()
