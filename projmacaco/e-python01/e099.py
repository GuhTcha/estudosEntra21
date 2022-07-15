'''
99. Crie uma estrutra molde (orientada a objetos) para cadastro de veículos,
tendo como caracteristicas que os descrevem sua marca, modelo, ano, cor e valor.
Cadastre ao menos três veículos, revelando seu numero identificador de objeto alocado em memória,
assim como o retorno esperado pelo usuário quando o mesmo consultar tal veículo. 
'''
class concessionária:
    def __init__(self,marca,modelo,ano,cor,valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valor = valor
    pass
carro1 = concessionária('Chery','Tiggo 8 TXS 1.6 Turbo','2023','Branco','R$ 201.990,00')
carro2 = concessionária('BYD','Tan EV','2022','Cinza','R$ 515.890,00')
carro3 = concessionária('Volvo','S60 R-Design T8 2.0','2022','Vermelho','R$ 269.950,00')

print('----------\nEsses são os modelos que temos disponíveis:\n----------')
print(carro1.marca,carro1.modelo,carro1.ano,carro1.cor,carro1.valor)
print(carro2.marca,carro2.modelo,carro2.ano,carro2.cor,carro2.valor)
print(carro3.marca,carro3.modelo,carro3.ano,carro3.cor,carro3.valor)
    