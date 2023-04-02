# CRUD create, Read, Update & delete

numbers = [1,2,3,4,5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700) # agregar nuevo elemento
print(numbers)

numbers.insert(0,'hola') # agrega un item y indice 
print(numbers)

numbers.insert(3,'change') # crea otro dato 
print(numbers)

tasks = ['todo 1','todo 2','todo 3']
new_list = numbers + tasks
print(new_list)

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)


strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

