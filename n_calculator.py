# Calculator that applies the same mathematical operation to n numbers

calc_repeat = True
numStore = []
while calc_repeat:
    calc = input("Enter Input: ")
    if calc.isnumeric():
        numStore.append(int(calc))
    else:
        match calc:
            case "+":
                numResult = numStore[0]
                for value in range(1, len(numStore)):
                    numResult += numStore[value]
                print("Result: ", numResult)
                calc_repeat = False
            case "-":
                numResult = numStore[0]
                for value in range(1, len(numStore)):
                    numResult -= numStore[value]
                print("Result: ", numResult)
                calc_repeat = False
            case "*":
                numResult = numStore[0]
                for value in range(1, len(numStore)):
                    numResult *= numStore[value]
                print("Result: ", numResult)
                calc_repeat = False
            case "/":
                numResult = numStore[0]
                for value in range(1, len(numStore)):
                    numResult /= numStore[value]
                print("Result: ", numResult)
                calc_repeat = False
            case _:
                print("Wrong Input! ")

