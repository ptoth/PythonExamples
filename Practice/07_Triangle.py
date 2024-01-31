triangleSideA = input("Provide side 'a' length: ")
triangleSideB = input("Provide side 'b' length: ")
triangleSideC = input("Provide side 'c' length: ")

triangleSideA = float(triangleSideA)
triangleSideB = float(triangleSideB)
triangleSideC = float(triangleSideC)

if not(
    (triangleSideA + triangleSideB > triangleSideC) and
    (triangleSideA + triangleSideC > triangleSideB) and
    (triangleSideB + triangleSideC > triangleSideA)
):
    print("Non-existent triangle!")
else:
    perimeter = triangleSideA + triangleSideB + triangleSideC
    print("Perimeter: ",perimeter)
