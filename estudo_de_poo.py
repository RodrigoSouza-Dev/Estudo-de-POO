class Aluno:
    def __init__(self):
        self.nome=input("Digite nome do aluno: ")
        self.idade=input("Digite a sala do aluno: ")

    def media (self):
        n1= float(input("Digite a primeira nota: "))
        n2= float(input("Digite a segunda nota: "))
        n3= float(input("Digite a terceira nota: "))
        mediaGeral= (n1+n2+n3)//3
        
        if mediaGeral >= 5:
            print('O aluno {} foi aprovado com média= {}! '.format(self.nome, mediaGeral))
        else:
            print('O aluno {} foi reprovado com média= {}! '.format(self.nome, mediaGeral))

aluno1= Aluno()
aluno.media()