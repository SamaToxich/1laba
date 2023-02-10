x = open('test.txt')
a = list(map(int, x.readline()))

m = []


def chet(v):
    s = ''
    while v > 0:
        s += str(v % 4)
        v //= 4
    return int(s[::-1])


def slovo(x):
    z = {'0':'ноль',
         '1':'один',
         '2':'два',
         '3':'три',
         '4':'четыре',
         '5':'пять',
         '6':'шесть',
         '7':'семь',
         '8':'восемь',
         '9':'девять'
          }
    return z[x]
    

for i in range(len(a)-1):
    s = str(a[i]) + str(a[i+1])
    if 0 < a[i] < 4 and a[i+1] < 4:
        if int(s) < chet(1025):
            if int(s) % 2 == 1:
                if s[-2] == '3':
                    m += [int(s)]
                    l = ''
                    for i in range(len(s)):
                        if s[i] != '3':
                            l += s[i]
                    print(l)

for i in range(len(a)-2):
    s = str(a[i]) + str(a[i+1]) + str(a[i+2])
    if 0 < a[i] < 4 and a[i+1] < 4 and a[i+2] < 4:
        if int(s) < chet(1025):
            if int(s) % 2 == 1:
                if s[-2] == '3':
                    m += [int(s)]
                    l = ''
                    for i in range(len(s)):
                        if s[i] != '3':
                            l += s[i]
                    print(l)

for i in range(len(a)-3):
    s = str(a[i]) + str(a[i+1]) + str(a[i+2]) + str(a[i+3])
    if 0 < a[i] < 4 and a[i+1] < 4 and a[i+2] < 4 and a[i+3] < 4:
        if int(s) < chet(1025):
            if int(s) % 2 == 1:
                if s[-2] == '3':
                    m += [int(s)]
                    l = ''
                    for i in range(len(s)):
                        if s[i] != '3':
                            l += s[i]
                    print(l)

for i in range(len(a)-4):
    s = str(a[i]) + str(a[i+1]) + str(a[i+2]) + str(a[i+3]) + str(a[i+4])
    if 0 < a[i] < 4 and a[i+1] < 4 and a[i+2] < 4 and a[i+3] < 4 and a[i+4] < 4:
        if int(s) < chet(1025):
            if int(s) % 2 == 1:
                if s[-2] == '3':
                    m += [int(s)]
                    l = ''
                    for i in range(len(s)):
                        if s[i] != '3':
                            l += s[i]
                    print(l)

sred = (max(m) + min(m)) // 2

k = ''
for i in range(len(str(sred))):
    g = slovo(str(sred)[i])
    k += g + ' '

print(f'Среднее значение: {k}')
