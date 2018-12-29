from random import randint

NUM_TRIALS = 1000

def d6():
    return randint(1, 6)

def game_one():
    prev, curr = None, None
    cost = 0
    while prev != 5 or curr != 6:
        prev = curr
        curr = d6()
        cost += 1
    return cost

def ev_game_one():
    games = []
    for i in range(NUM_TRIALS):
        games.append(game_one())
    return sum(games) / len(games)

def game_two():
    prev, curr = None, None
    cost = 0
    while prev != 5 or curr != 5:
        prev = curr
        curr = d6()
        cost += 1
    return cost

def ev_game_two():
    games = []
    for i in range(NUM_TRIALS):
        games.append(game_two())

    return sum(games) / len(games)

print(ev_game_one())
print(ev_game_two())