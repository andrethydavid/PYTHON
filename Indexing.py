# Indexing 
text = 'ella sabe python'
print(text[0])
print(text[1])
print(text[9])

#len es para medir palabras
size = len(text)
print('size =>',size)
print(text[size -1 ]) 
print(text[-1])


#slicing sacar partes del texto especificamente 

print(text[0:5])
print(text[10:16])
print(text[0:10])
print(text[5:-1])
print(text[5:])
print(text[:])
print(text[10:16:1]) #saltos de palabras
print(text[10:16:2]) #saltos de palabras 
print(text[::2]) 
