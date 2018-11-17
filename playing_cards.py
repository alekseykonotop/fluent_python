# playing cards and collections module

import collections
from random import choice



Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # Метод не работает, надо понять как сделать так, что при выполнении print данные выводились в нужно формате
    # def __string__(self, position):
    #     return f'{self._cards[position].rank} {self._cards[position].suit}'


deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print('========')
print(choice(deck))
print(choice(deck))
print(choice(deck))
print('========')
print(deck[12::13])
print('========')
for i, card in enumerate(deck):
    print(f'num {i + 1} is: {card}')