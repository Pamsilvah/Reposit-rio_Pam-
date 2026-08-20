def verificar_idade():
    idade = int(input('digite sua idade: '))
    if idade < 16:
        print('menor de 16 anos. Entrada proibida')
    else:
        print('Pode entrar na festa!!')
verificar_idade()