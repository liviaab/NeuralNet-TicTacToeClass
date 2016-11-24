# -*- coding: utf-8 -*-
# python ttt.py "Bases/tic-tac-toe.data"
import sys
import time
import pprint
import neurolab as nl
import numpy as np
import pylab as pl

def class_ttt():
    # create neural net with 3 inputs - input range [-0.5, 0.5]
    # 5 neuronios  para a camada escondida, 1 para a saída
    # 2 layers including hidden layer and output layer
    net = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5]], [9, 1])
    print "Neuronios entrada", net.ci
    print "Neuronios saida", net.co
    print "Numero camadas escondida+Saida", len(net.layers)
    print ""


    tr_inp = open("tr_inp.data", 'r')
    tr_targ = open("tr_targ.data", 'r')
    vl_inp = open("vl_inp.data", 'r')
     
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

    # Train networks
    print"Treinando redes. Goal: 0.001"
    error = net.train(ti, tt, epochs=500, show=50, goal=0.001)
    print"Tam conj de entrada:", len(ti), "Tam conj saida",  len(error)

    vl = []
    for line in vl_inp:
        line = line.rstrip()
        line = line.split(",")
        aux = []
        for k in line:
            aux.append( float(k) )
        vl.append(aux)

    # Simulate networks
    print "Simulando RN"
    out = net.sim(vl)
    print "Tamanho da entrada:", len(vl), "Tamanho da saida", len(out)

    o1 = open("o1.data", 'w')
    for i in out:
    	o1.write(str(int(i))+"\n")
    o1.close()

    # Plot results
    pl.subplot(221)
    pl.plot(error)
    pl.xlabel('Epoch number')
    pl.ylabel('error TTT (default SSE)')
    pl.show()

def class_car():
    # create neural net with 3 inputs - input range [-0.5, 0.5]
    # 5 neuronios  para a camada escondida, 1 para a saída
    # 2 layers including hidden layer and output layer
    net = nl.net.newff([[0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0],[-1.0, 1.0],[-1.0, 1.0],[-1.0, 1.0]], [9, 2])
    print "Neuronios entrada", net.ci
    print "Neuronios saida", net.co
    print "Numero camadas escondida+Saida", len(net.layers)
    print ""

    ctr_inp = open("ctr_inp.data", 'r')
    ctr_targ = open("ctr_targ.data", 'r')
    cvl_inp = open("cvl_inp.data", 'r')
     
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
        ctt.append([ float(line[0]), float(line[1]) ])


    # Train networks    
    print"Treinando redes. Goal: 0.001"
    error = net.train(cti, ctt, epochs=500, show=50, goal=0.001)
    print "Tam conj de entrada:", len(cti), "Tam conj saida", len(error)

    cvl = []
    for line in cvl_inp:
        line = line.rstrip()
        line = line.split(",")
        aux = []
        for k in line:
            aux.append( float(k) )
        cvl.append(aux)

    print "Simulando RN"
    # Simulate networks
    out = net.sim(cvl)
    print "Tamanho da entrada:", len(cvl), "Tamanho da saida", len(out)

    o2 = open("o2.data", 'w')
    for i in out:
        
        o2.write(str(int(i[0]))+","+str(int(i[1]))+"\n")
    o2.close()

    # Plot results
    pl.subplot(221)
    pl.plot(error)
    pl.xlabel('Epoch number')
    pl.ylabel('error car (default SSE)')
    pl.show()  

def class_car2():
    # create neural net with 3 inputs - input range [-0.5, 0.5]
    # 5 neuronios  para a camada escondida, 1 para a saída
    # 2 layers including hidden layer and output layer
    net = nl.net.newff([[0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],[0.0, 1.0], [0.0, 1.0], [-1.0, 1.0],[-1.0, 1.0],[-1.0, 1.0]], [15, 4])
    print "Neuronios entrada", net.ci
    print "Neuronios saida", net.co
    print "Numero camadas escondida+Saida", len(net.layers)
    print ""

    ctr_inp = open("c2tr_inp.data", 'r')
    ctr_targ = open("c2tr_targ.data", 'r')
    cvl_inp = open("c2vl_inp.data", 'r')
     
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


    # Train networks    
    print"Treinando redes. Goal: 0.001"
    error = net.train(cti, ctt, epochs=500, show=50, goal=0.001)
    print "Tam conj de entrada:", len(cti), "Tam conj saida", len(error)

    cvl = []
    for line in cvl_inp:
        line = line.rstrip()
        line = line.split(",")
        aux = []
        for k in line:
            aux.append( float(k) )
        cvl.append(aux)

    print "Simulando RN"    
    # Simulate networks
    out = net.sim(cvl)
    print "Tamanho da entrada:", len(cvl), "Tamanho da saida", len(out)

    o3 = open('o3.data', 'w')
    for i in out:
        o3.write(str(int(i[0]))+","+str(int(i[1]))+","+str(int(i[2]))+","+str(int(i[3]))+"\n" )
    o3.close()

    # Plot results
    pl.subplot(221)
    pl.plot(error)
    pl.xlabel('Epoch number')
    pl.ylabel('error car 2 (default SSE)')
    pl.show()  


inp = sys.argv[1]
inp = int(inp)

if inp == 1:
    class_ttt()
elif inp == 2:
    class_car()
elif inp == 3:
    class_car2()
else:
    print "Você não digitou uma opção válida."