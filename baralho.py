import collections

# namedtuple cria classe apenas com grupo de atributos, sem metodos
Card = collections.namedtuple('Card', ['rank', 'suit'])

# Classe que cria todas as cartas do baralho
# Por conta do metodo especial __len__, podemos usar len(deck) para 
# pegar a qtdade de cartas
# Por conta do metodo especial __getitem__, podemos pegar carta de qualquer
# posicao com deck[0]
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits \
                for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# Exemplos de uso:
# deck = FrenchDeck()
# len(deck)
# deck[-1]
# choice[deck]
