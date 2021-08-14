while True:
#       Variables
    gold=66.6
    cash=25
    painting=50
    cocaine=50
    weed=37.5
    oneplayermax=1.00
    twoplayermax=2.00
    threeplayermax=3.00
    fourplayermax=4.00
    fiveplayermax=5.00
#       Questions/Message
    print ("\nPLEASE NOTE PUT A ZERO/0 IF YOU DO NOT HAVE A VALUE!")
    try:
        gold_amount=float(input("What are is the amount of Gold you have? "))
        cocaine_amount=float(input("What are is the amount of Coke you have? "))
        painting_amount=float(input("What are is the amount of Paintings you have? "))
        weed_amount=float(input("What are is the amount of Weed you have? "))
        cash_amount=float(input("What are is the amount of Cash you have? "))
#       Setting Gold Amounts to 0 as a int if they equal 0 as a string
        if gold_amount == "0":
            gold_amount=0
        elif weed_amount=="0":
            weed_amount=0
        elif cash_amount=="0":
            cash_amount=0
        elif cocaine_amount=="0":
            cocaine_amount=0
        elif painting_amount == "0":
            painting_amount=0
#       Time Tables for Formulas
        cashformula=cash*cash_amount
        paintingformula=painting*painting_amount
        weedformula=weed*weed_amount
        cocaineformula=cocaine*cocaine_amount
        goldformula=gold*gold_amount
#       Adding and Deviding To get correct Mathz
        addition_sector=((goldformula+cocaineformula+paintingformula+weedformula+cashformula)/100)
        rounded_sector=round(addition_sector, 1)
#       If/Elif/Else Statement Final Speach's For Gold Calcuation
        if rounded_sector < oneplayermax:
            print("You do not have the ability to fill a single bag!");
        elif rounded_sector < oneplayermax:
            print("You cannot fill up any bags!");
        elif rounded_sector < twoplayermax: 
            print("You have the ability to fill up 1 bags!");
        elif rounded_sector < threeplayermax: 
             print("You have the ability to fill up 2 bags!");
        elif rounded_sector < fourplayermax: 
             print("You have the ability to fill up 3 bags!");
        elif rounded_sector < 4.5:
            print("You have the ability to fill 4 bags!")
        elif rounded_sector > 4.1:
            print("You have the ability fill up 4+ bags!")
        elif rounded_sector > fiveplayermax:
            print("You have the ability to fill up 4+ bags")
        print("This is the rounded number " + str(rounded_sector) + " bags!")
        print("The exact number is " + str(addition_sector) + " bags!\n")
    except ZeroDivisionError:
        print("Error: You Cannot Devide by Zero! Also how the fuck did you even find this error DM me on discord Unlegitiment#0930!")
    except ValueError:
        print("You cannot have that character as a value please try again!")
#       Test more errors lmao cause kinda sucks rn lmao
#       Made By Unlegitiment! Please Contact for use via Discord Unlegitiment#0930!
#       #ad lmaooooo
#       Notes for The Coding Process
#       Equal to (==)
#       Not equal to (!=)
#       Less than (<)
#       Less than or equal to (<=)
#       Greater than (>)
#       Greater than or equal to (>=)