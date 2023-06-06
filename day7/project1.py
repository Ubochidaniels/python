userinput = int(input("usercode:"))
if userinput == 131:
    Request = (input("Make a request \n A: Buy Recharge card\n B: Request for airtime\n C: Borrow data\n D: Top \n "))
    if Request == "A":
        input =int(input("Recharge card: \n 1: $100\n 2: $200\n 3: $300\n 4: $400 \n "))
        if input == 3:
            print(" $300 dollars recharge succesful")
        elif Request == 2:
          print(" $200 dollars recharge successful")
        elif Request == 4:
            print(" $300 dollars recharge successful")
        elif Request == 1:
            print(" $400 dollars recharge was successful")
    if Request == "B":
        input = int(input (" Request for airtime \n 1: 200 \n 2: 400 \n 3: 500 \n 4: 600 \n" ))
        if input == 1:
            print(" 200 Recharged successfully")
        elif input ==3:
            print("500 recharge successful" )
        elif input ==2:
            print("400 recharge successful ")
        elif input ==4:
            print("600 recharge successful")
else:
    print ("wrong input")

