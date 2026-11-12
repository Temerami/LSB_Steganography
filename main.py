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
        fl1 = 0
        while fl1 == 0:
            try:
                path = input('\n'
                             'Enter path of image: ')
                im = Image.open(path).convert("RGB")
            except:
                print('Invalid path')
            else:  # в этой конструкции else выполняется, когда не произошло ошибки в try
                fl1 = 1
    return im


mode = choose_mode()
im = choose_image(mode)
im.show()
