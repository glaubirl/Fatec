#Solucao Peterson
from threading import Thread
import time

global turn, i, j, flag     #É criado a variável turn e uma lista que irá conter
# as variáveis i e j como parâmetros

def regiaoCritica():
    time.sleep(1)   #A região crítica roda um tempo de execução de 1 segundo

def processamentoA(times, delay):   #Criação da função processamentoA, cujos
    #parâmetros são times e delay
    global turn, i, j, flag
    for x in range(times):
        print ("Secao de Entrada A - ",x+1)     #Sessão de entrada
        flag[i] = True      #A flag de i é verdade
        turn = j    #Turn recebe valor de j
        while (flag[j] and turn == j):  #Enquanto a flag de j for verdade e o turn 
            #for de j o processamento executado é o B. Quando essa condição
            #for mentira esta será uma sessão de entrada
            continue
        print ("Regiao Critica A")  #Sessão crítica
        regiaoCritica()     #Chamada da região crítica
        print ("Secao de Saida A")  #Sessão de saída
        flag[i] = False     #A flag terá valor de falso
        print ("Regiao nao critica A\n")    #Sessão restante
        time.sleep(delay)   #Tempo de execução terá valor contido na variável delay

def processamentoB(times, delay):   #Criação do processo B
    global turn, i, j, flag
    for x in range(times):
        print ("Secao de Entrada B - ",x+1)     #É mostrado a sessão de entrada e
        #seu número para identificar quantos processos já foram feitos
        flag[j] = True  #A posição 1 da flag receberá valor True
        turn = i    #O turn recebe o valor de i
        while (flag[i] and turn == i):  #Enquanto o flag 0 for verdade e i igual ao
            #i, o processo B ficará em espera
            continue
        print ("Regiao Critica B")
        regiaoCritica()     #Região crítica do processo B é executado
        print ("Secao de Saida B")
        flag[j] = False     #A posição 1 da lista flag recebe o valor False
        print ("Regiao nao critica B\n")
        time.sleep(delay)   #Tempo de execução terá valor contido na variável delay


print ("Exemplo de Solucao de Peterson")
execTimes = 5   #Número de vezes que cada processo será executado
turn = 0    #Dá a vez para o processo A
i = 0   #I será posição 0 da lista flag
j = 1   #J será posição 1 da lista flag
flag = []   #Criação da lista flag
flag.append(False)  #Adiciona valor False à lista flag
flag.append(False)  #Adiciona um segundo valor False à lista flag

tA = Thread(target=processamentoA, args=(execTimes,1,))     #Criação do thread A
tA.start()  #Thread A é colocado para executar
tB = Thread(target=processamentoB, args=(execTimes,5,))     #Criação do thread B
tB.start()  #Thread B é colocado para executar
