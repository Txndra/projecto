#SK was here xddddd
#prep
import sqlite3
from tkinter import *
import pandas as pd
import matplotlib as plt
import os
import requests
#df = pd.read_csv("database")

#Login screen
def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def CloseAll():
  delete2()
  screen.destroy()

def login_success():
  global screen3
  screen3 = Toplevel(screen) 
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Success").pack()
  Button(screen3, text = "OK", command =CloseAll).pack()
  menu()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Success", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  #getting from entry boxes
  username1 = username_verify.get()
  password1 = password_verify.get()
  #clear boxes for ease
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
  #beta encryption level just to story name and pass{WORK ON IF HAVE TIME}
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_success()
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  #new window
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  #can now use anywhere
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Secant Marketing Program")
  Label(text = "Hi there!", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

#MAIN MENU functions
def menu():
  global start
  global option
  start = Tk()
  start.title("SMG v1.1.0")
  start.geometry("450x400")
  global searchbox
  global search
  sites = [
    "Amazon",
    "Tesco",
    "Sainsburys"
    ]
  #kek
  option = StringVar()
  

  #drop menu
  drop = OptionMenu(start, option, *sites)
  drop.grid(row=1, column=0)
  #functionality of send button ready for api
  submitbut = Button(start, text='submit', command=send)
  submitbut.grid(row=2,column=2)
  #entry boxes
  searchbox_label = Label(start, text="Search:")
  searchbox_label.grid(row=2, column=0)
  #e
  searchbox = Entry(start,width=30)
  searchbox.grid(row=2,column=1)
  #saving inputted values
  search = searchbox.get()
  #clearing box after search
  clear = Button(start,text="Clear", command=ClearBox)
  clear.grid(row=2,column=3)
  #quit program
  button_quit = Button(start, text="Exit Program", command=quit)
  button_quit.grid(row=99,column=99)
  


  
  start.mainloop()
# clear box
def ClearBox():
  searchbox.delete(0, END)
#feedback to user about what is going on
def send():
  search = searchbox.get()
  Label(start, text=f'sending request for,{search}, on {option}').grid(row=3,column=1)
  Label(start, text=f'{search}, Inputted').grid(row=4,column=1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN PARTTTT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#connection to amazon api live feed
class Retailer(option,search):
  search = str(search)
  option = str(option)
  def query2amazon(self):
    global word
    url = "https://amazon-product-reviews-keywords.p.rapidapi.com/product/search"

    querystring = {"keyword":search,"country":"GB","category":"aps"}

    headers = {
        'x-rapidapi-host': "amazon-product-reviews-keywords.p.rapidapi.com",
        'x-rapidapi-key': "3d86ca03bamsh2cfb5ea5f839101p185cdejsna0a123169efb"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
#adding user input so they can type what they want
#def search(word):


main_screen()
