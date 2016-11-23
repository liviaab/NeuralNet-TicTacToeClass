import sys
import random

# from changeinp import *
# change_ttt("Bases/tic-tac-toe.data", "ttt.data")
def change_ttt(entrada, saida):
	# x ->	-0.5	o -> 0.5		b -> 0
	# positivo -> 1
	# negativo -> 0
	entrada = open(entrada, "r")
	saida = open(saida, "w")

	for line in entrada:
		line = line.split(",")

		if line[-1].rstrip() == "positive":
			line[-1] = '1'
		else:
			line[-1] = '0'

		for i in range(0,9) :
			aux = ''
			if line[i] == 'x':
				aux = -0.5
			elif line[i] == 'o':
				aux = 0.5
			else:
				aux = 0
			saida.write(str(aux) + "," )


		saida.write(line[-1]+ "\n")

	entrada.close()
	saida.close()

"""
# change_car("Bases/car.data", "car2.data")
def change_car(entrada, saida):
	# unacc -> 0	acc -> 1
	# good -> 2		vgood -> 3
	# MUDARR

	entrada = open(entrada, "r")
	saida = open(saida, "w")

	for line in entrada:
		line = line.split(",")

		if line[-1] == "unacc\n":
			line[-1] = '0'
		elif line[-1] == "acc\n":
			line[-1] = '1'
		elif line[-1] == "good\n":
			line[-1] = '2'
		else:
			line[-1] = '3'

		for i in range(0,10) :
			saida.write(line[i])
			if not i == 9:
				saida.write(",")
			else:
				saida.write("\n")

	entrada.close()
	saida.close()
"""

# ti, tt, vi, vt = separate_trainvalidtn_set("ttt.data")
def separate_trainvalidtn_set(entrada):
	entrada = open(entrada, "r")

	data = []
	train = []
	traintarget = []
	validation = []
	validationtarget = []

	for line in entrada:
		data.append(line)

	random.shuffle(data)

	for line in data:
		line = line.split(",")

		if len(train) >= len(data)*0.7:
			validationtarget.append([ float( line[-1].rstrip() ) ])
			a = []
			for i in range(0,9):
				a.append(float(line[i]))
			validation.append(a)

		else:
			traintarget.append([float(line[-1].rstrip() )])
			a = []
			for i in range(0,9):
				a.append(float(line[i]))
			train.append(a)


	print "Tamanho treino: ", len(train), "Tamanho Validacao: ",  len(validation), "Total: ", len(train)+len(validation)

	train_file = open("tr_inp.data", 'w')
	for i in train:
		for k in range(0, 9):
			if k == 8:
				train_file.write(str(i[k])+"\n")
			else:
				train_file.write(str(i[k])+",")
	train_file.close()

	traintarget_file = open("tr_targ.data", 'w')
	for i in traintarget:
		traintarget_file.write(str(i[0])+"\n")
	traintarget_file.close()

	validation_file = open("vl_inp.data", 'w')
	for i in validation:
		for k in range(0, 9):
			if k == 8:
				validation_file.write(str(i[k])+"\n")
			else:
				validation_file.write(str(i[k])+",")
	validation_file.close()

	validtarget_file = open("vl_targ.data", 'w')
	for i in validationtarget:
		validtarget_file.write(str(i[0])+"\n")
	validtarget_file.close()


change_ttt("Bases/tic-tac-toe.data", "ttt.data")
separate_trainvalidtn_set("ttt.data")
