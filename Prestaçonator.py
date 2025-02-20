prestacao2 = {"Rotativos":{"Alternativos":{"Quantidade": 0,"Valor": 0},"Avulsos":{"Quantidade":0,"Valor":0},"Convênios":{"Quantidade":0,"Valor":0},"Cliente Excedente":{"Quantidade:":0,"Valor":0},"Hóspedes":{"Quantidade":0,"Valor":0},"Moto":{"Quantidade": 0,"Valor": 0},"Total":{"Quantidade":0,"Valor":0}},"Mensalidades":{"Pagamento depósito bancário":{"Quantidade":0,"Valor":0},"Pagamento de mensal na filial":{"Quantidade":0,"Valor":0},"Total":{"Quantidade": 0,"Valor": 0}},"Pagamentos em cartão":{"Débito":{"Quantidade":0,"Valor":0},"Crédito":{"Quantidade":0,"Valor":0},"Total":{"Quantidade":0,"Valor":0}},"Sem parar":{"Quantidade":0,"Valor":0},"Pix":{"Quantidade":0,"Valor":0},"Cancelamentos":{"Quantidade":0,"Valor":0},"Total da receita":0,"Valor em dinheiro":0}
prestacao = {}
def saudacao():
    print("*******Bem Vindo ao Prestaçonator*******")
    print("Qual sistema você está usando? (1)Jump (2)SigaPark (3)Prosiga")
    escolhasistema()

def escolhasistema():
    sistema = int(input("Sistema:"))
    if (sistema != 1 and sistema != 2 and sistema != 3):
        print("Numero da operação invalido, encerrando o programa...")
        return
    
    if sistema == 1:
        jump()
    elif sistema == 2:
        print(sistema)
    elif sistema == 3:
        print(sistema)

def jump():

    print("*****Por favor, insira os dados a seguir*****")
    #Função rotativos
    rotativos()
    conveniosJump()
    print("*******Cartões*******")
    #Função input débito
    debitoJump()
    #Função input Crédito
    creditoJump()
    #Função input pix
    pix()
    #Função input cancelamento
    cancelamentos()
    calculoTotais()
    valorDinheiro()
    imprimirPrestacao()

def rotativos():
    print("*****Rotativos*****")
    rotativo ={
        "Quantidade" : int(input("Quantidade de Rotativos:")),
        "Valor" : float(input("Valor do rotativo:"))
    }
    return rotativo
    
def conveniosJump():

    convenio = {
        "Quantidade" : int(input("Quantidade de convênios acima de 30 reais:")) + int(input("Quantidade de Convenios acima de 60 reais:")),
        "Valor" : float(input("Valor do convenio acima de 30 reais:")) + float(input("Valor do convênio acima de 60 reais:"))
    }
    return convenio
    
    

def debitoJump():
    print("*******Débito:*******")
    debito = {
        "Quantidade" : int(input("Quantidade de pagamentos em débito(Digite 0 se não houver):")),
        "Valor" : float(input("Valor dos pagamentos em débito(Digite 0 se não houver):")) 
    }
    

def creditoJump():
    print("*******Crédito:*******")
    credito = {
        "Quantidade" : int(input("Quantidade de pagamentos em crédito(Digite 0 se não houver):")),
        "Valor" : float(input("Valor dos pagamentos em crédito(Digite 0 se não houver):"))
    }

def obterPix():
    print("*******PIX*******")
    print("Digite o valor de cada pix (Digite 0 para encerrar):")
    pixVal = 0
    pixQTD = 0
    while True:
        valor = float(input("Valor:"))
        pixVal += valor
        pixQTD += 1
        if valor == 0:
            break
    pix = {
        "Quantidade" : pixQTD,
        "Valor" : pixVal
    }
      


def obterCancelamentos():
    print("*****Cancelamentos*****")
    print("Digite o valor de cada cancelamento (Digite 0 para encerrar):")
    cancelaVal = 0
    cancelaQTD = 0
    while True:
        valor = float(input("Valor:"))
        cancelaVal += valor
        cancelaQTD += 1
        if valor == 0:
            break
    cancelamentos = {
        "Quantidade" : cancelaQTD,
        "Valor" : cancelaVal
    }
        

def calculoTotais():
    prestacao["Rotativos"]["Total"]["Quantidade"] = prestacao["Rotativos"]["Avulsos"]["Quantidade"] + prestacao["Rotativos"]["Convênios"]["Quantidade"]
    prestacao["Rotativos"]["Total"]["Valor"] = prestacao["Rotativos"]["Avulsos"]["Valor"] + prestacao["Rotativos"]["Convênios"]["Valor"]
    prestacao["Pagamentos em cartão"]["Total"]["Quantidade"] = prestacao["Pagamentos em cartão"]["Débito"]["Quantidade"] + prestacao["Pagamentos em cartão"]["Crédito"]["Quantidade"]
    prestacao["Pagamentos em cartão"]["Total"]["Valor"] = prestacao["Pagamentos em cartão"]["Crédito"]["Valor"] + prestacao["Pagamentos em cartão"]["Débito"]["Valor"]

def valorDinheiro():
    prestacao["Valor em dinheiro"] = prestacao["Rotativos"]["Total"]["Valor"] - prestacao["Pagamentos em cartão"]["Total"]["Valor"]
    print("O valor em dinheiro é %d" % prestacao["Valor em dinheiro"])

def imprimirPrestacao():
    print("**********************************************************************\n*******************************Prestação*******************************\n**********************************************************************\n")
    for x, item in prestacao.items():
        if type(item) == dict:
            print ("*****" + x + "*****")
            for y, subitem in item.items():
                if type(subitem) == dict:
                    print("*****" + y + "*****")
                    for z,subsubitem in subitem.items():
                        print(z + " : " + str(subsubitem))
                else:
                    print( y + " : " + str(subitem))
                
        else:
            print(x + " : "+ str(item))

saudacao()       



