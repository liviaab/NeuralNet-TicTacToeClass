# -*- coding: utf-8 -*-
# python ttt.py "Bases/tic-tac-toe.data"
import sys
import time
import pprint
import neurolab as nl
import numpy as np
import pylab as pl
import math
from aux import *


def class_ttt():
    # Algortimos de treinamento para teste:
    # nl.trainf = nl.train.train_gdm 
    # nl.trainf = nl.train.train_gdx
    # nl.trainf = nl.train.train_rprop 
    
    # Rede neural com 9 neuronios de entrada - range [-0.5, 0.5]
    # 9 neuronios  para a camada escondida, 1 para a saída
    # Função de transferencia padrao: transf = TanSig
    # testar com LogSig, SoftMax - modificar no newff
    net = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5]], [9, 1])

    tr_inp = open("ttt/tr_inp.data", 'r')       # entrada para treino
    tr_targ = open("ttt/tr_targ.data", 'r')     # saída esperada para treino 
    vl_inp = open("ttt/vl_inp.data", 'r')       # entrada para a validacao/generalizacao da rede
     
    # listas <- arquivos
    ti = []
    for line in tr_inp:
        line = line.rstrip()
        line = line.split(",")
        aux = []
        for k in line:
            aux.append( float(k) )
        ti.append(aux)

    tt = []
    for line in tr_targ:
        tt.append([float(line.strip())])

    vl = []
    for line in vl_inp:
        line = line.rstrip()
        line = line.split(",")
        aux = []
        for k in line:
            aux.append( float(k) )
        vl.append(aux)

    # Train networks
    print"\tTreinando redes..."
    nl.trainf = nl.train.train_gdm
    error = net.train(ti, tt, epochs=500, show=100, goal=0.001)    

    # Simulate networks
    print "\tSimulando Rede Neural"
    out = net.sim(vl)

    # o1 = open("saidas/o1.data", 'w')
    # for i in out:
    # 	o1.write(str(int(i))+"\n")
    # o1.close()
    #ploteresults(error, "Erro TTT")
    tr_inp.close()
    tr_targ.close()
    vl_inp.close()
    return error, out

def class_car3():
    # Modificando método de treinamento da rede - 
    nl.trainf = nl.train.train_gdm #original
    # nl.trainf = nl.train.train_gdx
    # nl.trainf = nl.train.train_rprop 
    

    # Rede neural com 21 neuronios de entrada - range [0.0, 1.0]
    # 21 neuronios  para a camada escondida, 4 para a saída
    # Função de transferencia padrao: transf = TanSig
    # testar com LogSig, SoftMax - modificar no newff
    net = nl.net.newff([
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0], 
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0], 
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0], 
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0],
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0],
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0]], [21, 4])
   
    ctr_inp = open("car3/c3tr_inp.data", 'r')       # entrada treino
    ctr_targ = open("car3/c3tr_targ.data", 'r')     # target treino
    cvl_inp = open("car3/c3vl_inp.data", 'r')       # entrada validação
     
    # listas <- arquivos 
    cti = []
    for line in ctr_inp:
        line = line.rstrip()
        line = line.split(",")
        aux = []
        for k in line:
            aux.append( float(k) )
        cti.append(aux)

    ctt = []
    for line in ctr_targ:
        line = line.rstrip()
        line = line.split(",")
        ctt.append([ float(line[0]),float(line[1]),float(line[2]),float(line[3]) ])

    cvl = []
    for line in cvl_inp:
        line = line.rstrip()
        line = line.split(",")
        aux = []
        for k in line:
            aux.append( float(k) )
        cvl.append(aux)

    # Train networks    
    print"\tTreinando redes..."
    error = net.train(cti, ctt, epochs=500, show=50, goal=0.001)
    
    # Simulate networks
    print "\tSimulando Rede Neural "    
    out = net.sim(cvl)
    
    # o3 = open('saidas/o3.data', 'w')
    # for i in out:
    #     o3.write(str(int(i[0]))+","+str(int(i[1]))+","+str(int(i[2]))+","+str(int(i[3]))+"\n" )
    # o3.close()
    # ploteresults(error, "Erro Car3") 
    ctr_inp.close()
    ctr_targ.close()
    cvl_inp.close()
    return error,  out

def main():
    inp = sys.argv[1]
    inp = int(inp)
    repeticoes = 30
    erros = []
    saidas = []
    listacc = []
    lporctacc = []
    erromedio = []
    errovarnc = []
    errodsvp = []    

    if inp == 1:

        for i in range(0, repeticoes):
            print "\t", i, "Iteracao"
            erro, saida = class_ttt()
            erros.append(erro)
            saidas.append(saida)

        # erromedio = mediaaritm(erros)
        # errovarnc = variancia( erros, erromedio)
        # errodsvp = desviopadrao(errovarnc)
        # diferenças dos valores esperados para o reultado da validacao:
        listacc, lporctacc = diffsaidasttt(saidas, "ttt/vl_targ.data")  

        # # plotar os graficos com as informações de erro para cada geração
        # pl.subplot(211)
        # l1, l3 = pl.plot(erromedio, '-',  errodsvp, '--')
        # pl.legend((l1,l3), ('Err Medio',  "Desvio Padrao"), loc='upper right', shadow=False)
        # pl.ylabel("Erros")
        # pl.xlabel("Epocas (min)")
        # pl.title('Epocas x  Erros e DesvioP ')        

        # #plotar graficos para variação da saida nas 30 execucoes
        # pl.subplot(212)
        # l2,l4 = pl.plot( listacc, 'ro', lporctacc,'g^')
        # pl.legend( (l2,l4), ("Num acertos", "Porcentagem"), loc='upper right', shadow=False)
        # pl.ylabel("Acertos")
        # pl.xlabel("Qtde inputs")
        # pl.title(" Inputs x Acertos")
        # pl.axis([-1, repeticoes +10 , -1, len(saidas[0])+20])
        # pl.show()

    elif inp == 2:
        for i in range(0, repeticoes):
            print "\t", i, "Iteracao"
            erro, saida = class_car3()
            erros.append(erro)
            saidas.append(saida)

        # diferenças dos valores esperados para o reultado da validacao:
        listacc, lporctacc = diffsaidasttt(saidas, "car3/c3vl_.data")  

    else:
        print "Você não digitou uma opção válida."

    erromedio = mediaaritm(erros)
    errovarnc = variancia( erros, erromedio)
    errodsvp = desviopadrao(errovarnc)

    # plotar os graficos com as informações de erro para cada geração
    pl.subplot(211)
    l1, l3 = pl.plot(erromedio, '-',  errodsvp, '--')
    pl.legend((l1,l3), ('Err Medio',  "Desvio Padrao"), loc='upper right', shadow=False)
    pl.ylabel("Erros")
    pl.xlabel("Epocas (min)")
    pl.title('Epocas x  Erros e DesvioP ')        

    #plotar graficos para variação da saida nas 30 execucoes
    pl.subplot(212)
    l2,l4 = pl.plot( listacc, 'ro', lporctacc,'g^')
    pl.legend( (l2,l4), ("Num acertos", "Porcentagem"), loc='upper right', shadow=False)
    pl.ylabel("Acertos")
    pl.xlabel("Qtde inputs")
    pl.title(" Inputs x Acertos")
    pl.axis([-1, repeticoes +10 , -1, len(saidas[0])+20])
    pl.show()

main()