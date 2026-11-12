from PIL import Image


def choose_mode():
    mode = ''
    while mode != '1' and mode != '2':
        mode = input('\n'
                     '1 - test mode\n'
                     '2 - operating mode\n'
                     'choose mode: ')
    return mode


def choose_image(mode):
    if mode == '1':
        im = Image.open('data/Mona_Lisa.jpg').convert("RGB")
    else:
        fl = 0
        while fl == 0:
            try:
                path = input('\n'
                             'Enter path of image: ')
                im = Image.open(path).convert("RGB")
            except:
                print('Invalid path')
            else:  # в этой конструкции else выполняется, когда не произошло ошибки в try
                fl = 1
    return im


#принимает символ, возвращает его в двоичном виде(строка) с незначащими нулями
def f(i):
    size = len(i.encode('utf-8')) #сколько байт занимает 1 символ
    tmp = bin(ord(i))[2:]
    tmp = '0'*(8*size-len(tmp)) + tmp #добавляем незначащие нули, у каждого символа своя длинна в 2сс
    #если в начале 0, то символ занимает 1 байт, если 1, то 2 байта
    if size == 2:
        tmp = '1' + tmp[1:]
    return tmp


#то же самое, только здесь на вход идут числа
def g(i):
    tmp = bin(i)[2:]
    tmp = '0'*(8-len(tmp)) + tmp
    return tmp


def h(k, text_2, T):
    text_len = len(text_2)
    if k < text_len:
        if T[-1] != text_2[k]:
            if T[-1] == '0':
                T = T[:-1] + '1'
            else:
                T = T[:-1] + '0'
        k += 1
    return [k, T]


def take_message():
    message = input('\n'
                    'Input your message: ')
    fl = 1
    while fl == 1:
        text_2 = ''
        for i in message:
            if len(i.encode('utf-8')) > 2:
                fl = 1
                break
            else:
                text_2 += f(i)
                fl = 0
        if fl == 1:
            print('uncorrected symbols')
            message = input('\n'
                            'Input your message: ')
    return text_2


def encoder(im, text_2, arr, mode):
    x, y = im.size
    k = 0  # идёт по строке из 0 и 1
    for i in range(x):
        for j in range(y):
            R, G, B = arr[i, j]

            R = g(R)
            G = g(G)
            B = g(B)

            k, R = h(k, text_2, R)
            k, G = h(k, text_2, G)
            k, B = h(k, text_2, B)

            arr[i, j] = int(R, 2), int(G, 2), int(B, 2)
    print('\nFile saved in project directory')
    print("Input this number in decoder", len(text_2))
    if mode == '1':
        im.save(
            "data/Mona_Lisa_shifr.png")  # сохраняй в png, чтобы избежать сжатия, а следовательно неправильной интерпретации
    else:
        im.save(
            "Image_with_shifr.png")


def decoder(mode):
    text_len = int(input('\n'
                         'Enter decode number: '))
    if mode == '1':
        im = Image.open('data/Mona_Lisa_shifr.png').convert("RGB")
    else:
        im = Image.open('Image_with_shifr.png').convert("RGB")
    arr = im.load()
    x, y = im.size
    ans = []  # сюда помещаем каждый символ в 2сс
    ans_2 = ''  # переводятся в привычные символы
    k = 0
    tmp = ''  # сюда считываются столько единиц и нулей, сколько введено
    for i in range(x):
        for j in range(y):
            R, G, B = arr[i, j]
            R = g(R)
            G = g(G)
            B = g(B)

            if k < text_len:
                tmp += R[-1]
                k += 1
            if k < text_len:
                tmp += G[-1]
                k += 1
            if k < text_len:
                tmp += B[-1]
                k += 1

    while len(tmp) > 0:
        if tmp[0] == '0':
            ans.append(tmp[:8])
            tmp = tmp[8:]
            continue
        if tmp[0] == '1':
            ans.append(tmp[:16])
            tmp = tmp[16:]

    for i in ans:
        i = '0' + i[1:]
        ans_2 += chr(int(i, 2))
    print("Message in image:", ans_2)


mode = choose_mode()
im = choose_image(mode)

text_2 = take_message()
arr = im.load()

encoder(im, text_2, arr, mode)
im.show()

decoder(mode)
