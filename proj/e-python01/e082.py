#e082.py 82. Crie uma função que eixbe em tela tanto o conteudo de uma variavel local quando de uma variavel global,
# sendo as variáveis de mesmo nome, porem uma não substituindo a outra. (usar o comando: global <variavel>)
# 1.  Mesmo exercicios fazendo com uma classe. 
var = 11
print ('Início: ',var)

def limpa_tela(self,a):
    global var
    print('Entrou1 : ',a)
    a = var + 1
    print('Entrou2 : ',a)
    return a
#não usar variaveis com nome iguais e cuidar com os globais, podem ocorrer bugs.
limpa_tela()
print('Saiu: ',var)