from tkinter import messagebox
from tkinter import *
from Password import *
from random import *
import pyperclip

# class StartPage(Frame):
#     def __init__(self, parent, controller):
#         Frame.__init__(self,parent)
#         self.controller = controller
#         self.label = Label(self, te)
#
#     def mainWindow(self):
#         self.newWindow = Toplevel(self.master)
#         self.app = MyWindow(self.newWindow)
#
#     def CheckPin(self):
#         if self.entry.get() == "1111":
#             messagebox.showinfo('Success', 'Your PIN is correct 🏆')
#             self.mainWindow()
#         elif self.entry.get() == "":
#             messagebox.showinfo('Empty Field', 'Entry field is emtpy')
#         else:
#             messagebox.showinfo('Wrong PIN', 'Your PIN is wrong 🚫')
#

class MyWindow:
    def __init__(self, master):
        # Create Window Components
        self.my_canvas = Canvas(width=200, height=200)
        self.my_photo = PhotoImage(file="logo.png")
        self.application_name_label = Label(text="Application Name :")
        self.application_name_entry = Entry(width=50)
        self.url_label = Label(text="Website/Url :")
        self.url_entry = Entry(width=50)
        self.username_label = Label(text="Email/Username :")
        self.username_entry = Entry(width=50)
        self.password_label = Label(text="Password :")
        self.password_entry = Entry(width=50)
        self.password_generate_button = Button(text="Generate", width=12, command=self.generate_password)
        self.add_button = Button(text="Add", width=12, command=self.add_new_password_into_txt_file)
        self.show_password_button = Button(text="Show", width=12)
        self.clear_button = Button(text="Clear", width=12, command=self.clear_all_fields)

        # Add Components in Grid
        self.my_canvas.create_image(100, 100, image=self.my_photo)
        self.my_canvas.grid(row=0, column=0, columnspan=5, padx=20, pady=20)
        self.application_name_label.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.application_name_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
        self.application_name_entry.focus()
        self.url_label.grid(row=2, column=0, columnspan=1, padx=5, pady=5)
        self.url_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
        self.username_label.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self.username_entry.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
        self.password_label.grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        self.password_entry.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
        self.add_button.grid(row=5, column=0, columnspan=1, padx=5, pady=5)
        self.show_password_button.grid(row=5, column=1, columnspan=1, padx=5, pady=5)
        self.clear_button.grid(row=5, column=2, columnspan=1, padx=5, pady=5)
        self.password_generate_button.grid(row=5, column=3, columnspan=1, padx=5, pady=5)

    def add_new_password_into_txt_file(self):
        new_entry = Application()

        if len(self.application_name_entry.get()) == 0 or len(self.password_entry.get()) == 0 or len(self.url_entry.get()) == 0 or len(self.username_entry.get()) == 0:
            messagebox.showinfo(title="Oops", message="Please don not leave any fields empty!")
        else:
            new_entry.application_name = self.application_name_entry.get()
            new_entry.url = self.url_entry.get()
            new_entry.password = self.password_entry.get()
            new_entry.email = self.username_entry.get()
            is_ok = messagebox.askokcancel(title=new_entry.application_name, message=f"These are the details entered:\nUser/Email: {new_entry.email}\nPassword: {new_entry.password}\nIs it ok to save it?")

            if is_ok:
                with open("mypasswords.txt", "a") as data_file:
                    data_file.write(new_entry.display_app())

    def clear_all_fields(self):
        self.application_name_entry.delete(0, END)
        self.application_name_entry.focus()
        self.url_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.username_entry.delete(0, END)

    def generate_password(self):
        # Password Generator Project
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

        password_list = password_symbols + password_numbers + password_letters
        shuffle(password_list)

        password = "".join(password_list)

        self.password_entry.insert(0,password)
        pyperclip.copy(password)
