#e069.py
class i:
    def __init__(self,item1,item2):
        self.item1 = item1
        self.item2 = item2
        print(f'No seu carrinho tem: {self.item1} e {self.item2}')

compras = i(item1 = str(input('Deseja algo? ')), item2 = str(input('Mais alguma coisa? ')))