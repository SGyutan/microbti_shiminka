from microbit import *
import music
import utime

"""
P0 と GND の端子にスピーカー/ブザー/ヘッドホンを繋ぐ必要あり
"""

onpu = Image("00900:"
             "00990:"
             "00909:"
             "99900:"
             "99900")

left_arrow = Image("00900:09000:99999:09000:00900")


# 笑顔のまち永遠なれ
# 作詞・作曲タケカワユキヒデ
# 4分音符=120

kukishi = [
            'd4:2','eb4:2','f4:2','f4:2','f4:2','f4:2','f4:2','f4:2','g4:4','a4:4','bb4:8',
            'g4:2','a4:2','bb4:2','bb4:2','a4:2','a4:2','g4:2','f4:10','r:4',
            'r:2','g4:2','g4:2','g4:2','g4:2','g4:2','a4:4','bb4:2','c5:2','a4:2','g4:2','f4:2','g4:6','r:4',
            'g4:2','g4:2','g4:2','g4:2','a4:4','bb4:4','a4:8','r:8',
            'd4:2','eb4:2','f4:2','f4:2','f4:2','f4:2','f4:2','f4:2','g4:4','a4:4','bb4:4',
            'r:2','a4:2','a4:2','bb4:2','c5:2','bb4:2','a4:2','g4:2','f4:2','g4:10','r8',
            'bb4:2','bb4:2','bb4:2','bb4:2','a4:4','bb4:4','c5:4','bb4:4','bb4:4','r:4',
            'g4:2','g4:2','g4:2','bb4:2','a4:2','a4:2','a4:2','bb4:10','r:8',
            'r:4','c5:2','c5:6','c5:2','c5:6','bb4:4','a4:4','bb4:4','a4:4','d4:4','d5:2','c5:2','c5:2','bb4:10','r:8',
            'r:4','g4:4','a4:4','bb4:4','g4:4','a4:4','bb:4','bb:4','bb4:4','a4:4','bb4:4','c5:2','c5:10',
            'r:2','bb4:2','a4:2','bb4:10','r:2','bb4:2','a4:2','bb4:10',
            'r:4','bb4:2','a4:6','bb4:4','c5:4','d5:2','c5:4','bb4:2','bb4:4','r:8',
            'g4:2','a4:2','a4:2','a4:2','bb4:4','c5:4','eb5:4','d5:4','c5:4','d5:4','c5:4','bb4:2','bb4:10',
            'r:4','bb4:4','bb4:2','a4:2','a4:2','bb4:10','r:8','r:16'
            ]



while True:
    display.show(onpu)
    utime.sleep_ms(800)
    display.show(left_arrow)
    utime.sleep_ms(800)

    #Aボタンを押すと始まります。
    if button_a.is_pressed():
     	#テンポはbpmの値で変えられます。
     	music.set_tempo(ticks=4, bpm=150)
        music.play(kukishi)


	#Bボタンを押すとプログラム終了です。（演奏途中で停止はできません）
    elif button_b.is_pressed():
        break

    else:
        pass
