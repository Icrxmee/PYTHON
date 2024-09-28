
frase = 'Curso em Video Python'

print ('--' * 15)

# FATIAMENTO

print (frase[9])

print (frase[9:13])

print (frase[9:21])

print (frase[9:21:2])

print (frase[:5])

print (frase[15:])

print (frase[9::3])

print ('--' * 15)

# ANÁLISE

print (len(frase))

print (frase.count('o'))

print (frase.count('o',0,13))

print (frase.find('deo'))

print (frase.find('Android'))

print ('Curso' in frase)

print ('--' * 15)

# TRANSFORMAÇÃO

print (frase.replace('Python','Android'))

print (frase.upper())

print (frase.lower())

print (frase.capitalize())

print (frase.title())

print (frase.strip())

print ( '--' * 15)

# DIVISÃO

print (frase.split())

# JUNÇÃO

print('-'.join(frase))