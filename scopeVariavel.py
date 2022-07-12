#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 11/07/2022

########################
# Scorpo das variáveis:#
########################
# Todas as variáveis em um programa podem não estar acessíveis em todos os locais desse programa.
# Isso depende de onde você declarou uma variável.

# O escopo de uma variável determina a parte do programa onde você pode acessar um determinado
# identificador. Existem dois escopos básicos de variáveis em Python:
# Variáveis globais
# Variáveis locais

###############################
# Variáveis globais vs. locais:
# As variáveis que são definidas dentro de um corpo de função têm um escopo local e
# aquelas definidas fora têm um escopo global.

# Isso significa que as variáveis locais podem ser acessadas apenas dentro da função em que são declaradas,
# enquanto as variáveis globais podem ser acessadas em todo o corpo do programa por todas as funções.
#  Quando você chama uma função, as variáveis declaradas dentro dela são trazidas para o escopo.

# exemplo:
total = 0 # variável global

def soma(x, y):  # função que soma dois números e armazena o resultado em uma variável local total
  total = x + y # variável local total que é acessada apenas dentro da função soma e não pode ser acessada fora
  return total # retorna o valor da variável local total para a função soma

# chamando a função soma
total = soma(10, 20) # chamando a função soma e armazenando o resultado em total (variável global)
print(total) # imprime o valor da variável global total
