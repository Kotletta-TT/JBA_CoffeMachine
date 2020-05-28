# put your python code here
first_num = float(input())
second_num = float(input())
operation = input()

if not second_num and operation in ["/", "mod", "div"]:
    print("Division by 0!")
elif operation == "mod":
    print(first_num % second_num)
elif operation == "pow":
    print(first_num ** second_num)
elif operation == "div":
    print(first_num // second_num)
elif operation == "/":
    print(first_num / second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
