from random import randint

coin = {0 : 'Heads',
        1 : 'Tails'}

flip = randint(0,1)

print(coin[flip])