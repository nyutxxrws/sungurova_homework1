user_input = input("Введите число: ")
if user_input.isdigit() == False:
    print("Ошибка: введено не число")
elif int(user_input) == 0:
    print("Число должно быть положительным")
elif int(user_input) % 2 == 0:
    print(f"Число {user_input} является четным")
else:
    print(f"Число {user_input} не является четным")