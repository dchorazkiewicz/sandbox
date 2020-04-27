import numpy as np

class Integrator(object):
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()
        
    def construct_method(self):
        raise NotImplementedError

    def integrate(self, f):
        return np.dot(self.weights, f(self.points))

class Midpoint(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n # quick forms
        h = (b-a)/float(n)
        x = np.linspace(a + 0.5*h, b - 0.5*h, n)
        w = np.zeros(len(x)) + h
        return x, w

class Trapezoidal(Integrator):
    def construct_method(self):
        x = np.linspace(self.a, self.b, self.n)
        h = (self.b - self.a)/float(self.n - 1)
        w = np.zeros(len(x)) + h
        w[0] /= 2
        w[-1] /= 2
        return x, w

class Simpson(Integrator):
    def construct_method(self):
        if self.n % 2 != 1:
            print("n must be odd, 1 is added")
            self.n += 1
        x = np.linspace(self.a, self.b, self.n)
        h = (self.b - self.a)/float(self.n - 1)*2
        w = np.zeros(len(x))
        w[0:self.n:2] = h*1.0/3
        w[1:self.n-1:2] = h*2.0/3
        w[0] /= 2
        w[-1] /= 2
        return x, w

class GaussLegendre2(Integrator):
    def construct_method(self):
        if self.n % 2 != 0:
            print("n must be odd, 1 is added") 
            self.n -= 1
        nintervals = int(self.n/2.0)
        h = (self.b - self.a)/float(nintervals)
        x = np.zeros(self.n)
        sqrt3 = 1.0/np.sqrt(3)
        for i in range(nintervals):
            x[2*i]= self.a + (i+0.5)*h - 0.5*sqrt3*h
            x[2*i+1] = self.a + (i+0.5)*h + 0.5*sqrt3*h
        w = np.zeros(len(x)) + h/2.0
        return x, w

class F(object):
    def __init__(self, m):
        self.m = float(m)
    def __call__(self, t):
        m = self.m
        return (1 + 1/m)*t**(1/m)

if __name__ == "__main__":
    def f(x): 
        return np.sin(x**2 + 2)
    a = 2; b = 3; n = 4
    for Method in Midpoint, Trapezoidal, Simpson, GaussLegendre2:
        m = Method(a, b, n)
        print(m.__class__.__name__, m.integrate(f))

    print("Parametric integral")
    for m in [1/2,1/6,1/102]:
        f=F(m)
        m=Trapezoidal(1,5,101)
        print(m.__class__.__name__, m.integrate(f))