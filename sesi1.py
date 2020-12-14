# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:56:46 2020

@author: user
"""

##Training Python

Text = "Kelas Python"
print(Text)

Text2 = "BMKG"
print(Text +  Text2)


###LIST
kardus = ['aqua', 'cocacola', 'sprite', 'fanta']
print(kardus)
botol = 'sprite'
print(botol)
print(kardus[-4])
kardus[0] = 'cleo'
print(kardus)
kardus[-1] = 80
print(kardus)

###TUPLES
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge') ##Tuple
te = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge'] ##List
print(t)
print(te)
print(type(t))
print(type(te))

###DICTIONARY
MLB_team = {
        'Colorado' : 'Rockies',
        'Boston' : 'Red Sox',
        'Minnesota' : 'Twins',
        'Milwaukee' : 'Brewers',
        'Seattle' : 'Mariners'
        }
print(MLB_team['Minnesota'])
print(MLB_team['Colorado'])
MLB_team['Kansas City'] = 'Royals'
MLB_team
print(MLB_team)
MLB_team['Seattle'] = 'Seahawks'
MLB_team
del MLB_team['Seattle']


person = {}
type(person)
person['fname'] = 'Hack'
person['lname'] = 'PTP'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Jose']
person['pets'] = {'dog' : 'Fido' , 'cat' : 'Sox'}
print(person['fname'])
print(person['lname'])
print(person['children'])
print(person['children'][1])
print(person['pets'])

##Built-in Methods
d = {'a' : 10, 'b' : 20, 'c' : 30}
print(d.items())
print(type(d))
print(d.keys())


##LINE CONTINUATION
person1_age = 42
person2_age = 16
person3_age = 71
someone_is_of_working_age = (
        (person1_age >= 18 and person1_age <= 65) 
        or (person2_age >= 18 and person2_age <= 65) 
        or (person3_age >= 18 and person3_age <= 65)
        )
someone_is_of_working_age







