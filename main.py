from tkinter import messagebox
from tkinter import  *
from random import choice ,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_passaword():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)



    password_letters= [choice(letters) for char in range(nr_letters)]
    passaword_symbols = [choice(numbers) for symbols  in range(nr_symbols)]
    passaword_numbers = [choice(symbols) for number  in range(nr_numbers)]

    passaword_list = passaword_symbols + passaword_numbers +password_letters
    shuffle(passaword_list)

    password = "".join((passaword_list))
    passaword_e.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():



    search_website = website_e.get()

    try:
        with open("data.json", "r") as data_file:
            s_data = json.load(data_file)
            # reading old data


    except FileNotFoundError:
        warning = messagebox.showinfo(title="Couldn't find website", message="Please enter another site")

    else:
        if search_website in s_data:

            saved_data = s_data[search_website]
            document = messagebox.showinfo(title=search_website.title(),
                                           message=f"email:{saved_data['email']} \n Password:{saved_data}")
        else:
            warning = messagebox.showinfo(title="Error", message=f"No details about {search_website}")


def save():
    website_text = website_e.get()
    email_text = email_e.get()
    passaword_text = passaword_e.get()
    new_data = {
        website_text: {
            "email":email_text,
            "pasaword":passaword_text,
        }
    }

    if len(website_text) ==0 or len(passaword_text) == 0:
        warning = messagebox.showinfo(title="Oops",message="Plase makesure you haven!t left any fields empty")
    else:
        try:
            with open("data.json","r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                # saving new data
                json.dump(new_data,data_file,indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_e.delete(0,END)
            passaword_e.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title = ("Passaword Manager")
window.config(padx=50,pady=50,highlightthickness=0)
canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)

# website label
website_l = Label(text="Website:")
website_l.grid(column=0,row=1)

#website  enter
website_e = Entry(width=35)
website_e.grid(column=1,row=1,columnspan=2)
website_e.focus()



# email label2
email = Label(text="Email/Username::")
email.grid(column=0,row=2)

#email  enter
email_e = Entry(width=44)
email_e.grid(column=1,row=2,columnspan=3)
email_e.insert(0,"name@gmail.com")

# passaword label
password_l = Label(text="Password:")
password_l.grid(column=0,row=3,)


#passaword  enter
passaword_e = Entry(width=36)
passaword_e.grid(column=1,row=3,columnspan=2)


# generate button
generate_button = Button(text="Generate Password",command=generate_passaword)
generate_button.grid(column=2,row=3,columnspan=2)

# add button
add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2,)

# search button
search_button = Button(text="Searcch",width=10,command=search)
search_button.grid(column=2,row=1,columnspan=2)
# en

window.mainloop()