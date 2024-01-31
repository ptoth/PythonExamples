firstNum = input("Provide first number: ")
secondNum = input("Provide second number: ")
operator = input("Provide operator: ")

if operator == "+":
    print("Result incorrect: ", firstNum + secondNum)
    print("Result correct (casted as float type): ", float(firstNum) + float(secondNum))
elif operator == "-":
    print("Result: ", firstNum - secondNum)
    print("Result correct (casted as float type): ", float(firstNum) - float(secondNum))
elif operator == "*":
    print("Result incorrect: ", firstNum * secondNum)
    print("Result correct, but wrong casting: ", int(firstNum) * int(secondNum))
    print("Result correct, with proper castong: ", float(firstNum) * float(secondNum))
elif operator == "/":
    print("Result incorrect: ", int(firstNum) / int(secondNum))
