users = {
    'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
    'address': {
        'street': 'Kulas Light',
        'suite': 'Apt. 556',
        'city': 'Gwenborough',
        'zipcode': '92998-3874',
        'geo': {
            'lat': '-37.3159',
            'lng': '81.1496'
        }
    }
}

print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users['email'])
print(users['address']['city'])
print(users['address']['geo']['lat'])

print(users)
print(type(users))
print('\nUbah Dict ke Json')

import json

hasil = json.dumps(users)
print(type(hasil))
print(hasil)

with open('hasil json', 'w') as file:
    json.dump(users, file)
