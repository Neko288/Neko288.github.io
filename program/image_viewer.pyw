import os,math,tkinter as tk,subprocess
from tkinter.constants import Y
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk

win = tk.Tk()
win.geometry("1900x1200")
win.title("View image")

#--setting--
#frame  (setting)
frame = tk.Frame(win,
bd=2,
width=300,
height=400,
relief= tk.SOLID,
)
frame.place(x=1483, y=200)

#label setting
label_setting = tk.Label(
win,
font = ("游ゴシック", 20),
text = '設定',)
label_setting.place(x = 1600, y=205,)

#bg color
color_text = tk.Entry(width=15)
color_text.insert(tk.END,"snow")
color_text.place(x = 1580, y =250, )
label_bg = tk.Label(
win,
font = ("游ゴシック", 12),
text = '背景色',)
label_bg.place(x = 1500, y=245,)

#設定更新
def setting():
  #bg color
  win.configure(bg=color_text.get())
  label["bg"]= color_text.get()

#setting run button
setting_run_button = tk.Button(win, text='適用',  width=5, height=1, 
  bg='#ff0080', 
  foreground='white',
  activeforeground='black',
  command=lambda:setting())
setting_run_button.place(x = 1700, y = 550)


#--setting--END


label = tk.Label(
  win,
  font = ("游ゴシック", 18),
  text = "画像ビューアー",)
label.place(x = 1447, y=10,)


#pathだけどなんでも本来はURL
entry_text = tk.Entry(width=70)
entry_text.insert(tk.END,"D:/Mori/image/Genshin/")
entry_text.place(x = 1450, y =50, )

#global  &  atokara text
global img
canvas = tk.Canvas(win, width=550, height=800, bg="#c0c0c0")
global_num = 0
label_wh = tk.Label(
win,
font = ("游ゴシック", 12),
text = '',
bg='white',)
label_wh.place(x = 1700, y=820,)

label_size = tk.Label(
win,
font = ("游ゴシック", 12),
text = '',
bg='white',)
label_size.place(x = 1700, y=870,)

label_dir = tk.Label(
win,
font = ("游ゴシック", 12),
text = '',
bg='white',)
label_dir.place(x = 1700, y=770,)

label_where = tk.Label(
win,
font = ("游ゴシック", 12),
text = '',
bg='white',)
label_where.place(x = 1600, y=720,)

label_test = tk.Label(
win,
font = ("游ゴシック", 12),
text = '',
bg='white',)
label_test.place(x = 1600, y=670,)


#Help button
help_button = tk.Button(win, text='Help',  width=5, height=1, 
  bg='#ff0080', 
  foreground='white',
  activeforeground='black',
  command=lambda:subprocess.Popen(["start", 'C:/any\Python-P/imaeg_viewer/Help.txt'], shell=True))
help_button.place(x = 1800, y = 15)

#画像表示
def show_image(back):
  #resize
  global canvas
  global global_num
  global img
  global label_wh

  canvas.place_forget()
  if back == 'n':
    global_num +=1
    print('next')
  if back == 'b':
    global_num -=1
    print('back')
  if back == 's':
    global_num = 0

  dir_path = entry_text.get() + r'/' #パスの最後に/入れて
  aru_nai = os.path.exists(dir_path)
  if aru_nai == False:
    messagebox.showerror('Error 404','指定されたパスが見つかりません。絶対パスを入力してください。')
  all_img = os.listdir(dir_path)

  if len(all_img) <= 1:
      messagebox.showerror('Error', '画像が少ないようです...一枚以下では表示できません')
  img = Image.open(dir_path + all_img[global_num])
  print('   Image.open ..OK')



  label_wh["text"] = '画像xy : ' + str(img.width) +'x'+ str((img.height))
  image_size = os.path.getsize(dir_path + all_img[global_num]) / 1024
  n = 2  # 切り捨てしたい桁
  y = math.floor(image_size * 10 ** n) / (10 ** n)
  label_size["text"] = '画像サイズ :' + str(y)+'MB'
  label_dir["text"] = 'ファイル数 : ' + str(len(all_img)) +'/'+ str(global_num)
  label_where["text"] = '場所 : ' + dir_path
  win.title('image_Viewer for 「' + all_img[global_num] + '」')
  print('   windows set ..OK')

  w = img.width
  h = img.height
  size = 1400
  sizeh = 1050
  if w == h:
    small_num_1 = (w / size)
    w = math.ceil(w/small_num_1)
    h = w
  elif w >= size:
    small_num_2 = (w / size)
    w = math.ceil(w/small_num_2)
    h = math.ceil(h/small_num_2)
  elif w <= size:
    small_num_3 = (size / w)
    w = math.ceil(w*small_num_3)
    h = math.ceil(h*small_num_3)
  if h >= sizeh:
    small_num_4 = (h / sizeh)
    w = math.ceil(w/small_num_4)
    h = math.ceil(h/small_num_4)

  resize_img = img.resize((w,h))
  label_test["text"] = 'リサイズ画像サイズ : ' + str(w) +" x "+str(h) 

#画像クリック時フォルダーを開く
  def click(self):
    subprocess.Popen([entry_text.get() +'/'+all_img[global_num]], shell=True)

  img = ImageTk.PhotoImage(resize_img)
  canvas = tk.Canvas(win, width=w, height=h, bg="#c0c0c0",)
  canvas.place(x=0, y=0)
  canvas.create_image(0,0, anchor=tk.NW, image=img)
  canvas.bind("<Button-1>", click)
  print('   create_image ..OK')

#Next button
next_image_button = tk.Button(win, text='Next',  width=10, height=2, 
  bg='#00ffff', 
  foreground='black',
  activeforeground='black',
  command=lambda:show_image('n'),
  repeatinterval=150,#長押し
  repeatdelay=1,)#長押し
  #引数付き関数をボタンで実行する際の注意点*2
next_image_button.place(x = 1600, y = 100)

#Back button  
back_image_button = tk.Button(win, text='Back',  width=10, height=2, 
  bg='#ff0080', 
  foreground='white',
  activeforeground='black',
  command=lambda:show_image('b'),
  repeatinterval=150,#長押し
  repeatdelay=1,)
back_image_button.place(x = 1700, y = 100)



#show_image('s')
print('___PROGRAM Setting ..OK___')

win.mainloop()



#*2 = https://duckduckgo.com/?q=command+tkinter+%E5%BC%95%E6%95%B0&t=ffab&ia=web