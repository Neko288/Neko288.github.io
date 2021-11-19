#これはVSCなどで使うことを想定したバージョンです。
import pyperclip


key = (' ')#intのみ。多分六桁まで
text =  ("  ")  #暗号化する内容
text_decode = ("񣌸񣍀񣍴񣍭")  #解読する内容


def Encode():
    code = ""
    for char in list(text):
        unic = ord(char)
        unic = (unic + int(key))
        code += chr(unic)
    print("Encode..." + code)
    pyperclip.copy(code)

def Decode():
    code =""
    for char in list(text_decode):
        unic = ord(char)
        unic = (unic - int(key))
        code += chr(unic)
    print("Decode..." + code)
    pyperclip.copy(code)


Encode()
#Decode()


