from random import choices as sorteia
from time import sleep
from os import get_terminal_size as screen_wxh, getcwd
from platform import system as os_type
import sys 
print (getcwd())
if os_type() == 'Windows':
    from inputimeout import inputimeout, TimeoutOccurred
    import winsound
    os_iswin=True
elif os_type() == 'Linux':
    import select
    from playsound import playsound
    os_iswin=False
else:
    print ("No Apple/Android Users Supported")
    exit()




marcas = list()
with open ('marcas.txt') as f:
    for line in f.readlines():
        marcas.append(line.strip())

def solto_ponto(pontim_wav):
    global os_iswin
    if os_iswin:
        winsound.PlaySound(pontim_wav, winsound.SND_FILENAME)
    else:
        path = str(getcwd()+'/')
        pontim_wav = path + pontim_wav
        playsound(pontim_wav)
    return

def timer_win(t):
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    timer += "\r"
    try:
        i = inputimeout(prompt=timer, timeout=1)
    except TimeoutOccurred:
        i = None
    return i

def timer_lin(t):
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    sys.stdout.write(timer + "\r")
    sys.stdout.flush()
    i, o, e = select.select( [sys.stdin], [], [], 1 )
    if not i:
        i = None
    return i
        

def countdown(t):
    global os_iswin
    while t:
        if os_iswin:
            i = timer_win(t)
        else:
            i = timer_lin(t)
        t -=1
        if i != None:
            print('\n\n VOCÊ ACERTOU!\n\n')
            solto_ponto("etetra.wav")
            return False
    solto_ponto("acabou.wav")  
    print('\n\n FIM DO TEMPO!\n\n')
    return True

def rodada():
    marca = sorteia(marcas)[0]
    print('\n\n\n',marca,'\n'*(int(screen_wxh()[1]) +2))
    #print(marca,'\n'*40)
    if input('Olhe a marca acima, deseja trocar ou continuar?\n(t/c)').upper().startswith('T'):
        rodada()
    if countdown(60):
        if input('Sabe qual a marca?\n(s/n):').lower().startswith('n'):
            print ('\n\n ERROU!!! \n\n')
            solto_ponto("errou.wav")
        else:
            print ('\n\n\ O tempo acabou\n mas você acertou!\n\n Parabéns!\n\n')
            solto_ponto("etetra.wav")
    
    if input("A marca era %s \n\nmais uma?\n(s/n):"%marca).lower().startswith('n'):
        print(u'\n\nAdeus, até a próxima\n\n')
        sleep(3)
        exit()    
    rodada()
    


rodada()
