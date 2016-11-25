# funcoes auxiliares para calcular os erros dos testes
import math
import time
import pprint

def mediaaritm(valores):
	# valores = lista de listas
	mediafin = []
	minimo = len(valores[0])
	for lista in valores:
		if len(lista) < minimo:
			minimo = len(lista)

	for k in range(0, minimo):
		mediafin.append(0.0)
	
	for lista in valores:
		for i in range(0, minimo):
			mediafin[i] += lista[i]

	for k in mediafin:
		k = k/len(valores)

	return mediafin

def variancia( valores, media):
	var = []

	for k in range(0, len(media)):
		var.append(0.0)
	
	for lista in valores:
		for i in range(0, len(media)):
			var[i] = var[i] + math.pow(( lista[i] - media[i]), 2)

	for v in var:
		v = v/len(valores)

	return var

def desviopadrao( variancia ):
	dp = []
	for valor in variancia:
		dp.append( math.sqrt(valor) )
		
	return dp

def diffsaidasttt(saidas, target):
	target = open(target, 'r')
	obj = []
	for line in target:
		line = line.rstrip()
		line = int(line)
		obj.append(line)

	lisacc = []
	lptacc = []
	for saida in saidas:
		i = 0
		acertos = 0
		for o in saida:
			if int(o) == obj[i]:
				acertos += 1
			i += 1

		lisacc.append( acertos )
		lptacc.append( float(acertos)/float(len(saida)) * 100 )

	target.close()
	return lisacc, lptacc