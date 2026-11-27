def calc(t, a, b=0):
    if t == "c":
        x = 3.1416 * a * a
        print("El area es: " + str(x))
        return x
    elif t == "r":
        x = a * b
        print("El area es: " + str(x))
        return x
    elif t == "t":
        x = a * b / 2
        print("El area es: " + str(x))
        return x
    else:
        print("error")

calc("c", 2)
calc("r", 4, 5)
calc("t", 6, 3)