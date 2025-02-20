import random
#Exercicios da disciplina programacao orientada a objetos
#1 Soma de duas variaveis'
variavel_um = 5
variavel_dois = 7 

print(variavel_um + variavel_dois)

#2 Soma de strings (Concatenacao)
string_a = "Quinhentos"
string_b = " e Vinte Cinco"

print(string_a + string_b)

#3 Impressao de variaveis diferentes
um_nome = "Fernando"
uma_saudacao = "Bem vindo"
um_saldo = 1572325.87

print(" %s, %s. O seu saldo e de: %.2f R$."
    % (uma_saudacao, um_nome, um_saldo))

#4 Tamanho de uma string
uma_string = "Esta string de exemplo serve para treinar"
print(len(uma_string))

#5 Funcao hello_world
def hello_world():
	print("Hello world!")

hello_world()

#6 Funcao de numero aleatorio
def numero_aleatorio():
	numero = random.random() * 100
	print("%.2f" %(numero))  

numero_aleatorio()
numero_aleatorio()

#7 Soma de dois inteiro2
def soma(numero1, numero2 = 5):
	print("O resultado da soma e %d" % (numero1 + numero2))
	
	
#8 Quatro operacoes (Funcao soma ja definida)

def subtracao(numero1, numero2):
	print("O resultado da subtracao e: %d" % (numero1-numero2))

def multiplicacao(numero1, numero2):
	print("O resultado da multiplicacao e: %.2f" % (numero1 * numero2)) 

def divisao(numero1, numero2):
	print("O resultado da divisao e: %.2f" % (numero1 / numero2))
	
soma(23,67)
subtracao(15,8)
multiplicacao(28,90)
divisao(920,4)

#9 Contador ate o penultimo numero dado
def contador(numero):
	if numero >= 0:
		for i in range(numero):
			print(i)
	else:
		print("Numero invalido")

contador(5)
contador(-1)

#10 Soma do numero 0 ao numero indicado
def soma_contador(numero):
	soma = 0
	for i in range(numero + 1):
		soma += i
	print("A soma dos numeros de 0 a %d 'e: %d!" % (numero, soma))

soma_contador(3)
soma_contador(20)

#11 Soma dos numeros pares
def soma_pares(numero):
	soma  = 0
	for i in range(numero + 1):
		if i % 2 == 0:
			soma += i
	print("A soma dos numeros pares de 0 a %d e: %d!" % (numero, soma))
	
soma_pares(2)
soma_pares(20)

#12 Separar as letras de uma string
def separa_string(string):
	for i in range(len(string)):
		print("- %s" %(string[i]))

separa_string("Elias")

#13 Numeros iguais soma, numeros diferentes subtrai

def soma_ou_subtrai(numero1, numero2):
	if numero1 == numero2:
		print("A operacao realizada foi soma e o resultado foi: %s" % (numero1 + numero2))
	else:
		print("A operacao realizada foi subtracao e o resultado foi: %s" % (numero1 - numero2))

soma_ou_subtrai(2,2)
soma_ou_subtrai(4,6)

#13 Par, impar ou zero
def par_impar_ou_zero(numero):
	if numero == 0:
		print("O numero e zero!")
	elif numero % 2 == 0:
		print("O numero e par")
	else:
		print("O numero e impar")

par_impar_ou_zero(0)
par_impar_ou_zero(2)
par_impar_ou_zero(3)

#14 Verificar se um numero e maior que 10 e menor que vinte ou um numero e menor ou igual a 10 ou
# maior ou igual a vinte

def entre_dez_e_vinte_ou_nao(numero):
	if (numero > 10) and (numero < 20):
		print("O numero e maior que dez e menor que vinte")
	else:
		print("O numero e menor ou igual a dez ou maior ou igual a vinte")

entre_dez_e_vinte_ou_nao(15)
entre_dez_e_vinte_ou_nao(10)
entre_dez_e_vinte_ou_nao(5)
entre_dez_e_vinte_ou_nao(20)
entre_dez_e_vinte_ou_nao(25)	

#15 Calculadora basica

def calculadora_basica(numero1, numero2, identificador):
	if identificador == "+":
		print("O resultado da soma é: %d" % (numero1 + numero2))
	elif identificador == "-":
		print("O resultado da subtração é: %d" % (numero1 - numero2))
	elif identificador == "*":
		print("O resultado da multiplicação é: %.2f" % (numero1 * numero2))
	elif identificador == "/":
		if numero2 != 0:
			print("O resultado da divisão é: %.2f" % (numero1 / numero2))
		else:
			print("Não tente quebrar esta calculadora!!!")
	else:
		print("Operador inválido!")

calculadora_basica(1,2,"+")
calculadora_basica(7,3,"-")
calculadora_basica(6,9,"*")
calculadora_basica(1,0,"/")
calculadora_basica(20,2,"/")
calculadora_basica(20,30,"%")

#16 Bomboneiere

def leitor_de_codigo_de_barras(codigo):
	
