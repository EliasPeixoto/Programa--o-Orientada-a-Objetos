import random
import re
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

#16 Codigo de barras
def analisador_codigo_de_barras(codigo):
    regex = re.compile('[0-9]*')
    soma_codigo = 0
    if len(regex.match(codigo).group()) == 10:
        for digito in codigo:
                soma_codigo += int(digito)
        if soma_codigo <= 15:
                print("Bomboniere")
        elif soma_codigo > 15 and soma_codigo <= 30:
                   print("Higiene")
        elif soma_codigo > 30 and soma_codigo <= 45:
                   print("Utensilios")
        elif soma_codigo > 45 and soma_codigo <= 60:
                   print("Congelados")
        elif soma_codigo > 60 and soma_codigo <= 75:
                   print("Bebidas")
        else:
                   print("Padaria")	       	
    else:
        print("O codigo deve possuir 10 digitos numericos!")
        
analisador_codigo_de_barras("a203948576")
analisador_codigo_de_barras("9999999999")
analisador_codigo_de_barras("4550000000")
analisador_codigo_de_barras("5555540000")
analisador_codigo_de_barras("5555559000")
analisador_codigo_de_barras("5555555525")
analisador_codigo_de_barras("5555559599")


#17 #18 #19 Classe de pessoa
#class Pessoa:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade 
#    
#    def __str__(self):
#        return ("Esta pessoa e o(a) %s e tem %d anos!" % (self.nome, self.idade))
#    
#    def apresentacao(self):
#        return ("Olá, meu nome é %s" % (self.nome))
#        
#pessoa_1 = Pessoa("Carlos", 26)
#
#print(pessoa_1)
#
#pessoa_1.nome = "Josefa"
#
#print(pessoa_1)
#
#class Empregado(Pessoa):
#
#    QTDEmpregado = 0
#
#    def __init__(self, nome, idade, matricula):
#        super().__init__(nome, idade)
#        self.matricula = matricula
#
#    def estipular_salario(self, salario):
#
#        self.salario = salario
#
#    def __str__(self):
#         return "Meu nome é %s, minha idade é %d e meu salário é %.2f" % (self.nome, self.idade, self.salario)
#    
#    def bater_ponto(self):
#        print("Funcionário %s de matrícula %d bateu o ponto!" % (self.nome, self.matricula))
#
#    
#   
#empregado_1 = Empregado("Carlos", 27, 7831409814)
#print(empregado_1.matricula)
#empregado_1.bater_ponto()

#20 Cachorros 

class Cachorro: 
    def __init__(self,cor,race,tamanho):
        self.cor = cor
        self.race = race
        self.tamanho = tamanho
    
    def latir (self):
        if self.tamanho <= 40:
            print("RauRau!")
        elif self.tamanho > 40 and self.tamanho <= 60:
            print("Auau!")
        else:
            print("RoufRouf!")

cachorro1 = Cachorro("Branco","Pincher", 35)
cachorro1.latir()

cachorro2 = Cachorro("Laranja", "Caramelo", 55)
cachorro2.latir()

cachorro3 = Cachorro("Preto", "Pastor Alemão", 75)
cachorro3.latir()

#21 Pessoas e CPFS
class Conta:
    def __init__(self, numero, saldo, titular, senha):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = titular
        self.__senha = senha
    
    def consulta_numero(self):
        print("O numero da conta é %d" % (self.__numero))
    def consulta_saldo(self):
        print("O seu saldo é de %.2f reais" % (self.__saldo))
    def consulta_titular(self):
        print("O titular da conta é %s" % (self.titular.consulta_nome()))
    def consulta_senha(self):
        print("A senha desta conta é %d" % (self.__senha))
    def sacar(self, valor, senha):
        if senha == self.__senha:
            if self.__saldo - valor >= 0:
                self.__saldo -= valor
                print("Voce sacou %.2f" % (valor))
            else:
                print("Saldo insuficiente!")
        else:
            print("Senha incorreta!")

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    def consulta_nome(self):
        return self.__nome

pessoa1 = Pessoa("Carlos")
conta1 = Conta(1, 10000, pessoa1, 1234)

conta1.consulta_saldo()
conta1.sacar(100,123412837)
conta1.consulta_saldo()
conta1.sacar(100,1234)
conta1.consulta_saldo()
conta1.sacar(100000000,1234)
conta1.consulta_saldo()