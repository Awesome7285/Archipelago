with open('external/games.txt') as f:
    data = f.read().split('\n')

with open('external/out.txt', 'w') as f:
    for game in data:
        print(game)
        if '(' not in game:
            f.write(game + '\t\n')
        else:
            platform = game[game.find('(')+1:-1]
            game = game[:game.find('(')-1]
            f.write(game + '\t' + platform + '\n')