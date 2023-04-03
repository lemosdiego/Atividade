T1 = int(0)
T2 = int(1)
T3 = int(0)
print ('-' *30)
print (' ' *3, 'Consulta da Sequência de Fibonacci')
print ('-' *30)
Valor = int(input('Digite um número: '))
while Valor > T3:
    T3 = T1 + T2
T1 = T2
T2 = T3
if Valor == 0 or Valor == 1:
    print ('O número faz parte da sequência de Fibonacci.')
elif Valor == T3:
    print ('O número faz parte da sequência de Fibonacci.')
else:
    print ('O número digitado não faz parte da sequência de Fibonacci.')
