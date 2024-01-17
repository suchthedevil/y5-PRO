def vyhod2(zoznam,hodnota):
    while hodnota in zoznam:  #prvky zo zoznamu nevyhadzujeme cez for cyklus (ak nerobime kopiu)
        zoznam.remove(hodnota)
    print(zoznam)  

vyhod2([37, 'hello', -7,"hello", 3.14, 'hello', 2],"hello")

