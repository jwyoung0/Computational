#derivative formula with class

class Derivative:
    def __init__(self, f, h = 1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h #make short forms
        return (f(x+h) - f(x))/h


from math import sin, cos, pi
df = Derivative(sin)
x = pi
print(df(x))
print(cos(x))
    

print(df(0.5))
print(cos(0.5))
