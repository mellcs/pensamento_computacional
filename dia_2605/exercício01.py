'''
#crie uma função recursiva que faça uma contagem regressiva a partir de um número digitado pelo usuário. ao chegar em 0, o programa deve exibir a mensagem: "decolar!"


#pedir número ao usuário
numero = int(input("Insira um número para fazermos a contagem regressiva:"))


#contar regressivamente
def contagem(numero):
    contador = numero

    while contador > 0:
        contador -= 1
    

#quando chegar em 0 exibir decolar
if contagem(numero) == 0:
    print("Decolar!")


#printar tudo
def main():
    resposta = contagem(contador)
    print(resposta)
    
------
'''
def contagem_regressiva(numero):
    if numero == 0:
        print("Decolar!")
    else:
        print(numero)
        contagem_regressiva(numero - 1)
        
def main():
    numero_digitado = int(input("Insira um número para fazermos a contagem regressiva:"))
    contagem_regressiva(numero_digitado)
    
main()