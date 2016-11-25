import sys
import random

def change_ttt(entrada, saida):
	# x ->	-0.5		o -> 0.5		b -> 0
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

def separate_trvl_lists(entrada, tam):
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
			for i in range(0,tam):
				a.append(float(line[i]))
			validation.append(a)

		else:
			traintarget.append([float(line[-1].rstrip() )])
			a = []
			for i in range(0,tam):
				a.append(float(line[i]))
			train.append(a)

	print "Tamanho treino: ", len(train), "Tamanho Validacao: ",  len(validation), "Total: ", len(train)+len(validation)
	entrada.close()
	return train, traintarget, validation, validationtarget 

def separate_trainvalidtn_settt(entrada):
	train, traintarget, validation, validationtarget  = separate_trvl_lists(entrada, 9)

	train_file = open("ttt/tr_inp.data", 'w')
	for i in train:
		for k in range(0, 9):
			if k == 8:
				train_file.write(str(i[k])+"\n")
			else:
				train_file.write(str(i[k])+",")
	train_file.close()

	traintarget_file = open("ttt/tr_targ.data", 'w')
	for i in traintarget:
		traintarget_file.write(str(i[0])+"\n")
	traintarget_file.close()

	validation_file = open("ttt/vl_inp.data", 'w')
	for i in validation:
		for k in range(0, 9):
			if k == 8:
				validation_file.write(str(i[k])+"\n")
			else:
				validation_file.write(str(i[k])+",")
	validation_file.close()

	validtarget_file = open("ttt/vl_targ.data", 'w')
	for i in validationtarget:
		validtarget_file.write(str(int(i[0]))+"\n")
	validtarget_file.close()


def Ftodist(tipo):
	if tipo == 'vhigh' or tipo == '2'or tipo == 'unacc':
		return 1,0,0,0
	elif tipo == 'high' or tipo == '3' or tipo == 'acc':
		return 0,1,0,0
	elif tipo == "med"or tipo == '4' or tipo == "good":
		return 0,0,1,0
	else: #low ou 5more ou vgood
		return 0,0,0,1

def Ttodist(tipo):
	if tipo == "2" or tipo == "small" or tipo == "low":
		return 1, 0, 0
	elif tipo == "4" or tipo == "med":
		return 0, 1, 0
	else: #more, big ou high
		return 0, 0, 1

#------------------- car 3 dist 3 locais - nao usadas
def findclass3opt(tipo):
	if tipo == "2" or tipo == "small" or tipo == "low":
		return -1
	elif tipo == "4" or tipo == "med":
		return 0 	
	else: #more, big ou high
		return 1
		
def change_car_todist(entrada, saida):
	"""
	1 buying	vhigh, high, med, low 		1000,0100,0010,0001
	2 maint		vhigh, high, med, low 		1000,0100,0010,0001
	3 doors		2, 3, 4, 5more 				1000,0100,0010,0001
	4 persons	2, 4, more 					-1,0,1
	5 lug-boot	small, med, big 			-1,0,1
	6 safety	low, med, high 				-1,0,1
	7 Class		unacc, acc, good, vgood 	1000,0100,0010,0001

	"""
	entrada = open(entrada, 'r')
	saida = open(saida, 'w')
	
	for line in entrada:
		line = line.rstrip()
		line = line.split(",")
		#1
		a, b, c, d = Ftodist(line[0])
		#2
		e, f, g, h = Ftodist(line[1]) 
		#3
		i, j, k, l = Ftodist(line[2]) 
		#4
		m = findclass3opt(line[3])
		#5
		n = findclass3opt(line[4]) 
		#6
		o = findclass3opt(line[5]) 
		#7
		p, q, r, s= Ftodist(line[6])

		saida.write(str(a)+','+str(b)+','+str(c)+','+str(d)+','+str(e)+','+str(f)+','+str(g)+','+str(h)+','+str(i)+','+str(j)+','+str(k)+','+str(l)+','+str(m)+','+str(n)+','+str(o)+','+str(p)+','+str(q)+','+str(r)+','+str(s)+'\n')

	entrada.close()
	saida.close()

