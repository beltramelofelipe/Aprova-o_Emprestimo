valor_casa = float(input('Qual valor da casa? '))
salario = float(input('Qual o seu salario? '))
par_pag = int(input('Em quantos anos vocÊ pretende pagar? '))

meses = (par_pag * 12)
valor_parcela = (valor_casa / meses)
percent_salario = (valor_parcela / salario)

if percent_salario > 0.3:
   print('O seu emprestimo foi negada :(')

else:
   print('PARABÉNSS SEU EMPRESTIMO FOI APROVADO')
   print('------------------------------')
   print('valor do emprestimo {: .1f}'.format(valor_casa))
   print('Quantidade de parcelas {}'.format(meses))
   print('Valor da parcela {}'.format(valor_parcela))
   print('------------------------------')
