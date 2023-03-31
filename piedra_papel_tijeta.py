user_option = input('piedar papele o tijera =>')
computer_option = 'tijera'

if user_option == computer_option:
  print('empate¡')
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('piedra gana a tijera')
    print('user gano¡')
  else:
    print('papel gano a piedra')
    print('computer gano')
  
elif user_option == 'papel':
  if computer_option == 'piedra':
    print('papel gana a tijera')
    print('user gano')

  else:
    print('tijera gana a papel')
    print('computer gano¡')

elif: user_option == 'tijera':
  if computer_option == 'papel':
    print('tijera gana a papel')
    print('user gano¡')
else:
  print('piedra gana a tijera')
  print('computer gano¡')
  