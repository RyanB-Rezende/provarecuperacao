'''
Questão 3: Implementar um Conversor de Temperaturas com Loop
Escreva uma função chamada conversor_temperatura que recebe dois argumentos: um número (temperatura) e uma string representando a unidade de conversão (unidade). 
A função deve retornar o resultado da conversão da temperatura para a unidade especificada. As unidades suportadas são:

    "CtoF" para converter de Celsius para Fahrenheit
    "FtoC" para converter de Fahrenheit para Celsius
    "CtoK" para converter de Celsius para Kelvin
    "KtoC" para converter de Kelvin para Celsius
    "FtoK" para converter de Fahrenheit para Kelvin
    "KtoF" para converter de Kelvin para Fahrenheit

A função deve lidar com entradas inválidas e retornar uma mensagem apropriada nesses casos.

Segue um trecho mostrando como deve ser implementada a função:
    def conversor_temperatura(temperatura, unidade):
        if unidade == "CtoF":
            return (temperatura * 9/5) + 32


Na entrada dos números deve ser feito o tratamento de exceções, para que seja tratado os casos que não sejam digitados números.

O programa deve ficar em loop, solicitando ao usuário os valores e a unidade de conversão até que o usuário digite s para sair.

As temperaturas convertidas devem ser armazenadas em uma lista e depois de encerrar, mostrar a lista, a maior temperatura, a menor temperatura e a média das temperaturas convertidas.

# Exemplo de uso:
# Input: 100 "CtoF"
# Output: 212.0

# Input: 32 "FtoC"
# Output: 0.0

# Teste a função
print(conversor_temperatura(100, "CtoF"))   # Saída esperada: 212.0
print(conversor_temperatura(32, "FtoC"))    # Saída esperada: 0.0
print(conversor_temperatura(0, "CtoK"))     # Saída esperada: 273.15
print(conversor_temperatura(273.15, "KtoC"))# Saída esperada: 0.0
print(conversor_temperatura(32, "FtoK"))    # Saída esperada: 273.15
print(conversor_temperatura(273.15, "KtoF"))# Saída esperada: 32.0

'''