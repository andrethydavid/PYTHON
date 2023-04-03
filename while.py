# mientras son siclos para donde y cuadno tyerminan las funciones 
'''''
while True:
  print('se ejecuto')
'''''


counter = 0

while counter < 10:
  counter += 1 
  print(counter)



counter = 0

while counter < 20:
  counter += 1
  if counter == 15:
    break # se rompe con una condicion deseada 
  print(counter)
  
  

counter = 0
# solo imprime los numeros del 15  en adelante 
while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter)
  