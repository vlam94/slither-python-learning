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

class Forca():

    def __init__(self):
        self.palavra = PalavraEscolhida("slither-python-learning/curso0/forca/palavras.txt")
        self.enforca = Grafico("slither-python-learning/curso0/forca/forcaimg.txt")
        
    def __str__(self, num_erros, letras_chutadas):
        return self.enforca.__str__(num_erros)


    def quiz(self,letras_chutadas,chute_errado):
        quiz=""
        if chute_errado:
            print("você já chutou: %s"%letras_chutadas)
        for letra in self.palavra.conteudo[0]:
            if letra in letras_chutadas:
                quiz += " %s "%letra

            else:
                quiz += " _ "
        print (u"A palavra é: %s\n"%quiz)

            
        return quiz

class Jogo():

    def __init__(self):
        self.ibagem = Grafico("slither-python-learning/curso0/forca/jogoimg.txt")
        self.forca = Forca()
        self.estado = 0
        self.num_erros = 0
    
    def __str__(self,partida):
        if partida: return self.forca.__str__(self.num_erros)
        return self.ibagem.__str__(self.estado)
        
    def partida(self):
        print(self.__str__(True))
        self.forca.quiz
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