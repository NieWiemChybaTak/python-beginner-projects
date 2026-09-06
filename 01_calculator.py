print("==Calculator==")

oblicz = True
while oblicz == True:
    try:
        Nr1 = input("Give first number or leave program - q ")
        if Nr1 == "q":
            break
        Nr2 = input("Give second number: ")
        dzialanie = input ("What operation you wish to do? Avaliable: + - * / ")
        firstNR = float(Nr1.replace(",","."))
        secondNR = float(Nr2.replace(",","."))
        if dzialanie == "+":
            Wynik = (firstNR + secondNR)
            if Wynik.is_integer():
                print(f"Result: {(int(Wynik))}")
            else:
                print(f"Result: {(float(Wynik))}")
        elif dzialanie == "-":
            Wynik = (firstNR - secondNR)
            if Wynik.is_integer():
                print(f"Result: {(int(Wynik))}")
            else:
                print(f"Result: {(float(Wynik))}")
        elif dzialanie == "*":
            Wynik = (firstNR * secondNR)
            if Wynik.is_integer():
                print(f"Result: {(int(Wynik))}")
            else:
                print(f"Result: {(float(Wynik))}")
        elif dzialanie == "/":
            if secondNR == 0:
                print("You can't divide by zero")
            else:
                Wynik = (firstNR / secondNR)
                if Wynik.is_integer():
                    print(f"Result: {(int(Wynik))}")
                else:
                    print(f"Result: {(float(Wynik))}")
        else:
            op_uanv = input("Operation unavaliable. Repeat or quit? (q = quit / r = repeat)")
            if op_uanv == "q":
                break
            elif op_uanv != "r":
                print("Not an option. Quitting")
    except ValueError:
        print("Give numbers not letters. You can't multiply a*g")
        po_błędzie = input("Do you wish to continue calculating? Yes/No ")
        if po_błędzie == "Yes":
            oblicz = True
        else:
            oblicz = False
            print("Calculating over")
            break
