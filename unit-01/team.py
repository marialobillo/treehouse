players = []

add_players_answer = input('Do you want to add players? (yes/no)')
if add_players_answer.lower() == 'yes':
    player_name = input('Write the player name:')
    players.append(player_name)
elif add_players_answer.lower() == 'no':
    print(players)

print('There are {} players on the team'.format(len(players)))

number = 1
for player in players:
    print('nº {} => {}'.format(number, player))
    number += 1

print('The goalkeeper is {}'.format(players[0]))
