import random
pos=0
FORCAIMG= ['''
  +===+
  |  \|
      |
      |
      |
      |
=========''', '''
  +===+
  |  \|
  O   |
      |
      |
      |
=========''', '''
  +===+
  |  \|
  O   |
  |   |
      |
      |
=========''', '''
  +===+
  |  \|
  O   |
 /|   |
      |
      |
=========''', '''
  +===+
  |  \|
  O   |
 /|\  |
      |
      |
=========''', '''
  +===+
  |  \|
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +===+
  |  \|
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +===+
  |  \|
  O   |
 /|\  |
_/ \  |
      |
=========''', '''
  +===+
  |  \|
  O   |
 /|\  |
_/ \_ |
      |
=========''']
chutes=[]
palavras=str() #atualizar com novas palavras usando .append e quando sair reescrever palavras.txt a partir do palavras[]
with open('curso bosta/forca/palavras.txt') as f:
    for line in f:
        palavras+=line.strip().upper()
        palavras+=' '
    palavras=palavras.split(' ')


def escolhePalavra():
    global palavras
    return random.choice(palavras)


def geraQuiz(palavra):
    quiz=list()
    for l in palavra:
        quiz.append("_")
    return quiz

def chuta():
    global chutes
    chute = input("Chute uma letra: ")[0].upper()
    while True: #erros=True
        if len(chutes)>=1 and chute in chutes:
            chute=input("\n\nLetra repetida, chute outra: ").upper()
        elif not (ord("A")<=ord(chute)<=ord("Z")): #cruzes q feio
            chute=input("\n\nChute apenas letras (Ç=C): ").upper()
        else: return chute


def checaChute(palavra,chute,quiz):
    global pos
    i=0
    for l in palavra:
        if chute == l:
            quiz[i]=chute
        i+=1
    if chute not in quiz:
        pos+=1
        chutes.append(chute)
    return quiz

def geraImg(quiz):
    global pos, FORCAIMG, chutes
    print("A palavra é: ")
    print(str(quiz).strip())
    print ('                %s' %FORCAIMG[pos])
    if len(chutes)>=1:
        print ("seus chutes errados:", chutes)    
    return

def start():
    global pos, chutes
    pos=0
    chutes=[]
    forca=[None,None]
    forca[0]=escolhePalavra()
    forca[1]=geraQuiz(forca[0])
    geraImg(forca[1])
    return forca

def addPalavra():
    global palavras
    f = open ('curso bosta/forca/palavras.txt','a')
    plv = input("insira palavra sem 'ç' e acentos,\nou digite * para sair do editor: ").upper()
    while plv != '*':
        for l in plv:
            wrt=bool(ord("A")<=ord(l.upper())<=ord("Z"))
            if not wrt:
                plv = input("insira palavra sem 'ç' e acentos,\nou digite * para sair do editor: ").upper()
                break
        if wrt:
            if plv in palavras:
                print("\nesta palavra já existe no jogo\n")
            else:
                f.write("\n%s"%plv)
                print("\npalavra %s adicionada com sucesso\n\n"%plv)
        plv = input("insira palavra sem 'ç' e acentos,\nou digite * para sair do editor: ").upper()
    f.close()
    return
                       

#main
while True:
    forca=start()
    print(forca[0])
    while pos<8:
        chute=chuta()
        forca[1]=checaChute(forca[0],chute,forca[1])
        geraImg(forca[1])
        win = bool('_' not in forca[1])
        if win:
            print (u'''

            
**************
*  PARABÉNS  *
*VOCÊ ACERTOU*
**************
            
            ''')
            break
    if not win:
        print (u'''


******************
*   Que pena!    *
* você falhou :( *
******************
            
        ''')
    while True:
        end = input("\n\nJogar novamente(S/N) ou adicionar\npalavras ao jogo(A)?:")[0].upper()
        if end=='A':
            addPalavra()
        elif end=='N':
            print(u'''
******************************************            
*░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░*
*░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░*
*░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░*
*░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░*
*░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░*
*░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██*
*░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██*
*░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██*
*░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██*
*██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██*
*█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██*
*██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░*
*░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░*
*░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░*
*░░████████████░░░█████████████████░░░░░░*
******************************************
        * Por hoje é só, pessoal *
        **************************
''')
            exit()
        else:
            print("\n\nVAMOS JOGAR NOVAMENTE!!\n\n\n\n\n")
            break