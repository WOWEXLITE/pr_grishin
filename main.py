
from random import choices

symbols = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'

chars = ''

pwd_length = int(input('Введите длинну пароля: '))
pwd_auto = (input('Сгенерировать пароль автоматически? (y,n): ') == 'y')

for text, seq in(
                 ('Включить верхний регистор',  symbols  ),
    if pwd_auto or(input(text + ' (y,n): ') == 'y'):
       chars += seq

password = ''.join(choices(chars, k=pwd_length))

print ('\n', password '\n', sep='')
