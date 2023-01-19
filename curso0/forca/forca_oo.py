import random
class Importavel():
    def __init__(self, endereco=None):
        self.conteudo=""

    def __str__(self):
        return self.conteudo

class PalavraEscolhida(Importavel):

    def __init__(self, endereco):
        Importavel.__init__()
        palavras=[]
        with open (endereco) as f:
            for line in f:
                palavras.append(line.strip().upper())
        self.conteudo=random.choice(palavras)
    
    def quiz(self,letras_chutadas):
        quiz=""
        for letra in self.conteudo:
            if letra not in letras_chutadas:
                quiz += " %s "%letra

            else:
                quiz += " _ "
        print (u"A palavra é: %s\n"%quiz)
        return quiz


class Enforcado(Importavel):
    def __init__(self, endereco):
        Importavel.__init__()
        ibagens=[""]
        i=0
        with open (endereco) as f:
            for line in f:
                if line == "@@@":
                    i+=1
                    ibagens.append("")
                    continue
                ibagens[i]+=line
        self.conteudo=ibagens
        
class Forca():

    def __init__(self):
        self.palavra = PalavraEscolhida("slither-python-learning/curso0/forca/palavras.txt")
        self.ibagem = Enforcado("slither-python-learning/curso0/forca/palavras.txt")
    
    def __str__(self):
        return self.quiz

    def start (self):
        print("nova partida de forca")
    def close (self):
        print("terminando partida")

class Jogo():

    def __init__(self):
        pass
    
    def __str__(self):
        pass

    def start (self):
        print("iniciando sistema")
        pass

    def close (self):
        print(u"por hoje é só pessoal")
        exit()
    


        
