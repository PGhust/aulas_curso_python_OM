# Função Print -> Exibe coisas na tela

# A composição é print(ARGUMENTO)  -> é um argumento NÃO nomeado

print(123)

# Podemos utilizar mais de um argumento

print(123, 456)  
print(789, 101112)


# Posso utilizar um argumento nomeado, como um separador sep=

print(12, 34, sep='~')  
print(56, 78, sep='_')

# Muitas vezes não enxergamos os caracteres de espaçamento e de quebra de linha num código e etc. \r\n -> CRLF por exemplo no windows \r\n -> LF


print(12, 34, sep='~', end='##')  #end= evidencia a quebra de linha, no caso a #
print(56, 78, sep='_', end='#$#$#$\n')
print(77, 7, sep='_', end='\n')