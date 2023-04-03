''''
for element in range(1,21):
  print(element)
'''
# for list
my_List =[23,45,67,89,43]
for element in my_List:
  print(element)

 #for tupla

my_tuple = ('nico', 'juli','santi')
for element in my_tuple:
  print(element)

product = {
  'name' : 'camisa',
  'price': 100,
  'stock' : 89
}

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'Nico',
    'age': 35
  },
  {
    'name': 'zule',
    'age' : 45
  },
  {
    'name': 'santiago'
    'age':    8
    
  }
]

for person in people:
  print('name =>', person['name'])
