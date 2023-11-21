from Models.Line import Line


class Rectangle:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def get_d(self):
        return self.d

    def get_ab(self):
        return Line(self.a, self.b)

    def get_bc(self):
        return Line(self.b, self.c)

    def get_cd(self):
        return Line(self.c, self.d)

    def get_da(self):
        return Line(self.d, self.a)

    def __str__(self):
        return f"Rectangle({self.a}, {self.b}, {self.c}, {self.d})"
