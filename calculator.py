#calculate adding, subtraction, multiply, division
num_1 = int(input("Enter a number:"))
num_2 = int(input("Enter a another number:"))
choice = input("Enter the operater + - * /")
if choice == "+":
    sum = num_1 + num_2
    print("The sum of number ",sum)
elif choice == "-":   
    diff = num_1 - num_2
    print("The diff of number ",diff)
elif choice == "*":
    Multiple = num_1 * num_2
    print("The Multiple of number ",Multiple)
elif choice == "/":
    division = num_1 / num_2
    print("The division of number ",division)
else:
    print("invalid choice") 
