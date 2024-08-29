def multiply(l):
    prod = 1

    for i in l:
        if i == 0:
            print("Not multiplying by 0")
            continue
        prod *= i

    print("Product is :", prod)
    return prod