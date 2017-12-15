instructions = [
    d.strip()
    for d in open('input.txt').read().split(',')
]

def up(x, y):
    return x, y+1

def down(x, y):
    return x, y-1

def left(x, y):
    return x-1, y

def right(x, y):
    return x+1, y

rightwards = {
    'up': 'right',
    'right': 'down',
    'down': 'left',
    'left': 'up'
}

leftwards = {
    'up': 'left',
    'left': 'down',
    'down': 'right',
    'right': 'up'
}

motions = {
    'up': up,
    'right': right,
    'down': down,
    'left': left
}

x = 0
y = 0
direction = 'up'
for instruction in instructions:
    turn = instruction[0]
    if turn == 'R':
        direction = rightwards[direction]
    else:
        direction = leftwards[direction]
    move = motions[direction]
    steps = int(instruction[1:])
    for _ in range(steps):
        x, y = move(x, y)

print abs(x) + abs(y)