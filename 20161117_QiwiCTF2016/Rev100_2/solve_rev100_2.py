tmp = [
    '^',
    '4',
    'K',
    'i',
    '.',
    '/',
    'N',
    'j',
    'P',
    'o',
    '?',
    'l',
    '2',
    'T',
    '?']

for e in tmp:
    print chr(ord(e) + 3)


list = [
    's',
    'y',
    'n',
    't',
    ':',
    '{',
    'w',
    'q',
    'E',
    '6',
    'f',
    'X',
    'u',
    'o',
    'f',
    'a',
    '4',
    'X',
    'N',
    'u',
    '1',
    '}']

for e in list:
    print e.decode('ROT13')
