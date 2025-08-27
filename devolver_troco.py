notas_e_moedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

#valor a receber: 1700 reais

#valor recebido:2000 reais


valor_receber = float(input ('Qual o valor a receber?'))
#1700

valor_recebido = float(input ('Qual o valor recebido?'))
#2000

diferenca = valor_receber - valor_recebido
#300

for valor in notas_e_moedas: #repetição irá conferir os valores e valor é o nome que eu dei
    quantidade_de_itens = 0 
    while valor <= diferenca:
        quantidade_de_itens +=1
        diferenca -= valor
        if quantidade_de_itens > 0:
            print (quantidade_de_itens, 'itens de', valor)

# print('o valor é', total)

