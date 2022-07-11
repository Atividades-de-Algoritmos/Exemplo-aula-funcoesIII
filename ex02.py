#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 11/07/2022
##
# https://super.abril.com.br/mundo-estranho/o-que-e-a-sequencia-de-fibonacci/
#
# Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência:
# 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ...

#########################################################
# fibonacci sem recursão
#
#########################################################

# entrada de dados -> número de termos da sequencia de Fibonacci
termo = int(input("Digite o número de termos da sequencia de Fibonacci: "))

#
#############################################################################################################################
print('#############################################')
print("#                parte 1                    #")
print("#############################################")
#

def fib1(termo): # escreve a série de Fibonacci até o termo n-ésimo
  a, b = 0, 1 # inicializa a série de Fibonacci com 0 e 1 como primeiros termos
  while termo > 0: # enquanto o termo não for atingido
    print(b, end=' ') # imprime o termo atual da série
    a, b = b, a + b # atualiza os termos da série de Fibonacci
    termo -= 1  # decrementa o termo

# saida de dados -> série de Fibonacci
print("Série de Fibonacci:")
fib1(termo)
print("--------------------------------------------")
#
#############################################################################################################################
print('#############################################')
print("#                parte 2                    #")
print("#############################################")
#

def fib2(termo):
  resultado = []
  a, b = 0, 1
  while termo > 0:
    resultado.append(b)
    a, b = b, a + b
    termo -= 1  # decrementa o termo
  return resultado

# saida de dados -> série de Fibonacci
print("Série de Fibonacci:")
print(f"fib({termo}) = {fib2(termo)}", end='')
