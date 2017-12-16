motions = {
    1: {
        'U': None,
        'R': None,
        'D': 3,
        'L': None
    },
    2: {
        'U': None,
        'R': 3,
        'D': 6,
        'L': None
    },
    3: {
        'U': 1,
        'R': 4,
        'D': 7,
        'L': 2
    },
    4: {
        'U': None,
        'R': None,
        'D': 8,
        'L': 3
    },
    5: {
        'U': None,
        'R': 6,
        'D': None,
        'L': None
    },
    6: {
        'U': 2,
        'R': 7,
        'D': 'A',
        'L': 5
    },
    7: {
        'U': 3,
        'R': 8,
        'D': 'B',
        'L': 6
    },
    8: {
        'U': 4,
        'R': 9,
        'D': 'C',
        'L': 7
    },
    9: {
        'U': None,
        'R': None,
        'D': None,
        'L': 8
    },
    'A': {
        'U': 6,
        'R': 'B',
        'D': None,
        'L': None
    },
    'B': {
        'U': 7,
        'R': 'C',
        'D': 'D',
        'L': 'A'
    },
    'C': {
        'U': 8,
        'R': None,
        'D': None,
        'L': 'B'
    },
    'D': {
        'U': 'B',
        'R': None,
        'D': None,
        'L': None
    },

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

