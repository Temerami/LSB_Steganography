def f(i):
    size = len(i.encode('utf-8')) #сколько байт занимает 1 символ
    tmp = bin(ord(i))[2:]
    tmp = '0'*(8*size-len(tmp)) + tmp #добавляем значащие нули, у каждого символа своя длинна в 2сс
    #если в начале 0, то символ занимает 1 байт, если 1, то 2 байта
    if size == 2:
        tmp = '1' + tmp[1:]
    return tmp

#то же самое, только здесь на вход идут числа
def g(i):
    tmp = bin(i)[2:]
    tmp = '0'*(8-len(tmp)) + tmp
    return tmp



from PIL import Image
a = Image.open("Mona_Lisa.jpg").convert("RGB")

b = a.size #массив из двух чисел

x = b[0]
y = b[1]

text = input()
text_2_ = [] #массив, хранящий в двоичном виде(со значащими нулями) символы в 2сс. 1 символ - 1 или 2 байта (англ или рус)
for i in text:
    text_2_.append(f(i))
text_2 = '' #с массивом работать неудобно, поэтому я объединяю все символы в двоичном виде в одну строку, состоящую из 0 и 1
for i in text_2_:
    text_2 += i
text_len = len(text_2) #длинна нужна для декодирования

k = 0 #идёт по строке из 0 и 1
arr = a.load()
for i in range(x):
    for j in range(y):
        R, G, B = arr[i, j]
        R = g(R)
        G = g(G)
        B = g(B)


        if k < text_len:
            if R[-1] != text_2[k]:
                if R[-1] == '0':
                    R = R[:-1] + '1'
                else:
                    R = R[:-1] + '0'
            k += 1

        if k < text_len:
            if G[-1] != text_2[k]:
                if G[-1] == '0':
                    G = G[:-1] + '1'
                else:
                    G = G[:-1] + '0'
            k += 1

        if k < text_len:
            if B[-1] != text_2[k]:
                if B[-1] == '0':
                    B = B[:-1] + '1'
                else:
                    B = B[:-1] + '0'
            k += 1

        arr[i, j] = int(R, 2), int(G, 2), int(B, 2)

print(text_len)
a.save("Mona_Lisa_shifr.png")#сохраняй в png, чтобы избежать сжатия, а следовательно неправильной интерпретации
a.show()

