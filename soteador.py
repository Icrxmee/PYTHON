import random
nome1 = str ( input ('Digite o aluno 1:'))
nome2 = str ( input ('Digete o aluno:2:'))
nome3 = str ( input ('Digite o aluno 3:'))
nome4 = str ( input ('Digite o aluno 4:'))
nome5 = str ( input ('Digite o aluno 5:'))


nomes1 = [nome1, nome2, nome3, nome4, nome5]
sortear1  = random.choice(nomes1)

print ('O sorteador foi {}' .format(sortear1))

# Ou pode ser feito de outra forma...

nomes2 = ['Pedros','Icaro','Jose','Saulo','Julia']
sortear2 = random.choice(nomes2)

print('O nome sorteador foi  {}' .format(sortear2))