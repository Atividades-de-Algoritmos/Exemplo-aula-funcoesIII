#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 11/07/2022

########################
# Funções anônimas:    #
########################

# O que é uma função lambda?
# Um lambda é simplesmente uma maneira de definir uma função em Python. Às vezes são conhecidos como
# operadores lambda ou funções lambda.

#############################################################################################################################
print('#############################################')
print("#                 parte 1:                  #")
print("#############################################")
## vamos ver uma função super básica definida da maneira “tradicional”: Aqui está uma
# função simples que duplica o valor passado.
def dobro1(x):  # função que duplica um número
  return x * 2  # retorna o dobro do número

print(dobro1(2)) # imprime 4



# Veja como fica como uma função lambda:

dobro2 = lambda x: x*2 # definindo a função lambda

print(dobro2(2))


# No exemplo acima, o lambda é construído como:
#####   lambda parâmetros:expressão   #########
# Sintaxe:
# lambda [arg1 [,arg2,.....argn]]:expressão

# Observe que em vez de usar def, a palavra-chave lambda é usada.
# Não são necessários parênteses. Qualquer coisa após a palavra-chave lambda
# é tratada como um parâmetro. Os dois pontos são usados para separar parâmetros
# e expressões. No nosso caso, a expressão é x*2.
# Não há necessidade de usar a palavra-chave return, o lambda faz isso automaticamente

# Você pode usar a palavra-chave lambda para criar pequenas funções anônimas. Essas funções são
# chamadas de anônimas porque não são declaradas da maneira padrão usando a palavra-chave def.

# Os formulários lambda podem receber qualquer número de argumentos, mas retornam apenas um valor
# na forma de uma expressão. Eles não podem conter comandos ou várias expressões.


# Uma função anônima não pode ser uma chamada direta para imprimir porque lambda requer uma expressão.
# As funções do Lambda têm seu próprio namespace local e não podem acessar variáveis que não estejam na lista de parâmetros e no namespace global.
# Embora pareça que os lambda são uma versão de uma linha de uma função, eles não são equivalentes a instruções embutidas em C ou C++, cuja finalidade é passar a alocação de pilha de função durante a invocação por motivos de desempenho.
#

# exemplos:
def parImpar1(valor): # função que retorna se um número é par ou impar
  if (valor % 2) == 0: # se o resto da divisão do número por 2 for 0, então o número é par
    return "par"
  else: # se o resto da divisão for diferente de 0, então o número é impar
    return "impar"

# ou:
parImpar2 = (lambda x: 'Impar' if (x % 2) else 'Par') # definindo a função lambda como parImpar2 (lambda x: 'Impar' if (x % 2) else 'Par')

print(parImpar2(2)) # imprime "Par"
print(parImpar2(3)) # imprime "Impar"