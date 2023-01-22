
import random

class Importavel():
    def __init__(self, endereco=None):
        self.conteudo=[]

    def __str__(self, pos):
        return f'{self.conteudo[pos]}'


class Palavra(Importavel):

    def __init__(self, endereco):
        Importavel.__init__(self)
        self.endereco= endereco
        
        
    def escolhePalavra(self):
        palavras=[]
        with open (f'{self.endereco}') as f:
            for line in f:
                palavras.append(line.strip().upper())
                palavra = random.choice(palavras)
        while palavra in self.conteudo or len(palavra) < 3:
            palavra = random.choice(palavras)
        self.conteudo.append(palavra)
        return  



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

    def __init__(self,ishardmode=input("pressione enter↵ para entrar\nou digite 'hard' para modo dificil: ").lower().startswith('h')): #(self,ishardmode) pra fazer assim o jogo teria que se iniciar antes
        self.ibagem = Grafico("jogoimg.txt")
        self.forca = Grafico("forcaimg.txt")
        self.palavra = Palavra("palavras.txt")
        self.palavra.escolhePalavra()
        self.ishardmode = ishardmode #(Fazer função de escolher dificuldade)
        self.chutes = []
        self.num_erros = int(ishardmode)
        self.abcd = "A Ã Á Â B C Ç D E Ê É F G H I Í J K L M N O Ô Ó P Q R S T U Ú V W X Y Z".split(' ') #isalpha() aceita ẽ, ĩ, î, que não existem no português
    
    def __str__(self):
        if self.num_erros==0:
            return self.forca.__str__(self.num_erros)
        return f'{self.montaImagem()}'
                
            
    def montaImagem(self):
        ret = "\n\n\nSeus chutes:\n*****"
        self.abcd
        for letra in self.chutes:
            ret+="\n* %s *"%letra
        ret += u"\n*****\n\nVocê ainda pode chutar:"
        ret=ret.split("\n") #"abre" pra juntar a img
        i=3
        for linha in self.ibagem.conteudo[2].split("\n"):
            ret[i]+=' '*(43-len(ret[i])) + linha
            i+=1
        ret = "\n".join(ret) #"fecha"
        starline=str("\n" + "*"*(len(self.abcd)*2-1))
        ret += starline + "\n%s"%' '.join(self.abcd) + starline + "\n\n\n%s"%self.forca.__str__(self.num_erros)
        return ret           
        
    
    def geraQuiz(self):
        ret=""
        for letra in self.palavra.conteudo[-1]:
            if letra in self.chutes:
                ret += "%s "%letra
            else:
                ret+= "_ "
        print (u"A palavra é: %s\n"%ret)         
        return ret

    def sair (self):
        print (self.ibagem.conteudo[-2])
        if not input(' '*35):
            print (self.ibagem.conteudo[-1])
            exit()  
        return

    def checaChute(self,chute):
        if chute not in self.palavra.conteudo[-1]:
            self.num_erros+=1+self.ishardmode
        self.abcd.remove(chute)
        self.chutes.append(chute)
        return

    def chuta(self):
        while True: #erros=True
            chute=input("Chute uma letra:\n")
            if chute=="exit":
                self.sair() 
            if not chute:
                continue
            chute=chute[0].upper()            
            if chute not in self.abcd: 
                print("\n'%s' não é válido\nou já foi chutado\n"%chute)
                continue
            break
        self.checaChute(chute)
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
        f = open (self.palavra.endereco,'r+')
        plv = str()
        while not (plv=='*'):
            plv = input("\nInsira a palavra com acentuação correta,\nou digite * para sair do editor: ").upper() 
            if not plv.isalpha():
                continue
            if plv in f.readlines():
                print("\nesta palavra já existe no jogo!\n")
                plv="#"
                continue
            if input("\nA palavra %s está correta?\nlembre-se da acentuação e ortografia!\n(S/N): "%plv).upper().startswith('S'):
                f.write("\n%s"%plv)
                print("\npalavra %s adicionada com sucesso\n\n"%plv)
                cont-=1
            if not bool(cont):
                print("\nvocê adicionou todas as %i palavras!\n"%lim)
                break
            print(u"você ainda pode adicionar %i palavras\n"%con)
        f.close()
        return

    def maisUma(self):
        if input(self.ibagem.conteudo[-3]).lower().startswith('n'):
            self.sair()
        self.__init__(self.ishardmode)
        self.jogar()    

    def jogar(self):
        while self.num_erros<10:
            print(self)
            if self.win():
                print(self.ibagem.conteudo[4-bool(self.num_erros)])
                print("você errou %i vezes\n\n"%self.num_erros)
                self.addPalavra()
                break
            self.chuta()
        self.maisUma()
        return
    
    def inicio (self):
        print(self.ibagem.conteudo[0])
        if self.ishardmode:
            print("\n\nem modo dificil\n * BOA SORTE! *\n\n")
        if input("Vocẽ gostaria de ler as regras?(s/n):\n").lower().startswith("s"):
            print(self.ibagem.conteudo[1])
            input(u"\nPressione enter↵ para continuar                                        ")
        return

forca=Jogo()
forca.inicio()
forca.jogar()

