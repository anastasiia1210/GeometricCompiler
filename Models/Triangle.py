from Models.Line import Line


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def get_ab(self):
        return Line(self.a, self.b)

    def get_bc(self):
        return Line(self.b, self.c)

    def get_ca(self):
        return Line(self.c, self.a)

    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"
