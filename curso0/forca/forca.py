import random
pos=0
FORCAIMG= ['''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||
| |         ($%)
| |        (    )
| |         `--'
| |
| |      
| |        
| |         
| |          
| |           
| |           
| |           
| |         
""""""""""|""""""""|""""|
|"|"""""""'""""""""'""|"|
| |                   | |
: :                   : :
. .                   . .''', '''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |           `--'
| |      
| |      
| |        
| |         
| |          
| |           
| |           
| |           
| |         
""""""""""|""""""""|""""|
|"|"""""""'""""""""'""|"|
| |                   | |
: :                   : :
. .                   . .''', '''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |          -`--'
| |          |. .|
| |          |   | 
| |          | . |  
| |          |___|   
| |          
| |           
| |           
| |           
| |         
""""""""""|""""""""|""""|
|"|"""""""'""""""""'""|"|
| |                   | |
: :                   : :
. .                   . .''', '''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'
| |        /Y . .|
| |       // |   | 
| |      //  | . |  
| |          |___|   
| |          
| |           
| |           
| |           
| |         
""""""""""|""""""""|""""|
|"|"""""""'""""""""'""|"|
| |                   | |
: :                   : :
. .                   . .''', '''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |          |___|   
| |          
| |           
| |           
| |           
| |         
""""""""""|""""""""|""""|
|"|"""""""'""""""""'""|"|
| |                   | |
: :                   : :
. .                   . .''', '''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\ 
| |          | __|   
| |          ||
| |          || 
| |          || 
| |          || 
| |         
""""""""""|""""""""|""""|
|"|"""""""'""""""""'""|"|
| |                   | |
: :                   : :
. .                   . .''', '''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |          |   |   
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         
""""""""""|""""""""|""""|
|"|"""""""'""""""""'""|"|
| |                   | |
: :                   : :
. .                   . .''', '''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         
""""""""""|""""""""|""""|
|"|"""""""'""""""""'""|"|
| |                   | |
: :                   : :
. .                   . .''', '''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|"`-'"`-'|""""|
|"|"""""""'""""""""'""|"|
| |                   | |
: :                   : :
. .                   . .

''']
chutes=[]
palavras=str() #atualizar com novas palavras usando .append e quando sair reescrever palavras.txt a partir do palavras[]
#with open('cursos/curso0/forca/palavras.txt') as f: #vscode
with open("palavras.txt") as f: #terminal
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
    while True: #erros=True
        chute=input("Chute uma letra:\n")
        if not chute:
            continue
        chute=chute[0].upper()            
        if len(chutes)>=1 and chute in chutes:
            print("\n a letra '%s' já foi chutada\n"%chute)
            continue
        if not (ord("A")<=ord(chute)<=ord("Z")): #cruzes q feio
            print("\n'%s' não é válido\nchute apenas letras (Ç=C)\n"%chute)
            continue
        return chute


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
    if pos>0:
        abcd="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(' ')
        print ("\n\nseus chutes errados:\n*****")
        for l in chutes:
            abcd.remove(l)
            print("* %s *"%l)
        for l in quiz:
            if l in abcd:
                abcd.remove(l)
        print("*****\n")
        spr=2*len(abcd)+1
        print("letras restantes:",str('*'*(spr-17)),"\n  %s*\n"%' '.join(abcd),"\b\b",str('*'*spr),"\n")
    print ('                %s' %FORCAIMG[pos])
    print("\nA palavra é: ",' '.join(quiz),"\n\n")
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
    lim=2#editar mais facil o limite
    cont=int(lim)
    f = open ("palavras.txt",'a')
    plv = input("\ninsira palavra sem 'ç' e acentos,\nou digite * para sair do editor: ").upper()
    while plv != '*':
        for l in plv:
            wrt=bool(ord("A")<=ord(l.upper())<=ord("Z"))
            if not wrt:
                plv = input("\ninsira palavra sem 'ç' e acentos,\nou digite * para sair do editor: ").upper()
                break
        if wrt:
            if plv in palavras:
                print("\nesta palavra já existe no jogo\n")
            else:
                if input("\nDeseja adicionar a palavra %s ao jogo?(S/N)"%plv).upper().startswith('S'):
                    f.write("\n%s"%plv)
                    palavras.append(plv)
                    print("\npalavra %s adicionada com sucesso\n\n"%plv)
                    cont-=1
                    print(u"você ainda pode adicionar %i palavras\n"%cont)
                if not bool(cont):#gastação de onda usando bool hehehe
                    print("\nvocê adicionou todas as %i palavras!\n"%lim)
                    break

        plv = input("insira palavra sem 'ç' e acentos,\nou digite * para sair do editor: ").upper()
    f.close()
    return
                       

