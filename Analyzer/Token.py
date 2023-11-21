class Token:
    def __init__(self, type, value):
        self._type = type
        self._value = value

    def get_type(self):
        return self._type

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def __str__(self):
        return f"[{self._type}, {self._value}]"
