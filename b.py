def fuc(num1, num2, num3):
    if num3 == 1:
        print("Ans: " + str(num1 + num2))
    elif num3 == 2:
        print("Ans: " + str(num1 - num2))
    elif num3 == 3:
        print("Ans: " + str(num1 * num2))
    elif num3 == 4:
        print("Ans: " + str(num1 / num2))
    elif num3 == 5:
        print("Ans: " + str(max(num1, num2)))
    elif num3 == 6:
        print("Ans: " + str(min(num1, num2)))
    else:
        print("error")

while True:
    x = input("What will you do(add, sub, mul, div, max, min) ").upper()
    y = float(input("First no: "))
    z = float(input("Second no: "))
    if x == "ADD":
        fuc(y, z, 1)
    elif x == "SUB":
        fuc(y, z, 2)
    elif x == "MUL":
        fuc(y, z, 3)
    elif x == "DIV":
        fuc(y, z, 4)
    elif x == "MAX":
        fuc(y, z, 5)
    else:
        fuc(y, z, 6)


