import random

def hontai():
    random_abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = ' 3 ' #名前を何文字にするか
    random_name = random.choices(random_abc, k=int(num)) #文字列をランダムに選択するンゴ
    random_name = ''.join(random_name) #リストを横に並べるンゴ(文章にする)
    print(random_name)
    input()
while True:
    hontai()