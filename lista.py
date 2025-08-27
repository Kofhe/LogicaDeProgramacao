new_player = 'mateus'
players = ['ada', 'bob','chris','dan']
players.insert(3,'ana')
#print('lucas' in players) #conferir se existe lucas na lista
print(len(players)) #len(players) conta quantos nomes tem na lista

for player in players:
    print(player)

# ou

contador = 0
while contador < len(players):
    print(players[contador])
    contador += 1

