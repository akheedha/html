n = int(input("Enter number of levels: "))

if n <= 0:
    print ("Invalid number entered, TRY AGAIN!!")
else:
    for i in range(1, n + 1):
        print("*" * i)