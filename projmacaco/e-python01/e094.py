class maiuscula:
    def __init__(self,string):
        self.string = string
    
    def imprimir(self):
        print(self.string)

    def mai(self):
        self.x = input('Me diga uma palavra:').upper()
        print(self.x)

maiuscula1 = maiuscula('------------\niniciando...\n------------')
maiuscula1.imprimir()
maiuscula1.mai()
