class RaizCuadrada:
    def __init__(self, a):
        self.a = a
        self.x = 1.0

    def calcular_raiz(self, iteraciones=10):
        for k in range(1, iteraciones + 1):
            self.x = (self.x + self.a / self.x) / 2
            print(f"La raíz en {k} iteraciones es: {self.x}")

a = float(input("Dame el valor de a: \n"))

raiz = RaizCuadrada(a)

raiz.calcular_raiz()

