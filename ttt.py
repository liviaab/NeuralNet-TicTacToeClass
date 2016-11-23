# -*- coding: utf-8 -*-
# python ttt.py "Bases/tic-tac-toe.data"
import sys
import time
import pprint
import neurolab as nl
import numpy as np
import pylab as pl

# create neural net with 3 inputs - input range [-0.5, 0.5]
# 5 neuronios  para a camada escondida, 1 para a saída
# 2 layers including hidden layer and output layer
net = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5]], [5, 1])
print "Net1 num neuronios entrada", net.ci
print "Net1 num neuronios saida", net.co
print "Net1 num camadas escondida+Saida", len(net.layers)
print ""
# create neural net with 5 inputs - input range [-0.5, 0.5]
# 5 neuronios  para as duas camadas escondidas, 1 para a saída
# 3 layers including hidden layer and output layer
# net2 = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5],[-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5], [-0.5, 0.5]], [5, 5, 1])
# print "Net2 num neuronios entrada", net2.ci
# print "Net2 num neuronios saida", net2.co
# print "Net2 num camadas escondida+Saida", len(net2.layers)


# Train networks
#net.trainf = nl.train.train_gd()
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

print"Treinando a rede. Goal: 0.001"
error = net.train(ti, tt, epochs=500, show=10, goal=0.001)
pprint.pprint(error)
print len(error)
#error2 = net2.train(tr_inp, tr_targ, epochs=500, show=1, goal=0.02)

print "Erro 1"
# pprint.pprint(error)

# print 'Erro 2'
#pprint.pprint(error2)

# Simulate networks
#out = net.sim(val_inp)
#out2 = net2.sim(val_inp)
#print "OUT 1"
#pprint.pprint(out)

# Plot results
pl.subplot(111)
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('error (default SSE)')
pl.show()

# pl.subplot(222)
# pl.plot(error2)
# pl.xlabel('Epoch number')
# pl.ylabel('error (default SSE)')
# pl.show()
