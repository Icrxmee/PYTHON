dias = float ( input('Quantos dias alugados:'))
km = float ( input( 'Quantos km eu rodei? :'))

buydia = dias  *  60.00
buykm  = km * 0.15
total = buydia + buykm

print ('O total a pagar é de R${:.2f}' .format(total))


