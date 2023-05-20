#Faça uma função que recebe três argumentos, e que retorne o produto desses três argumentos.

#resultado, multiplicação entre os três argumentos
def multiplicando(n1,n2,n3):
    multiplicacao = n1 * n2 * n3
    return multiplicacao
    
# return = retorna a parte específica da função (geralmente o resultado) para a função main/outras.

def main():
    n1 = int(input("Insira o primeiro número:"))
    n2 = int(input("Insira o segundo número:"))
    n3 = int(input("Insira o terceiro número:"))
    resultado = multiplicando(n1,n2,n3)
    print(resultado)
    
main()