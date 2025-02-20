#Este é meu primeiro python.
um_nome = "joão"
uma_idade = 40
casado = False
altura = 1.75
frase = "Pô, bixo. Bacana!"
#Cria uma variavel e multiplica a sting de frase com uma adição de espaço sete vezes
sete_po = (frase + " ") * 7
print("Hello, world!")
print("O nome do usuário fictício é: " + um_nome)
#Em python não é possivel concatenar uma string com outro tipo de dado, os outros tipos devem ser convertidos para string.
print("A idade do usuário fictício é: " + str(uma_idade))
print("O usuário fictício é casado? " + str(casado))
print("A altura do usuário ficticio é:" + str(altura))
print("A quantidade de letras que compõe o nome do usuário é " + str(len(um_nome)))
#Imprimindo partes da variavel frase
print(frase[:2])
print(frase[4:9])
print(frase[10:17])
print(sete_po)
#Retorna true se a string é achada na variavel, senão retorna false
print("Bacana!" in frase)
print("bacana" in frase)
print("uva" in frase)
print("O nome do usuário fictício é: " + um_nome + "\n" + frase)
#A função upper coloca todas as letras em maiúsculo, lower coloca todas em minúsculo, capitalize coloca só a primeira letra em maiúsculo.
print(frase.upper())
print(frase.lower())
print(um_nome.capitalize())
print( "%s Meu nome é %s.Eu tenho %d anos de idade e minha altura é %f metros!" % (frase,um_nome.capitalize(),uma_idade,altura))

#Listas
numeros_da_mega = [23,45,13]
print(numeros_da_mega)
#Imprime um numero na posição 3
print(numeros_da_mega[2])
#Adiciona dois numeros na lista
numeros_da_mega += [31,50]
print(numeros_da_mega)
#Adiciona um numero na lista usando a função append
numeros_da_mega.append(9)
print(numeros_da_mega)
#É possivel mudar o numero de um elemento da lista específico 
numeros_da_mega[0:1] = [41]
print(numeros_da_mega)
#Caso seja atribuido dois elementos da lista a um numero, um elemento será substituido e o outro excluido.
numeros_da_mega[1:3] = [5]
print(numeros_da_mega)
#Dois ou mais elementos da lista podem ser modificados de uma vez
numeros_da_mega[0:2] = [10,27]
print(numeros_da_mega)
#Caso o programador apresente um indice que não existe na lista, o numero será adicionado como um elemento novo.
numeros_da_mega[6:7] = [20]
print(numeros_da_mega)
#A adição implicita de elementos tambem funciona com mais de um número.
numeros_da_mega[6:8] = [43,11]
print(numeros_da_mega)

#Tuplas
naipes = ("Copas", "Paus", "Ouros", "Espadas")
ePau = (naipes[0] == "Paus")
print(ePau)

#Dicionários
notas = {"Ana": 8, "José":7.5, "Carlos": 9, "Maria":8.5}
print(notas)
#Imprime a nota de um aluno específico
print(notas["Ana"])
#Inclui uma nova nota
notas["Adamastor"] = 5
print(notas)
#Remove uma nota
del notas["José"]
print(notas)
print("Ana" in notas)
print("José" in notas)
#if, else e elif
if notas["Ana"]==8:
    print("É nota oito")
else:
    print("não é nota oito")
for i in range(10):
    print(i)
numero = 10
while numero>=1:
    print(numero)
    numero -= 1
    count = 0
while True:
    print(count)
    count += 1
    if count >=7:
        break
for i in range (10):
    if i == 5:
        continue
    print(i)
def hello_person(person):
    print("%s, Olá!" % person)

hello_person("Marcos")
hello_person("Maria")

def multiplica(a, b=2):
    return a*b
c = multiplica (5)
d = multiplica (10,5)
print(c)
print(d)

teste = {}

teste1 = {
    "subteste" : 10,
    "subteste2" : 30

}
teste2 = {
    "subsubteste" : 40,
    "subsubteste2" : 60  
}

teste.update({"teste1" : teste1})
teste.update({"teste2" : teste2})
print(str(teste))
