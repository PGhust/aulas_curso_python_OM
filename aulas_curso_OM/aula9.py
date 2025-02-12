#Operadores aritméticos 

adicao = 10 + 10
print('adição:',adicao)

subtracao = 10 - 10
print('subtração',subtracao)

# Quando operar um valor normal com um de ponto flutuante o resultado sempre é em ponto flutuante 

multiplicacao = 10 * 10
print('multiplicação', multiplicacao)

multfloat = 10 * 2.4
print(multfloat)



divisao = 10 / 2.4 # Retorna pto flutuante indepentende se é tudo int ou float 
print('divisão', divisao)

divisao_inteira = 10 // 2 # Nem sempre retorna inteiro, mas trunca a divisão quando ocorre um float cortando as casas decimais mas retornando um pto flutuante ex do 10//3 e 10/3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('exponenciacao', exponenciacao)

modulo = 55 % 2 # Resto da divisão -> Saber se o numero x é divisível por y se for retorna 0 
print('módulo', modulo)
print(10 % 8 == 0)
print(16 % 8 == 0)

# Dá para verificar paridade também 

print(10 % 2 == 0)
print(15 % 2 == 0)
