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
#net.trainf = nl.train.train_cg

print"Treinando redes. Goal: 0.001"
error = net.train(ti, tt, epochs=500, show=10, goal=0.001)
print len(error)

vl = []
for line in vl_inp:
    line = line.rstrip()
    line = line.split(",")
    aux = []
    for k in line:
        aux.append( float(k) )
    vl.append(aux)

# Simulate networks
out = net.sim(vl)

print "Saida"
for i in out:
	print int(i)

# Plot results
pl.subplot(221)
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('error (default SSE)')
pl.show()

