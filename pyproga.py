x = 1237178637
a = [k for k in range(0, 10)]
b = []

while (len(b) != 10):
    b.append(int(0))

while (((x // 10) != 0) or ((x >= 0) & (x <= 9))):
    for i in a:
        if (x % 10) == i:
            b[i] += 1
            x =  x // 10
    if x == 0:
        break
            
print("Количество цифр в числе:")
for i in a:
    print(a[i], "---", b[i])

