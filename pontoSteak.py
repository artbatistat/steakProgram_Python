'''
Criar um programa que dependendo da temperatura (em celsius) do steak da carne, ele retorna o ponto de cozimento.
O usuário deverá fornecer a temperatura.
'''

temperatura = int(input('Digite a temperatura da carne:'))

if(temperatura < 48):
    print(f'A carne ainda não está em nenhum ponto, por gentileza deixe mais alguns minutos')
elif(temperatura >= 48 and temperatura < 54):
    print(f'A carne está somente selada')
elif(temperatura >= 54 and temperatura < 60):
    print(f'Carne ao ponto para mal passada')
elif(temperatura >= 60 and temperatura < 65):
    print(f'Carne ao ponto')
elif(temperatura >= 65 and temperatura < 71):
    print(f'Carne ao ponto para bem passada')
else:
    print(f'Carne bem passada')