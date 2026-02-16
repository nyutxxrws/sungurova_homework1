while True:
    num = input("Введите число: ")
    if num == "exit":
        print("Выход из программы")
        break
    if num.lstrip('-').isdigit():
        print(f"В этом числе {len(num.lstrip('-'))} цифр")
    else:
        print("Ошибка: данные не являются числом")