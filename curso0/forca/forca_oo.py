import random

class Importavel():
    def __init__(self, endereco=None):
        self.conteudo=[]

    def __str__(self, pos):
        return f'{self.conteudo[pos]}'


class PalavraEscolhida(Importavel):

    def __init__(self, endereco):
        Importavel.__init__(self)
        self.endereco= endereco
        self.conteudo = self.escolhePalavra(endereco)
        
    def escolhePalavra(endereco):
        palavras=[]
        with open (endereco) as f:
            for line in f:
                palavras.append(line.strip().upper())
        return random.choice(palavras) #(str) override do tipo padrão de Importavel (list)


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

    def __init__(self,ishardmode):#(self,ishardmode) pra fazer assim o jogo teria que se iniciar antes
        self.ibagem = Grafico("slither-python-learning/curso0/forca/jogoimg.txt")
        self.forca = Grafico("slither-python-learning/curso0/forca/forcaimg.txt")
        self.palavra = PalavraEscolhida("slither-python-learning/curso0/forca/palavras.txt")
        self.ishardmode = ishardmode #(Fazer função de escolher dificuldade)
        self.chutes = []
        self.num_erros = int(ishardmode)
    
    def __str__(self):
        if self.num_erros==0:
            return self.forca.__str__(self.num_erros)
        return f'{self.montaImagem()}'
                
            
    def montaImagem(self):
        forca = "\n\n\nSeus chutes:\n*****"
        abcd="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(' ')
        for letra in self.chutes:
            forca+="\n* %s *"%letra
            abcd.remove(letra)
        forca += u"\n*****\n\nVocê ainda pode chutar:"
        forca=forca.split("\n") #"abre" pra juntar a img
        i=1
        for linha in self.ibagem.conteudo[2].split("\n"):
            forca[i]+=' '*(50-len(forca[i])) + linha
            i+=1
        forca = "\n".join(forca) #"fecha" 
        starline ="\n" + "*"*(len(abcd)*2+3)
        forca += starline + "\n* %s *"%' '.join(abcd) + starline + "\n\n\n%s"%self.forca.__str__(self.num_erros)
        return forca           
        
    
    def geraQuiz(self):
        ret=""
        for letra in self.palavra.conteudo:
            if letra in self.chutes:
                ret += " %s "%letra
            else:
                ret+= " _ "
        print (u"A palavra é: %s\n"%ret)         
        return bool("")

    def sair (self):
        print (self.ibagem.conteudo[-2])
        if not input(' '*35):
            print (self.ibagem.conteudo[-1])
            exit()  
        return


    def chuta(self):
        while True: #erros=True
            chute=input("Chute uma letra:\n")
            if chute=="exit":
                self.encerra() 
            if not chute:
                continue
            chute=chute[0].upper()            
            if chute in self.chutes: 
                print("\n a letra '%s' já foi chutada\n" %chute) 
                continue
            if chute.isalpha(): 
                print("\n'%s' não é válido\nchute apenas letras (Ç=C)\n"%chute)
                continue
            break
        if chute not in self.palavra.conteudo:
            self.num_erros+=1+self.ishardmode
        self.chutes.append(chute)
        return

    def win(self):
        if not "_" in self.geraQuiz():
            return True
        return False

    def addPalavra(self):
        if not input(self.ibagem.conteudo[-4]):
            return
        lim=2#editar mais facil o limite
        cont=int(lim)
        f = open (self.palavra.endereco,'a')
        plv="#"
        while plv != '*':
            if not bool(cont):
                print("\nvocê adicionou todas as %i palavras!\n"%lim)
                break
            while not plv.isalpha():
                plv = input("\ninsira palavra sem 'ç' e acentos,\nou digite * para sair do editor: ").upper() 
            if (palavra for palavra in f if plv==palavra):
                print("\nesta palavra já existe no jogo\n")
                plv="#"
                continue
            if input("\nDeseja adicionar a palavra %s ao jogo?(S/N)"%plv).upper().startswith('S'):
                f.write("\n%s"%plv)
                print("\npalavra %s adicionada com sucesso\n\n"%plv)
                cont-=1
                print(u"você ainda pode adicionar %i palavras\n"%cont)
        f.close()
        return

    def maisUma(self):
        if input(self.ibagem.conteudo[-3]).lower().startswith('n'):
            self.sair()
        self.__init__(self.ishardmode)
        self.partida()    

    def jogar(self):
        while self.num_erros<10:
            print(self)
            self.chuta()
            if self.win():
                print(self.ibagem.conteudo[3+bool(self.num_erros)])
                self.addPalavra()
                break
        self.maisuma()
        return
    
    def inicio (self):
        print(self.ibagem.conteudo[0])
        if input("Vocẽ gostaria de ler as regras?(s/n):\n").lower().startswith("s"):
            print(self.ibagem.conteudo[1])
            input(u"\nPressione enter↵ para continuar                                 ")
        return

jogo=Jogo(input("pressione enter↵ para entrar    ").lower().startswith("h"))
jogo.jogar()
jogo.maisUma()


