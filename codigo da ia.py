def calculadora_da_ia():
  try:
    #entrada da operação
    operção = input('escolha a operação (+ , - , * , /): ')
    #vefifica se a operação é valida
    if operação not in ['+' ,'-', '*', '/']:
        print('operação invalida!')
        return
        
        # entrada dos numeros
        
        num1 = float(input('digite o primeiro número:')
        num2 = float(input('digite o segundo número: ')
        num3 = float(input('digite o terceiro número: ')
        num4 = float(input('digite o quarto número: ')
                     
                     if operação == '+':
                     resultado = num1 + num2 + num3 + num4
                     elif operação == '-':
                     resultado = num1 - num2 - num3 - num4
                     elif operação == '*':
                     resultado = num1 * num2 * num3 * num4
                     #divisão safada
                     elif operação == '/':
                     if 0 in [num1 , num2 , num3 , num4]:
                     print(f'resultado: {resultado}')

             except ValueError:
                     print('por favor, insira apenas números validos.')
                     
                     #executar a calculadora hehe
                     calculadora_da_ia()