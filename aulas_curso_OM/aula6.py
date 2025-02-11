# Conversão de tipos, coerção é um ato de converter um tipo em outro, podendo ser utilizado type convertion, typecasting, coercion. Temos tipos IMUTÁVEIS, sendo eles: str, int, float, bool. 

print(1 + 1)
print('a' + 'b') # Concatena str -> polimorfismo (usa mesmo op, para múltiplas ações)

#print('1' + 1)
# Não dá para concatenar uma str om inteiro 
print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1') + 1)
 
# Funciona para valores booleanos também 
print(bool('')) #Nenhum valor -> False 
print(bool(' ')) #Algum valor -> True

# Posso concatenar coisas também 

print(str(11) + 'b')