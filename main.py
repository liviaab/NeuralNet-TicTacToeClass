# -*- coding: utf-8 -*-

from classify2 import *
from aux import *

def main():
    """
    Parametros:
    Primeiro: escolher qual problema a ser resolvido
    1 - tic-tac-toe
    2 - classificacao do carro

    Segundo:  metodo de treinamento da rede
    0 - original ( para car -> igual a 1 )
    1 - train_gdm (somente para ttt)
    2 - train_gdx 
    3 - train_rprop  

    Terceiro: Taxa de regularizacao
    0 - original/padrao - 0.01
    2 - 0.5
    3 - 1

    Quarto: Neuronio na camada escondida
    0 - original
    1 - +5
    2 - -5
    
    Quinto: Funcao de transformacao
    0 - original (TanSig)
    1 - LogSig
    2 - SoftMax

    Sexto:  Inicialização dos pesos
    0 - original ( sqrt(num neuronios na entrada)) / rand
    1 - 0
    2 - rand / sqrt(in)

    Setimo: numero de repeticoes
    livre - recomenda-se 0 < n < 50

    """


    inp = int(sys.argv[1])
    train = int(sys.argv[2])
    lr = int(sys.argv[3])
    num_neur = int(sys.argv[4])
    ftransf = int(sys.argv[5])
    pesos = int(sys.argv[6])
    repeticoes = int(sys.argv[7])

    erros = []
    saidas = []
    listacc = []
    lporctacc = []
    erromedio = []
    errovarnc = []
    errodsvp = []    

    #Impressao dos parametros
    print "------------------------------------------------------------"
    if(inp == 1):
        print "Problema: Tic Tac Toe"
    if(inp == 2):
        print "Problema: Classificacao Carro"

    print "Parametros escolhidos:"
    if(train == 0):
        print "Treinamento:\t\tPadrao - Broyden Fletcher Goldfarb Shanno"
    elif (train == 1):
        print "Treinamento:\t\tgdm - Gradient descent with momentum backpropagation"
    elif (train == 2):
        print "Treinamento:\t\tgdx - Gradient descent with momentum backpropagation and adaptive lr"
    elif (train == 3):
        print "Treinamento:\t\trprop - Resilient Backpropagation"
    else:
        train = 0
        print "Algortimo de treinamento padrao."    

    #Taxa de regularizacao:
    if (lr == 0):
        print "Taxa de regularizacao:\tPadrao - 0.0"
    elif (lr == 1):
        print "Taxa de regularizacao:\t0.5"
    elif (lr == 2):
        print "Taxa de regularizacao:\t1.0"
    else:
        lr = 0
        print "Taxa de regularizacao padrao."    

    #definindo funcao de tranferencia
    if( ftransf == 0):
        print "F Transferencia:\tPadrao - TanSig"
    elif (ftransf == 1):
        print "F Transferencia:\tLogSig"
    elif (ftransf == 2):
        print "F Transferencia:\tSoftMax"
    else:
        ftransf = 0
        print "F Transferencia padrao."  

    # numero de neuronios na camada de saida
    if (num_neur == 0 ):
        print "Neuronios na camada escondida:\tPadrao - 9"
    elif (num_neur == 1):
        print "Neuronios na camada escondida:\t14"
    elif (num_neur == 2):
        print "Neuronios na camada escondida:\t4"
    else:
        num_neur = 0 
        print "Numero de neuronios padrao."    

    #variacao dos pesos
    if(inp == 1):
        if (pesos == 0):
            print "Inicializacao Peso:\tPadrão - sqrt(in)"
        elif (pesos == 1):
            print "Inicializacao Peso:\t0"
        elif (pesos == 2):
            print "Inicializacao Peso:\tRand"
        else:
            pesos = 0
            print "Inicializacao Peso:\tPadrão - sqrt(in)"
    else:
        if (pesos == 0):
            print "Inicializacao Peso:\tPadrão - Rand "
        elif (pesos == 1):
            print "Inicializacao Peso:\t0"
        elif (pesos == 2):
            print "Inicializacao Peso:\tsqrt(in)"
        else:
            pesos = 0
            print "Inicializacao Peso:\tPadrão - sqrt(in)"

    print "------------------------------------------------------------"

    if inp == 1:
        for i in range(0, repeticoes):
            print i+1, "Iteracao"
            erro, saida = class_ttt(train, lr, num_neur, ftransf, pesos)
            erros.append(erro)
            saidas.append(saida)

        # diferenças dos valores esperados para o reultado da validacao:
        listacc, lporctacc = diffsaidasttt(saidas, "ttt/vl_targ.data")  

    elif inp == 2:
        for i in range(0, repeticoes):
            print "\t", i+1, "Iteracao"
            erro, saida = class_car3(train, lr, num_neur, ftransf, pesos)
            erros.append(erro)
            saidas.append(saida)

        # diferenças dos valores esperados para o reultado da validacao:
        listacc, lporctacc = diffsaidascar(saidas, "car3/c3vl_targ.data")  

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

    accm = 0 
    pctgm = 0.0
    for v in listacc:
        accm += v
    accm /= len(listacc)
    for v in lporctacc:
        pctgm += v
    pctgm /= len(lporctacc)

    print "Media de acertos: ", accm, "-", pctgm,"%"


main()