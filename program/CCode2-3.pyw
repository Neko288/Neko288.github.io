#暗号化/解読した文章が重なる問題を解決。
#無駄なdefもまとめた。

# -*- coding: utf-8 -*-
import pyperclip
import tkinter
from tkinter import messagebox

#make soft screen
win = tkinter.Tk()
win.title("CCode2")
win.geometry('850x450')


#make welcome label
label = tkinter.Label(
    win,
    font = ("System", 30),
    text = "This is CCode. I can Encode and Decode for you." )
label.place(x = 50, y = 50,)


#make Key
label_key = tkinter.Label(
    win,
    font = ("Lucida Sans Unicode", 12),
    text = "Enter the Key" )
label_key.place(x = 50, y = 150,)

key_text = tkinter.Entry(width=10)
key_text.place(x = 170, y =153, )


#make text
label_text = tkinter.Label(
    win,
    font = ("Lucida Sans Unicode", 12),
    text = "Enter the Text to be Encode or Decode" )
label_text.place(x = 50, y = 200,)

code_text = tkinter.Entry(width=75,)
code_text.place(x = 370, y =202, )

#label code
label_code = tkinter.Label(
    win,
    font = ("Arial", 25),
    text=' ',
    background='#FFFFFF' )
label_code.place(x = 50, y = 300,)

#make encode button 
def btn_click():
    key = key_text.get()
    text = code_text.get()
    code = ""
    if len(str(key)) > 7:
        messagebox.showerror('Error', 'パスワードが大きすぎます。6桁以内にしてください。')
    for char in list(text):
        unic = ord(char)
        unic = (unic + int(key))
        code += chr(unic)
    pyperclip.copy(code)
    code = ("Encode..." + code)
    
    #暗号化したものの出力
    label_code["text"] = code

button_encode = tkinter.Button(win, text='Encode', command=btn_click)
button_encode.place(x = 50, y = 250)
button_encode.bind(btn_click()) 


#make decode button
def btn_click_D():
    key = key_text.get()
    text = code_text.get()
    code =""
    if len(str(key)) > 7:
        messagebox.showerror('Error', 'パスワードが大きすぎます。6桁以内にしてください。')
    for char in list(text):
        unic = ord(char)
        unic = (unic - int(key))
        code += chr(unic)
    pyperclip.copy(code)
    code = ("Decode..." + code)

    #解読したものの出力
    label_code["text"] = code

button_decode = tkinter.Button(win, text='Decode', command=btn_click_D)
button_decode.place(x = 120, y = 250)
button_decode.bind(btn_click_D() )



win.mainloop()#mailnloopは最後に。待機状態にするらしい