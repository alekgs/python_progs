from itertools import product

ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз')
suits = ('треф', 'бубен', 'червей', 'пики')

cards = list(product(ranks, suits))

print(cards)

