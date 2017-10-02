#Estrita Alternância
from threading import Thread
import time

global turn

def regiaoCritica():
    time.sleep(1)   #Na região crítica será carregado um tempo de execução de 1
    #segundo

def processamentoA(times, delay):   #Função de processamentoA que tem as variáveis
    #times e delay como parâmetros de entrada
    global turn     #Variável global que informa ao programa qual processo deve esperar
    #e qual deve rodar
    for x in range(times):
        print ("Secao de Entrada A - ",x+1)     #É impresso na tela que esta rodando
        #a sessão A e o seu número para que seja ciente o número de processos já
        #rodados
        while (turn != 0):  #Enquanto o turn tiver valor diferente de 0 o programa
            #irá retornar para o começo e não executará região crítica do processo A
            continue
        print ("Regiao Critica A")  #Sessão de entrada
        regiaoCritica()     #Sessão crítica
        print ("Secao de Saida A")  #Sessão de saída
        turn = 1    #Nesta linha o turn terá valor de 1
        print ("Regiao nao critica A\n")    #Sessão restante
        time.sleep(delay)   #Haverá um tempo de espera de n segundos, cujo n tem
        #valor igual ao da variável delay

def processamentoB(times, delay):   #Função de processamentoB que tem as variáveis
    #times e delay como parâmetros de entrada
    global turn     #Variável global que informa ao programa qual processo deve esperar
    #e qual deve rodar
    for x in range(times):
        print ("Secao de Entrada B - ",x+1)          #É impresso na tela que esta rodando
        #a sessão B e o seu número para que seja ciente o número de processos já
        #rodados
        while (turn != 1): #Enquanto o turn tiver valor diferente de 1 o programa
            #irá retornar para o começo e não executará região crítica do processo B
            continue
        print ("Regiao Critica B")  #Sessão de entrada
        regiaoCritica()     #Sessão crítica
        print ("Secao de Saida B")  #Sessão de saída
        turn = 0    #Nesta linha o turn terá valor de 1
        print ("Regiao nao critica B\n")    #Sessão restante
        time.sleep(delay)   #Haverá um tempo de espera de n segundos, cujo n tem
        #valor igual ao da variável delay


print ("Exemplo de Estrita Aternancia")
execTimes = 5   #Define o número de execução de cada seção crítica em cada processo
turn = 0    #Define que a execução começará no processamentoA

#no processamento você pode passar quantas vezes que a exec e
#qual o tempo de delay para simular o efeito comboio
tA = Thread(target=processamentoA, args=(execTimes,2,))     #É criado um Thread para
#o processo A
tA.start()  #O Thread A é colocado para executar
tB = Thread(target=processamentoB, args=(execTimes,10,))    #É criado um Thread para
#o processo A
tB.start()  #O Thread B é colocado para executar
