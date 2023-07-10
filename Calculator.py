operations = '''
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
'''

intro = print('''commands:
start - start the program
quit - quit the program
''')

question = ">"

while question.lower != "quit":
    question = input(">")
    if question.lower()  == "start":
        print(operations)
        question = input(">")
        if question == "1":
            first = int(input("First Number: "))
            second = int(input("Second Number: "))
            result = first + second
            print(f'= {result}')
            break
        if question == "2":
            first = int(input("First Number: "))
            second = int(input("Second Number: "))
            result = first - second
            print(f'= {result}')
            break
        if question == "3":
            first = int(input("First Number: "))
            second = int(input("Second Number: "))
            result = first * second
            print(f'= {result}')
            break
        if question == "4":
            first = int(input("First Number: "))
            second = int(input("Second Number: "))
            result = first / second
            print(f'= {result}')
            break