#------------------- car 6 dist 
def change_car_todistall(entrada, saida):
	"""
	1 buying	vhigh, high, med, low 		1000,0100,0010,0001
	2 maint		vhigh, high, med, low 		1000,0100,0010,0001
	3 doors		2, 3, 4, 5more 				1000,0100,0010,0001
	4 persons	2, 4, more 					100,010,001
	5 lug-boot	small, med, big 			100,010,001
	6 safety	low, med, high 				100,010,001
	7 Class		unacc, acc, good, vgood 	1000,0100,0010,0001

	"""
	entrada = open(entrada, 'r')
	saida = open(saida, 'w')
	
	for line in entrada:
		line = line.rstrip() 
		line = line.split(",") 
		#1 
		a, b, c, d = Ftodist(line[0]) 
		#2
		e, f, g, h = Ftodist(line[1])  
		#3
		i, j, k, l = Ftodist(line[2])  
		#4 
		m , n, o = Ttodist(line[3]) 
		#5 
		p, q, r = Ttodist(line[4])  
		#6 
		s, t, u = Ttodist(line[5])  
		#7 
		v, w, x, y=	Ftodist(line[6])

		saida.write(str(a)+','+str(b)+','+str(c)+','+str(d)+','+str(e)+','+str
		(f)+','+str(g)+','+str(h)+','+str(i)+','+str(j)+','+str(k)+','+str(l)+
		','+str(m)+','+str(n)+','+str(o)+','+str(p)+','+str(q)+','+str(r)+','+
		str(s)+','+str(t)+','+str(u)+','+str(v)+','+str(w)+','+str(x)+','+str(y)+'\n')

	entrada.close()
	saida.close()
	return

def separate_sets_cardistall(entrada):
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

		line = line.rstrip()
		line = line.split(",")
		
		if len(train) >= len(data)*0.75:
			validationtarget.append([ float( line[-4]), float( line[-3]), float( line[-2]), float( line[-1] ) ])
			a = []
			for i in range(0,21):
				a.append(float(line[i]))
			validation.append(a)

		else:
			traintarget.append([ float( line[-4]), float( line[-3]),float( line[-2]), float(line[-1] )])
			
			a = []
			for i in range(0,21):
				a.append(float(line[i]))
			train.append(a)

	print "Tamanho treino: ", len(train), "Tamanho Validacao: ",  len(validation), "Total: ", len(train)+len(validation)
	entrada.close()

	# train, traintarget, validation, validationtarget 
	train_file = open("car3/c3tr_inp.data", 'w')
	for i in train:
		for k in range(0, 21):
			if k == 20:
				train_file.write(str(i[k])+"\n")
			else:
				train_file.write(str(i[k])+",")
	train_file.close()

	traintarget_file = open("car3/c3tr_targ.data", 'w')
	for i in traintarget:
		for k in range(0,4):
			if k == 3:
				traintarget_file.write(str(float(i[k]))+"\n")	
			else:
				traintarget_file.write(str(float(i[k]))+",")	
	traintarget_file.close()

	validation_file = open("car3/c3vl_inp.data", 'w')
	for i in validation:
		for k in range(0, 21):
			if k == 20:
				validation_file.write(str(i[k])+"\n")
			else:
				validation_file.write(str(i[k])+",")
	validation_file.close()

	validtarget_file = open("car3/c3vl_targ.data", 'w')
	for i in validationtarget:
		for k in range(0, 4):
			if k == 3:
				validtarget_file.write(str(int(i[k]))+"\n")
			else:
				validtarget_file.write(str(int(i[k]))+",")
	validtarget_file.close()	

	return


change_ttt("Bases/tic-tac-toe.data", "ttt/ttt.data")
separate_trainvalidtn_settt("ttt/ttt.data")

# change_car_todist("Bases/car.data", "car/car2.data")
# separate_sets_cardist("car/car2.data")

change_car_todistall("Bases/car.data", "car3/car3.data")
separate_sets_cardistall("car3/car3.data")