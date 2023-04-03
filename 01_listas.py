my_dict = {}
print(type (my_dict))


my_dict = {
  'avion ': 'bla bla bla',
  'name' : 'nicolas',
  'las_name' : 'molina monroy',
  'age' : 97
}
      
print(my_dict)
print(len(my_dict))

print(my_dict)
print(my_dict['age'])
print(my_dict['las_name'])
print(my_dict.get('age')) #get para indetificar una llave 

print('avion' in my_dict) # para realizar un buliano 
print('otroqueno' in my_dict)
