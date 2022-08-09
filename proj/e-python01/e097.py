#def retirada: https://www.youtube.com/watch?v=VrQmMbPpbf0
def erro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número válido.\033[m')
        if ok:
            break
    return valor

fixo = 29.11
extra = 5.00
horas = float(erro('Quantas horas você trabalha por semana? '))
if horas > 40.0:
    salario = fixo * 40
    adicional=extra*(horas - 40)  
    print(salario+adicional)
else:
    salario = fixo*horas
    print(salario)