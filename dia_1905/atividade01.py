#implemente uma calculadora (números reais) com suas funções básicas: soma, subtração, multiplicação e divisão.

#soma
def somatorio(n1, n2):
    soma = n1 + n2
    print(soma)
    
#subtração
def subtrair(n1, n2):
    subtracao = n1 - n2
    print(subtracao)
    
#multiplicação
def multiplicar(n1, n2):
    multiplicacao = n1 * n2
    print(multiplicacao)

#divisão
def dividir(n1, n2):
    divisao = n1 / n2
    print(divisao)

#mostrar resultado, dois inputs pra dois números, opção de operação

def main():
    n1 = int(input("Insira um número:"))
    n2 = int(input("Insira outro número:"))
    operacao = input("Digite a operação desejada (soma, subtração, multiplicação ou divisão):")

    if operacao == "soma":
        somatorio(n1, n2)
        
    elif operacao == "subtração" or operacao == "subtraçao":
        subtrair(n1, n2)
       
    elif operacao == "multiplicação" or operacao == "multiplicaçao":
        multiplicar(n1, n2)
        
    elif operacao == "divisão" or operacao == "divisao":
        dividir(n1, n2)
        
    
main()