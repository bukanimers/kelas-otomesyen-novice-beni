for bilangan in range(1,50):
    if bilangan % 3 == 0 and bilangan % 5 == 0:
        print("Dangdut")
    elif bilangan % 3 == 0:
        print("Dang")
    elif bilangan % 5 == 0:
        print("Dut")
    else:
        print(bilangan)