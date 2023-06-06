#Cálculo IMC

#IMC	                CLASSIFICAÇÃO	    OBESIDADE (GRAU)
#MENOR QUE 18,5	        MAGREZA	            0
#ENTRE 18,5 E 24,9	    NORMAL	            0
#ENTRE 25,0 E 29,9	    SOBREPESO	        I
#ENTRE 30,0 E 39,9	    OBESIDADE	        II
#MAIOR QUE 40,0	        OBESIDADE GRAVE	    III

magreza = 18.5
normal = 24.9
sobrepeso_1 = 29.9
obesidade_2 = 39.9
obesidade_3 = 40.0

def calc_imc():
    peso = float(input("Digite o seu peso......: "))
    altura = float(input("Digite a sua altura....: "))
    
    altura_total = altura * altura
    imc = peso / altura_total

    if (imc <= magreza):
        print(f'Seu IMC é {imc:.2f}. Sua classificação é MAGREZA.')
    elif (imc > magreza) and (imc <= normal):
        print(f'Seu IMC é {imc:.2f}. Sua classificação é NORMAL.')
    elif (imc > normal) and (imc <= sobrepeso_1):
        print(f'Seu IMC é {imc:.2f}. Sua classificação é SOBREPESO tipo I.')
    elif (imc > sobrepeso_1) and (imc <= obesidade_2):
        print(f'Seu IMC é {imc:.2f}. Sua classificação é OBESIDADE tipo II.')
    elif (imc > obesidade_2):
        print(f'Seu IMC é {imc:.2f}. Sua classificação é OBESIDADE tipo III.')
    else:
        print("Forneça a informação correta!")
    return imc

calc_imc()