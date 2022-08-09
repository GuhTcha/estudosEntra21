# Define our function
def calculate():
    operation = input('Qual o calculo?')

    n1 = int(input('Coloque o primeiro numero: '))
    n2 = int(input('Coloque o segundo número: '))

    if operation == '+':
        print('=', n1 + n2)

    elif operation == '-':
        print('=',n1 - n2)

    elif operation == '*':
        print('=',n1 * n2)

    elif operation == '/':
        print('=',n1 / n2)

    else:
        print("tente novamente")

calculate()

'referência: https://www.digitalocean.com/community/tutorials/como-fazer-um-programa-de-calculadora-simples-no-python-3-pt'