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

# termo -> valor do termo atual da sequencia de Fibonacci (número atual)
# 1 -> 0
# 2 -> (1 + 0) -> 1
# 3 -> 1 + 0 = 1
# 4 -> 1 + 1 = 2
# 5 -> 2 + 1 = 3
# 6 -> 3 + 2 = 5
# 7 -> 5 + 3 = 8
# termo n -> termo n-1 + termo n-2 = ...
# fib(n) -> fib(n-1) + fin(n-2) + ...

# entrada de dados -> número de termos da sequencia de Fibonacci
termo = int(input("Digite o número de termos da sequencia de Fibonacci: "))

#
#############################################################################################################################
print('#############################################')
print("#                parte 1                    #")
print("#############################################")
#
'''
# aplicando a fomula
def fib(termo):
  return fib(termo-1) + fib(termo-2)

print(f"fib({termo}) = {fib(termo)}")
###########################################
# gera o seguinte erro
#    return fib(termo-1) + fib(termo-2)
#  [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
###########################################
'''


