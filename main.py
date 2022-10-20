def rek(broj):
    if broj==0:
        return 0
    else:
        if (broj%10)%2==0:
            return 1+ rek(broj//10)
        else:
            return rek(broj//10)
broj=int(input("Unesite broj: "))
print(rek(broj))
