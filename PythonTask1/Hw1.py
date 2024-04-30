while True:
    print ("Введите число для подсчёта количества символов.")
    print ("Введите exit для выхода из программы.")
    x = input()
    if x == "exit":
            break
    elif str.isdigit(x) is not True:
        print("Введён несоответствующий тип данных. Попробуйте снова")
        print("")
    else: print("Символов в числе:",len(str(x)))


