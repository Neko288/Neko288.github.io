#フォントは独自フォントを使っているので、そのままだと動きません。(多分)必要に応じて、フォントの設定を変えてください

import os,math,tkinter as tk,subprocess
from PIL import Image, ImageTk


#フォルダー指定ウィンドウ
win = tk.Tk()
win.geometry("400x150")
win.title("View image")
win.config(bg='#5FA0B6')

#path指定するとこ
entry_text = tk.Entry(width=70)
entry_text.insert(tk.END,"C:/image/hoge/")
entry_text.place(x = 1, y =1, )


#画像切り替え時間
label_key = tk.Label(
    win,
    font = ("851ゴチカクット", 13),
    text = "切り替わるタイミング/秒",
    bg='#5FA0B6',
    fg='white')
label_key.place(x = 1, y = 23,)

timing_text = tk.Entry(win,width=5,relief="flat",)
timing_text.insert(tk.END,'3')
timing_text.place(x = 220, y =25, )

timing = int(timing_text.get()) * 1000


#グローバル用の情報とかglobal
global slide_win
global img
global_num = 0

def show_image():#画像をを次々流すよう。毎回ループする。
  global canvas
  global global_num
  global img
  #canvas.place_forget()#画像の残像が残るのを防ぐため。
  global_num += 1
  canvas.pack_forget()

  dir_path = entry_text.get() + r'/' #画像があるパス。(entryからディレクトリを取得)
  all_img = os.listdir(dir_path)#フォルダー内画像数

  img = Image.open(dir_path + all_img[global_num])#画像のパス。(画像の場所も入れる。dir_pathは画像のあるフォルダー)

  print(dir_path + all_img[global_num])

  slide_win.title('image_Viewer for 「 ' + all_img[global_num] + ' 」')#ウィンドウのタイトル

  w = img.width#画像の横のサイズを取得
  h = img.height#画像の縦のサイズを取得
  size = 1900#リサイズしたい画像サイズ(縦)
  sizeh = 1080#リサイズしたい画像サイズ(横)
  if w == h:
    small_num_1 = (w / size)#画像をリサイズしたいサイズで割る。元の画像xsmall_num_1=リサイズしたい画像サイズ
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

  resize_img = img.resize((w,h))#リサイズしたいwとhを求めたので、そのサイズでリサイズする。

  def click(self):
    subprocess.Popen([entry_text.get() +'/'+all_img[global_num]], shell=True)

  #画像を表示
  img = ImageTk.PhotoImage(resize_img)
  canvas = tk.Canvas(slide_win, width=w, height=h,bg="black")
  canvas.pack(anchor='center')
  canvas.create_image(0,0, anchor=tk.NW, image=img)
  canvas.bind("<Button-1>", click)
  print('画像を表示')

  slide_win.after(timing, show_image)


def slideshow():#画像を作るだけのウィンドウ(ようはwinみたいなもん)
  global canvas
  global slide_win
  slide_win = tk.Toplevel()
  slide_win.geometry("1920x1080")
  slide_win.attributes('-fullscreen', True)
  slide_win.configure(bg='black')
  canvas = tk.Canvas(slide_win, width=0, height=0, bg='black',)
  slide_win.after(100, show_image)#This is looooooooop

  slide_win.mainloop()#ここで新しいウィンドウ(画像を流すウィンドウ)を終了


#Next button(新しいウィンドウを開くボタン)
next_image_button = tk.Button(win, text='Run ',  width=8, height=1, 
  bg='white', 
  font=("851ゴチカクット", 20,),
  foreground='black',
  activeforeground='black',
  command=slideshow,)
next_image_button.place(x = 120, y = 60)

win.mainloop()
