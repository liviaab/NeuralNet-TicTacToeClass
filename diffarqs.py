import sys
import pprint


def diff(arq1, arq2):
	arq1 = open(arq1, 'r')
	arq2 = open(arq2, 'r')

	j = 0
	arq1dt =[]
	arq2dt =[]

	for line in arq1:
		arq1dt.append(line)

	for line in arq2:
		arq2dt.append(line)

	#if len(arq1dt) < len(arq2dt) else len(arq2dt)
	for i in range(0, (len(arq1dt) )  ):
		if arq1dt[i] == arq2dt[i]:
			j +=1

	print "Acertos: ",j,"Porcentagem: ", float( float(j) / float(len(arq1dt))) * 100.0 , "%"
	arq1.close()
	arq2.close()


arq1 = sys.argv[1]
arq2 = sys.argv[2]
diff(arq1, arq2)