#main
print('''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.                             __    __    __    __
                .X*#M@$!!  !X!M$$$$$$WWx:.                        /  \  /  \  /  \  /  \\
               :!!!!!!?H! :!$!$$$$$$$$$$8X:  ____*_*_*_*_*_*_*__/  __\/  __\/  __\/  __\________ 
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X: _____P_Y_T_H_O_N___/  /__/  /__/  /__/  /___________
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!    * * * * * * * * | / \   / \   / \   / \  \___
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!                    |/   \_/   \_/   \_/   \    o \\
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!                                            \_____/--<
               ~?WuxiW*`   `"#$$$$8!!!!??!!!                                           
             :X- M$$$$       `"T#$T~!8$WUXU~ *********   ****    *******    ******    *****
            :%`  ~#$$$m:        ~!~ ?$$$$$$  ********* ***  ***  ***  ***  ***  ***  *** *** 
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"  ***      ***    *** ***  *** ***       ***   ***
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`   ******   ***    *** ***  *** ***       ***   ***
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :     ******   ***    *** *******  ***       *********
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`     ***      ***    *** ***  *** ***       *********
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~      ***       ***  ***  ***  ***  ***  *** ***   ***
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `         ***         ****    ***  ***   ******  ***   ***
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

                                   *********************
                                   * B E M  V I N D O !*
                                   *********************
    ''')
while True:    
    forca=start()
    if len(forca[0])<=2:
        continue #erro de palavra vazia
    #print(forca[0]) #peep/cheat
    while pos<9:
        chute=chuta()
        forca[1]=checaChute(forca[0],chute,forca[1])
        geraImg(forca[1])
        win = bool('_' not in forca[1])
        if win:
            palavras.remove(forca[0]) #retira reocorrencia de palavras
            print (u'''

            
**************
*  PARABÉNS  *
*VOCÊ ACERTOU*
**************
            
            ''')
            break
    if pos==0:
            print("*1#1#1#1#1#1#*\n*DE PRIMEIRA!*\n*1#1#1#1#1#1#*")
    else:
        if not win:
            print (u'''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  x/x|
| |          (\\\\`_.'
| |         .-`--'.  *snap*
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \   * * '"|"|
| |        \ \*woosh* | |
: :         \ \ * * * : :
. .          `'       . .

******************
*   Que pena!    *
* você falhou :( *
******************
            
        ''')
        else: print(u"Você teve %i erros\n"%pos)
    while True:#zoei o expediente aq... seria melhor fz uma função pra essa parte/como daria pra limpar?
        if win:
            end = input("\n\nDeseja jogar novamente?(S/N)\n**********\n* BONUS! * - adicione ate 2 palavras ao jogo (A)\n**********\n")[0].upper()
            if end=='A':
                addPalavra()
                end = input("\n\nDeseja jogar novamente?(S/N)\n")[0].upper()
        else:
            end = input("\n\nDeseja jogar novamente?(S/N)\n")[0].upper()
        if end=='N':
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
        print("\n\nVAMOS JOGAR NOVAMENTE!!\n\n\n\n\n")
        break