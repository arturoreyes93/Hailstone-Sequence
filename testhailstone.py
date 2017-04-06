def cyclelength(n):
       cycle_length = 0
    while (n>1):
        if (n % 2 == 0):
            n = n//2
        else:
            n = n*3+1
        cycle_length = cycle_length + 1
    return cycle_length

def main():
    x = eval(input("enter number: "))

    y = cyclelength(x)

    print(y)
