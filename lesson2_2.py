# задание 2
new_list = list(input("Введите значение:"))
for i in range(1, len(new_list), 2):
    new_list[i - 1], new_list[i] = new_list[i], new_list[i - 1]
print(new_list)




