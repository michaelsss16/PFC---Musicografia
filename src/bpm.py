import time 
def RetornarBpm():
    finalizar = False
    while not finalizar:
        print('Pressione a tecla enter oito vezes no ritmo desejado.')
        input()
        a = time.time()
        input()
        b = time.time()
        input()
        c = time.time()
        input()
        d = time.time()
        input()
        e = time.time()
        input()
        f = time.time()
        input()
        g = time.time()
        input()
        h = time.time()

        media = ((b-a)+(c-b)+(d-c)+(e-d)+(f-e)+(g-f)+(h-g))/7
        bpm = int(60/media)
        print(bpm)
        val = input('0- realizr nova medição/n 1- Utilizar o bpm amostrado/n 2- Inserir bpm manualmente')
        if val == '0':
            finalizar = False
        if val == '1':
            return bpm
        if val == '2':
            #tratativa do int 
            return int(input('Bpm:'))


RetornarBpm()