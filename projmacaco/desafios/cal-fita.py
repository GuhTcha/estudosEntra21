
def calculadora(a):
    resultado = str(eval(a))
    print(resultado)

a = (input('Digite uma operação:'))
calculadora(a)

registro = {'Calculo':a,'Resultado':resultado}
# class Calculadora:
#     result = 0

#     def __init__(self, op, num1, num2) -> None:
#         self.num1 = num1
#         self.num2 = num2
#         self.op = op
#         _f = str(num1) + str(self.op) + str(num2)
#         self.result = eval(_f)
    
#     @property
#     def op(self):
#         return self.op_valido

#     @op.setter
#     def op(self,op):
#         if isinstance(op,str):
#             op = str(op.replace('X','*'))
#         self.op_valido = op

#         if isinstance(op,str):
#             op = str(op.replace('.','*'))
#         self.op_valido = op

#         if isinstance(op,str):
#             op = str(op.replace('^','**'))
#         self.op_valido = op

#         if isinstance(op,str):
#             op = str(op.replace(':','/'))
#         self.op_valido = op

# num1 = int(input('Digite um número: '))
# num2 = int(input('Digite um número: '))
# op = input('Informe o operador: ').upper()

# resultado = Calculadora(op, num1, num2)
# print(f'Resultado: {resultado.num1} {resultado.op_valido} {resultado.num2} = {resultado.result}')