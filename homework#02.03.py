my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
while n < len(my_list):
    if my_list[n] == 0:
        n += 1
        continue
    elif my_list[n] < 0:
        break
    print(my_list[n])
    n += 1

#for num in my_list:
#   if num > 0:
#       print(num)
#   elif num < 0:
#       break
