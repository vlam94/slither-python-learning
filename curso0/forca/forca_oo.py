import random
class Importavel():
    def __init__(self, endereco=None):
        self.conteudo=[]

    def __str__(self, pos):
        return f'{self.conteudo[pos]}'


class PalavraEscolhida(Importavel):

    def __init__(self, endereco):
        Importavel.__init__(self)
        palavras=[]
        with open (endereco) as f:
            for line in f:
                palavras.append(line.strip().upper())
        self.conteudo=random.choice(palavras)


class Grafico(Importavel):
    def __init__(self, endereco):
        Importavel.__init__(self)
        ibagens=[""]
        i=0
        with open (endereco) as f:
            for line in f:
                if line == "@@@\n":
                    i+=1
                    ibagens.append("")
                    continue
                ibagens[i]+=line
        self.conteudo=ibagens


class Jogo():

    def __init__(self):
        self.ibagem = Grafico("slither-python-learning/curso0/forca/jogoimg.txt")
        self.forca = Grafico("slither-python-learning/curso0/forca/forcaimg.txt")
        self.palavra = PalavraEscolhida("slither-python-learning/curso0/forca/palavras.txt")
        self.quiz = ""
        for letra in self.palavra.conteudo:
            self.quiz+=" _ "
        self.chutes_errados = []
        self.estado = 0
        self.num_erros = 0
    
    def __str__(self,partida):
        if partida: return self.forca.__str__(self.num_erros)+f'\n\na palavra é: {self.quiz}'
        return self.ibagem.__str__(self.estado)
    """
    def quiz(self):
        ret=""
        for letra in self.palavra.conteudo[0]:
            if letra in self.letras_chutadas:
                ret += " %s "%letra
            else:
                ret+= " _ "
        print (u"A palavra é: %s\n"%ret)         
        return ret
"""
    def partida(self):
        print(self.__str__(True))
        while self.num_erros<9:
            break
        return True

    def inicio (self):
        print(self.__str__(False))
        if input("Vocẽ gostaria de ler as regras?(s/n):\n").lower().startswith("s"):
            self.estado+=1
            print(self.__str__(False))
            input(u"\nPressione enter↵ para continuar                                 ")
            self.estado+=1
        self.estado+=2
        pass

    def encerra (self):
        print(self.ibagem.conteudo[-1])
        exit()
  
jogo = Jogo()
jogo.inicio()
while jogo.partida():
    continue

