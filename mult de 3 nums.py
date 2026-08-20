#calculadora

#operações básica:
    #somar (+)
    #subtrair (-)
    #multiplicar (*)
    #dividr (/)

def calculadora_da_pam():
    
    print('sejam bem-vindos a calculadora simples e funcional!')
    print('operações disponiveis:')
    print('1 adição (+)')
    print('2 subtração (-)')
    print('3 multiplicação(*)')
    print('4 divisão(/)')
    
    operação = input('escolha a operação(+,-,*,/):')
    
    if operação in ['+','-','*','/']:
        try:
            num1 = float(input('digite o primeiro número: '))
            num2 = float(input('digite o segundo número: '))
            num3 = float(input('digite o terceiro número: '))
            num4 = float(input('digite o quarto número: '))
            num5 = float(input('digite o quinto número: '))
            
            if operação == '+':
                resultado = num1 + num2 + num3 + num4 + num5
            elif operação == '-':
                resultado = num1 - num2 - num3 - num4 - num5
            elif operação =='*':
                resultado = num1 * num2 * num3 * num4 * num5
            elif operação == '/':
                    if 0 in [num2 / num3 / num4 / num5]:
                        print('Erro: divisão por zero!')
                    else:
                            return
                    resultado = num1/ num2/ num3/ num4/ num5
                    print(f'resultado: {resultado}')
            
                 except ValueError:
                    print('por favor, insira apenas números validos')
                    else:
                        print('operação invalida')
                
    #execultar calculadora
                    calculadora_da_pam()