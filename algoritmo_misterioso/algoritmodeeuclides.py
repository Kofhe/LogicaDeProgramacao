primeiro_numero = input ("Digite um número inteiro: ")
primeiro_numero = int (primeiro_numero)

segundo_numero = int(input("Digite um número inteiro: "))

if primeiro_numero > segundo_numero:
    primeiro_numero = primeiro_numero - segundo_numero

elif segundo_numero > primeiro_numero:
    segundo_numero = segundo_numero - primeiro_numero

else:
    print ( "números são iguais")
