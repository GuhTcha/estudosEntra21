fixo = 29.11
extra = 5.00
horas = float(input('Quantas horas você trabalha por semana? '))
if horas > 40.0:
    salario = fixo * 40
    adicional=extra*(horas - 40)  
    print(salario+adicional)
else:
    salario = fixo*horas
    print(salario)