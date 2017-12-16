motions = {
    1: {
        'U': None,
        'R': 2,
        'D': 4,
        'L': None
    },
    2: {
        'U': None,
        'R': 3,
        'D': 5,
        'L': 1
    },
    3: {
        'U': None,
        'R': None,
        'D': 6,
        'L': 2
    },
    4: {
        'U': 1,
        'R': 5,
        'D': 8,
        'L': None
    },
    5: {
        'U': 2,
        'R': 6,
        'D': 8,
        'L': 4
    },
    6: {
        'U': 3,
        'R': None,
        'D': 9,
        'L': 5
    },
    7: {
        'U': 4,
        'R': 8,
        'D': None,
        'L': None
    },
    8: {
        'U': 5,
        'R': 9,
        'D': None,
        'L': 7
    },
    9: {
        'U': 6,
        'R': None,
        'D': None,
        'L': 8
    }
}

position = 5
code = ''
for line in open('input.txt'):
    for instruction in line.strip():
        next_position = motions[position][instruction]
        if next_position:
            position = next_position
    code += str(position)

print code

