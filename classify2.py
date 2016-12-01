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


def class_ttt(train, lr, num_neur, ftransf, pesos):
    # Algortimos de treinamento para teste:
    if(train == 0):
        pass; #original 
    elif (train == 1):
        nl.trainf = nl.train.train_gdm
    elif (train == 2):
        nl.trainf = nl.train.train_gdx
    elif (train == 3):
        nl.trainf = nl.train.train_rprop
    else:
        pass
   
    # numero de neuronios na camada de saida
    middle_neur = 9
    if (num_neur == 0 ):
        pass;
    elif (num_neur == 1):
        middle_neur += 5
    elif (num_neur == 2):
        middle_neur -= 5
    else:
        pass

    # Rede neural com 9 neuronios de entrada - range [-0.5, 0.5], 9 neuronios  para a camada escondida (padrao), 1 para a saída
    net = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5]], [middle_neur, 1])

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

    #inicializar pesos
    if (pesos == 0):
        net.layers[0].np['w'][:]= math.sqrt( net.ci )
    elif (pesos == 1):
        net.layers[0].np['w'][:]= 0
    elif (pesos == 2):
        pass
    else: 
        pass
    
    #definindo funcao de tranferencia
    if( ftransf == 0):
        pass;
    elif (ftransf == 1):
        net.layers[-1].transf = nl.trans.LogSig()
    elif (ftransf == 2):
        net.layers[-1].transf = nl.trans.SoftMax()
    else:
        pass

    # Train networks
    print"\tTreinando redes..."        
    #Taxa de regularizacao:
    if (lr == 0):
        error = net.train(ti, tt, epochs=1200, show=100, goal=0.001)    
    elif (lr == 1):
        error = net.train(ti, tt, epochs=1200, show=100, goal=0.001, rr=0.1)    
    elif (lr == 2):
        error = net.train(ti, tt, epochs=1200, show=100, goal=0.001, rr=0.5)
    elif (lr == 3):
        error = net.train(ti, tt, epochs=1200, show=100, goal=0.001, rr=1.0)
    else:
        pass
    
    # Simulate networks
    print "\tSimulando Rede Neural"
    out = net.sim(vl)

    tr_inp.close()
    tr_targ.close()
    vl_inp.close()
    return error, out

def class_car3(train, lr, num_neur, ftransf, pesos):
    # Algortimos de treinamento para teste:
    if(train == 0 or train == 1):
        nl.trainf = nl.train.train_gdm #original
    elif (train == 2):
        nl.trainf = nl.train.train_gdx
    elif (train == 3):
        nl.trainf = nl.train.train_rprop
    else:
        pass
   
    # numero de neuronios na camada de saida
    middle_neur = 21
    if (num_neur == 0 ):
        pass;
    elif (num_neur == 1):
        middle_neur += 5
    elif (num_neur == 2):
        middle_neur -= 5
    else:
        pass


    # Rede neural com 21 neuronios de entrada - range [0.0, 1.0]
    # 21 neuronios  para a camada escondida, 4 para a saída
    # Função de transferencia padrao: transf = TanSig
    net = nl.net.newff([
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0], 
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0], 
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0], 
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0],
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0],
        [0.0, 1.0], [0.0, 1.0],[0.0, 1.0]], [middle_neur, 4])
   
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

    #inicializar pesos
    if (pesos == 0):
        net.layers[0].np['w'][:]= math.sqrt( net.ci )
    elif (pesos == 1):
        net.layers[0].np['w'][:]= 0
    elif (pesos == 2):
        pass
    else: 
        pass

    #definindo funcao de tranferencia
    if( ftransf == 0):
        pass;
    elif (ftransf == 1):
        net.layers[-1].transf = nl.trans.LogSig()
    elif (ftransf == 2):
        net.layers[-1].transf = nl.trans.SoftMax()
    else:
        pass

    # Train networks    
    print"\tTreinando redes..."
    error = net.train(, ctt, epochs=500, show=50, goal=0.001)
    #Taxa de regularizacao:
    if (lr == 0):
        error = net.train(cti, ctt, epochs=1200, show=100, goal=0.001)    
    elif (lr == 1):
        error = net.train(cti, ctt, epochs=1200, show=100, goal=0.001, rr=0.1)    
    elif (lr == 2):
        error = net.train(cti, ctt, epochs=1200, show=100, goal=0.001, rr=0.5)
    elif (lr == 3):
        error = net.train(cti, ctt, epochs=1200, show=100, goal=0.001, rr=1.0)
    else:
        pass
    
    # Simulate networks
    print "\tSimulando Rede Neural "    
    out = net.sim(cvl)
    
    ctr_inp.close()
    ctr_targ.close()
    cvl_inp.close()
    return error,  out
