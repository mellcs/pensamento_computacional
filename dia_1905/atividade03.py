#Implemente uma função que retorne a raiz quadrada de um número digitado 

# fazer raiz do número
def raizes (numero):
    raiz = numero ** 0.5
    return raiz

#mostrar resultado, input pro numero desejado
def main():
    numero = int(input("Insira um número para saber sua raiz quadrada:"))
    resposta = raizes(numero)
    print(resposta)

main()