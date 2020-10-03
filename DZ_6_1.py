value = 100
while value > 0:
    n = int(input("Enter value: "))
    if (value - n) < 0:
        print("Ошибка, результат будет отрицательным числом.")
        continue
    value -= n
print("You have", value)
