import numpy as np

class Diff(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

"""Classes of diff methods witthout explicit constructors"""
class Forward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h
    
class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h
    
class Central2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)
    
class Central4(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (4./3)*(f(x+h)- f(x-h)) /(2*h) - \
        (1./3)*(f(x+2*h) - f(x-2*h))/(4*h)
  
class Central6(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (3./2) *(f(x+h)- f(x-h)) /(2*h) - \
        (3./5) *(f(x+2*h) - f(x-2*h))/(4*h) + \
        (1./10)*(f(x+3*h) - f(x-3*h))/(6*h)

class Forward3(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (-(1./6)*f(x+2*h) + f(x+h) - 0.5*f(x) - \
        (1./3)*f(x-h))/h


class Diff2(Diff):
    def __init__(self, f, h=1E-5, dfdx_exact=None):
        Diff.__init__(self, f, h)
        self.exact = dfdx_exact
    def error(self, x):
        if self.exact is not None:
            df_numerical = self(x)
            df_exact = self.exact(x)
        return df_exact - df_numerical
class Forward1(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h
    
def _test_one_method(method):
    """Test method in string ‘method‘ on a linear function."""
    f = lambda x: a*x**2 + b
    df_exact = lambda x: 2*a*x
    a = 0.2; b = -4
    df = eval(method)(f, h=2E-5)
    x = 6.2
    print(f"method %s produce a difference %g" % \
         (method, df(x)-df_exact(x)))

if __name__ == "__main__":
    # we are able to nested calls
    mysin = Central2(Central2(np.sin))
    print(f'Nested call: %g' % (mysin(1)))
    # "unit test"
    _test_one_method('Forward1')
