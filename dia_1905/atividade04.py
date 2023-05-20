#Faça uma função que receba como parâmetro um número inteiro e retorne o fatorial desse núme ro(o número vezes ele mesmo e todos os números antes dele até 0)

#fazer o fatorial
def fatorando(numero):
    multiplicacao = 1
    contador = 1
    while contador <= numero:
        multiplicacao = multiplicacao * contador
        contador = contador + 1
    return multiplicacao

#mostrar resposta, input para saber o número inteiro
def main():
    numero = int(input("Insira um número"))
    resultado = fatorando(numero)
    print(resultado)
    
main()