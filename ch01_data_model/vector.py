from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Boa pratica!
    # Implementa a representacao do objeto como string
    # Se nao for implementado exibe algo como <Vector object at 0x10e>
    # O Python chamara esse metodo como alternativa ao __str__, caso nao
    # esteja implementado
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # implementa operador +
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # Implementa operador *
    # Cria um novo objeto com o resultado (esperado dos operadores infixos)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
