class Calculadora:
    def __init__(self):
        self.value = 0

    def add(self, n1, n2):
        self.value = n1 + n2
        return self.value