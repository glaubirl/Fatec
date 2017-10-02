#Semáfaro
from threading import Thread,Semaphore  #Além do sub-módulo Thread, o Semaphore também é importado para utilização de acquire e realease no programa
import time     #É importado a biblioteca time para que seja feito um tempo de
#execução

s = Semaphore()     #A variável s será o semáforo do programa que irá mostrar
#quando parar e quando voltar

def regiaoCritica():    #Criação da função de região crítica que irá executar um
    #tempo de execução de 1 segundo
    time.sleep(1)

def processamentoA(times, delay):   #Criação do processo A que irá receber times e
    #delay como parâmetros
    for x in range(times):
        print ("Secao de Entrada A - ",x+1)     #Sessão de entrada
        s.acquire()     #O semáforo avisa que entrará em sessão de execução exclusiva (crítica)
        print ("Regiao Critica A")
        regiaoCritica()     #Região Crítica em execução
        print ("Secao de Saida A")
        s.release()     #O semáforo libera a execução para as demais sessões do programa
        print ("Regiao nao critica A\n")
        time.sleep(delay)       #Tempo de execução é rodado com o valor de delay em segundos

def processamentoB(times, delay):   #É criado a função processamentoB que irá executar a região crítica de B
    for x in range(times):
        print ("Secao de Entrada B - ",x+1)
        s.acquire()     #O semáforo faz com que a região abaixo dela tenha a execução exclusiva
        print ("Regiao Critica B")        
        regiaoCritica()     #Região crítica é executada
        print ("Secao de Saida B")
        s.release()     #O programa libera a execução para as demais partes do programa
        print ("Regiao nao critica B\n")
        time.sleep(delay)   #Tempo de execução com valor de delay em segundos é executado


print ("Exemplo de Semafaro")
execTimes = 5   #Número de execução dos processos

tA = Thread(target=processamentoA, args=(execTimes,1,))     #Criação da thread A
tA.start()  #Thread A é executada
tB = Thread(target=processamentoB, args=(execTimes,5,))     #Criação da thread B
tB.start()  #Thread B é executada
