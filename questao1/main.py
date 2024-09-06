def determinar_fase_da_vida(fase):

    if fase < 3:
        return 'Infancia'
    elif 3 <= fase <=12:
        return 'Pre-Adolescencia'
    elif 13  <= fase <= 19:
        return 'Adolescente'
    elif 20 <= fase <= 35:
        return 'Juventude'
    elif 36 <= fase <= 55:
        return 'Meia-Idade'
    elif fase >56:
        return 'Terceira-Idade'
    
fase = int(input('Coloque Sua Idade: '))
idade = determinar_fase_da_vida(fase)
print(f'Você está na sua fase da {idade}.')
