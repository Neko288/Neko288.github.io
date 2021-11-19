#これは原神におけるダメージ計算ツールです。（鋭意開発中）
#関数(引数)についてhttps://www.javadrive.jp/python/userfunc/index2.html
#ダメージ計算についてhttps://wikiwiki.jp/genshinwiki/ダメージ計算式

print('倍率などはすべて実数値で入力してください。  例(80% = 0.8')
def all_keisan():
    #与えるダメージ
    def dmKeisan():
        atk = float(input("攻撃力 = "))
        bai = float(input("天賦ダメージ倍率 = "))
        cridm = float(input("会心ダメ = "))
        dmbuff = float(input("ダメージバフ = "))
        dm = (atk * bai * (1 + cridm ) * (1 + dmbuff) )
        kdm =(dm * 0.9)
        #↑基本的に敵には耐性10%があるのでそれをマイナスしている。
        print(kdm)


    def shiKeisan():
        #これはシールド計算式による。大抵はこれでいける。
        deff = float(input("防御力 or HP or 熟知 = "))
        bai_s = float(input("天賦倍率 = "))
        deff_num = float(input("天賦数値 = "))
        shi = (deff * bai_s + deff_num)
        print(shi)

    #結晶シールドのダメージ吸収量 kShi=結晶シールド
    def KshieldKeisan():
        genZyu = float(input("元素熟知 = "))
        keShi = (1.6 *  25 * genZyu / (9 *(genZyu + 1400)))
        print(keShi)


    dosuru = float(input("何する？ \n\
        ダメージ計算=1\n\
        シールド吸収量計算(防御力参照)=2\n\
        結晶シールド吸収量計算=3\n"))

    if dosuru == (1):
        dmKeisan()
    elif dosuru == (2):
        shiKeisan()
    elif dosuru == (3):
        KshieldKeisan()

while True:
    all_keisan()






input()


#これより下はメモです。



#キャラステータス
"""
atk = input("攻撃力=")
kisoatk = input("基礎攻撃力=")
hp = input("最大HP=")
deff = input("防御力=")
cri = input("会心率=")
cridm = input("会心ダメ=")
bai = input("天賦ダメージ倍率")
name = input("キャラ名=")
dmbuff = input("ダメージバフ")
genZyu = float(input("元素熟知="))
"""




#元素反応を考えない場合。
"""
if name==("仮"):
    dm = (atk * bai * (1 + cridm ) * (1 + dmbuff))
    print(dm)
"""

#聖遺物   Per=%
"""
sei_Per = input("聖遺物攻撃%=")
sei_12 = input("聖遺物攻撃数値=")
sei_dmbuff = input("ダメージバフ")
sei_criPer = input("聖遺物会心率")
sei_cridm = input("聖遺物会心ダメ")
"""


