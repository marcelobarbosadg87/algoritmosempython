n = int(input("Informe o valor "))



def fat(n):
    if(n < 2):
        return 1
    else:
        return n * fat(n-1)

print(fat(n))
