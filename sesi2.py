# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:53:18 2020

@author: user
"""

##Training Python Sesi 2
##IF
x = 0
y = 5

if x < y:
    print('yes')
if y < x:
    print('yes')
if x:
    print('yes')
if y:
    print('yes')
if 'aul' in 'grault':
    print('yes')
if 'quux' in ['foo', 'bar', 'baz']:
    print('yes')

##WHILE
n = 5
while n > 0 :
    n -= 1
    print(n)

##BREAK
while True:
    msg = input('Ketikan karakter: ').lower()
    print(msg)
    if msg == 'stop':
        break

##contoh 
temp = input('Ketikan temperatur yang ingin dikonversi, eg. 45F, 120C: ')
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == 'C':
    result = int(round((9 * degree) / 5 + 32))
elif i_convertion =='F':
    result = int(round((degree - 32) * 5 /9))
else:
    print('Masukan input yang benar')
print('Temperaturnya adalah', result, 'derajat')