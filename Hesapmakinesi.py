# Hesap Makinesi

print ('|Merhaba Hesap makinesine hoşgeldin...')


num1 = int (input ('|1. sayıyı yazarmısın : '))
num2 = int (input ('|2. sayıyı yazarmısın : '))
op = input ('|Birşey Seç (+, -, x, /)')
print ('|-----------------------------------------------------------------|')


if op =='+' :
    print (num1, '+', num2, '=', num1 + num2)

if op == '-' :
    print (num1, '-', num2, '=', num1 - num2)

if op == 'x' :
    print (num1, 'x', num2, '=', num1 * num2)
    
if op == '/' :
    print (num1, '/', num2, '=', num1 / num2)


print('Görüşürüz!')