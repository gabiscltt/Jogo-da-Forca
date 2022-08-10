import random

def sortearPalavra():
    if len(palavra)<8:
        for letra in palavra: 
            acerto.append('_')
        print(acerto)
    else:
        sortearLetra()

def sortearLetra():
    letrasorteada = random.choice(list(palavra))
    for letra in palavra:        
        if letrasorteada==letra:
            acerto.append(letrasorteada)
        else:
            acerto.append('_')
    print(acerto)

fimdojogo = False
sorteando = True
palavra=[]
while not fimdojogo:
    while len(palavra)==0:
        erros = []
        acerto = []
        banco = ['casa', 'bolo', 'sagacidade', 'motor', 'controle', 'massa', 'serenidade', 'ossos', 'lagartixa', 'pneu', 'carro', 'marreta', 'garrafa', 'pedal', 'letras', 'pandemia', 'inescrupuloso', 'versatilidade']
        palavra = random.choice(banco)
        print('A PALAVRA SORTEADA É:')
        sortearPalavra()
        break

    def validarLetra(t):       
        if t in palavra:
            contador = 0
            for letra in palavra:
                if t==letra:            
                    acerto[contador]=(t)       
                contador += 1
            print('Você acertou!')
            print(acerto)
        else:
                erros.append(t)
                print('Você errou!')
                print(erros)
                print(' ')
                desenho()

    def desenho():
        if len(erros)==1:
            print("""+---+
    |   O""")
        elif len(erros)==2:
            print("""+---+
    |   O
    |  /""")
        elif len(erros)==3:
            print("""+---+
    |   O
    |  /|""")
        elif len(erros)==4:
            print("""+---+
    |   O
    |  /|\ """)
        elif len(erros)==5:
            print("""+---+
    |   O
    |  /|\ 
    |  /  """)
        elif len(erros)==6:
            print('Não foi desta vez!')
            print(' ')
            print("""+---+
    |   O
    |  /|\ 
    |  / \ 
    +=======""")

   
    tentativa = input('Digite uma letra.')
    validarLetra(tentativa)

    if len(erros)==6:
        print('Você perdeu!')
        jogardnv = input('''Deseja jogar novamente? 
    1 = SIM e 2= NÃO''')
        if jogardnv=='2':
            print('Jogo encerrado por aqui.')
            fimdojogo=True
        else:
            palavra = []
            continue

    elif acerto==list(palavra):
        print('Você venceu!')
        jogardnv = input('Deseja jogar novamente? 1 = SIM e 2= NÃO')
        if jogardnv=='2':
            print('Jogo encerrado por aqui.')
            break
        else:
            palavra = []
            continue
