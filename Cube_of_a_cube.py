def cube(x):
    return x**3


def isThree(x):
    if x%3 == 0:
        return cube(x)
    else:
        print("Invalid Number")



print(isThree(15))