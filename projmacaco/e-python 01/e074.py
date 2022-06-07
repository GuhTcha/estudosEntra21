# Define our function
def calculate():
    operation = input('Qual o calculo?')

    num1 = int(input('Coloque o primeiro numero: '))
    num2 = int(input('Coloque o segundo número: '))

    if operation == '+':
        print('=', num1 + num2)

    elif operation == '-':
        print('=', num1 - num2)

    elif operation == '*':
        print('=', num1 * num2)

    elif operation == '/':
        print('=', num1 / num2)

    else:
        print("tente novamente")

calculate()