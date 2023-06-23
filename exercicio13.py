numero1 = 8
numero2 = 88
resposta = numero2/numero1
numeros= []
print(resposta)

if resposta < 10:
    print ('numero baixo')
else:
    print('numero alto')

while True:
    nota = float(input('Digite uma nota entre 0 e 10:'))
    if nota >= 0 and nota <= 10:
        print('nota está valida obrigada(o), nota inserida:', nota)
        break
    else:
        print('Nota invalida, insira uma nota entre 0 ou 10')