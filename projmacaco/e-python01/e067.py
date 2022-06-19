#e067.py
class carros:
    def __init__(self, fabricante, modelo, ano, combustivel, configuração):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self. combustivel = combustivel
        self.configuração = configuração 
    pass

carro1 = carros('Chery','Tiggo 8 TXS 1.6 Turbo','2023','Gasolina','SUV')
carro2 = carros('BYD','Tan EV','2022','Elétrico','SUV')
carro3 = carros('Volvo','S60 R-Design T8 2.0','2022','Híbrido','Sedâ')

print(carro1.fabricante,carro1.modelo,carro1.ano,carro1.combustivel,carro1.configuração)
print(carro2.fabricante,carro2.modelo,carro2.ano,carro2.combustivel,carro2.configuração)
print(carro3.fabricante,carro3.modelo,carro3.ano,carro3.combustivel,carro3.configuração)

'referência: https://www.youtube.com/watch?v=j6B8shHXzks'

#versão 1
# class Chery:
#     nome='Tiggo 8 TXS 1.6 Turbo'
#     ano=2023
#     combustivel='Gasolina'
#     configuração='SUV'

# class BYD:
#     nome='Tan EV'
#     ano=2022
#     combustivel='Eletricidade'
#     configuração='SUV'

# class Volvo:
#     nome='S60 R-Design T8 2.0'
#     ano=2022
#     combustivel='Híbrido'
#     configuração='Sedâ'