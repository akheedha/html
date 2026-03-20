while(True):
    num = input("Enter a number or 'e' to exit: ")

    if num.lower() == 'e':
        break

    no = int(num)
    for i in range(1, 11):
        print(no, "x", i, "=", no*i) 