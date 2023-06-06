code = int(input("Enter user code\n"))
if code == 131:
    requesting = int(input("What do you wnat \n 1: recharge \n 2: buy data"))
    if requesting == 1:
        recharge = input("how much do you want to recharge\n a: 100 \n b:200 ")
        if recharge == "a":
            print("recharge of 100 naira was successful")
        elif recharge == "b":
            print("recharge of 200 naira was successful")
    else:
            print("wrong input")
else:
    print("invalid entry")