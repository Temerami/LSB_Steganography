def g(i):
    tmp = bin(i)[2:]
    tmp = '0'*(8-len(tmp)) + tmp
    return tmp


from PIL import Image

a = Image.open("Mona_Lisa_shifr.png").convert('RGB')
text_len = int(input())
ans = [] #сюда помещаем каждый символ в 2сс
ans_2 = '' #переводятся в привычные символы

b = a.size
x = b[0]
y = b[1]
arr = a.load()
k = 0
tmp = '' #сюда считываются столько единиц и нулей, сколько введено
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

for i in range(text_len // 8): #это работает только для символов 1б
    ans.append(tmp[:8])
    tmp = tmp[8:]

for i in ans:
    ans_2 += chr(int(i, 2))

print(ans_2)


