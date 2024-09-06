def conversor_temperatura(temperatura, unidade):
    if unidade == "CTOF":
        return (temperatura * 9/5) + 32
    elif unidade == "FTOC":
        return (temperatura - 32) * 5/9
    elif unidade == "CTOK":
        return temperatura + 273.15
    elif unidade == "KTOC":
        return temperatura - 273.15
    elif unidade == "FTOk":
        return (temperatura - 32) * 5/9 + 273.15
    elif unidade == "KTOF":
        return (temperatura - 273.15) * 9/5 + 32
    else:
        return "Unidade inválida."

temperaturas_convertidas = []

while True:
    sair = input("Digite 's' para sair ou Enter para continuar: ").strip().upper()
    if sair == 'S':
        break
    
    temperatura = float(input("Digite a temperatura: "))
    unidade = input("Digite a unidade de conversão (CtoF, FtoC, CtoK, KtoC, FtoK, KtoF): ").strip().upper()
    
    resultado = conversor_temperatura(temperatura, unidade)
    
    if resultado == "UNIDADE INVÁLIDA.":
        print(resultado)
    else:
        print(f"A temperatura convertida é: {resultado}")
        temperaturas_convertidas.append(resultado)

if temperaturas_convertidas:
    maior = max(temperaturas_convertidas)
    menor = min(temperaturas_convertidas)
    media = sum(temperaturas_convertidas) / len(temperaturas_convertidas)
    
    print("\nTemperaturas convertidas:", temperaturas_convertidas)
    print(f"Maior temperatura: {maior}")
    print(f"Menor temperatura: {menor}")
    print(f"Média das temperaturas: {media}")
else:
    print("Nenhuma temperatura foi convertida.")
