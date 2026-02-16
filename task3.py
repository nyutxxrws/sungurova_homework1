user_input = input("Введите ваш возраст: ")
if user_input[0] == '-':
    print("Ошибка: возраст не может быть отрицательным!")
elif user_input.isdigit():
    if int(user_input) >= 18:
        print("Вы совершеннолетний")
    else:
        print("Вы несовершеннолетний")
else:
    print("Ошибка: введено не число!")