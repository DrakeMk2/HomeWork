area1 = int(input('Введите число от 3 до 20: '))
area2 = []
for i in range(1, 21):
    for j in range(1, 21):
        q = i + j
        if area1 % q == 0 and i < j:
            area2.append(i)
            area2.append(j)
z = ''.join(map(str, area2))
print('Ваш пароль: ',z)
