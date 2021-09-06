
#prep
import sqlite3
from tkinter import *
import pandas as pd
import matplotlib as plt
import os
import requests
import time
import 
#df = pd.read_csv("database")

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

def ClearBox():
  searchbox.delete(0, END)
  
def send():
  search = searchbox.get()
  Label(start, text=f'sending request for,{search}, on {option}').grid(row=3,column=1)
  Label(start, text=f'{search}, Inputted').grid(row=4,column=1)
 
#connection to amazon api live feed
def query2amazon():
  global word
  url = "https://amazon-product-reviews-keywords.p.rapidapi.com/product/search"

  querystring = {"keyword":word,"country":"GB","category":"aps"}

  headers = {
      'x-rapidapi-host': "amazon-product-reviews-keywords.p.rapidapi.com",
      'x-rapidapi-key': "3d86ca03bamsh2cfb5ea5f839101p185cdejsna0a123169efb"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  print(response.text)
#adding user input so they can type what they want
#def search(word):
  


menu()


