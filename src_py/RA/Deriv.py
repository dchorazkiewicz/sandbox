import numpy as np

class Diff_fun(object):
    """Superclass of numerical derivatives"""
    def __init__(self, h=1.0E-5):
        self.h = h # spacing for numerical derivatives

    def __call__(self, x):
        raise NotImplementedErrors

    def df(self, x):
        """Return the 1st derivative of self.f."""
        # Compute first derivative by a finite difference
        h = self.h
        return (self(x+h) - self(x-h))/(2.0*h)

    def ddf(self, x):
        """Return the 2nd derivative of self.f."""
        # Compute second derivative by a finite difference:
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h))/(float(h)**2)


class My_lambda(Diff_fun):

    def __init__(self, f, h=1.0E-5):
        Diff_fun.__init__(self, h)
        self.f = f
    def __str__(self):
        return "This is custom lambda function."
    def __call__(self, x):
        return self.f(x)



if __name__ == "__main__":

    f=My_lambda(lambda x: x**3)
    print(type(f))
    print(f'Function value:%g' % f(1))
    print(f'Derivative value: %g' % f.df(1))
    print(f'Second derivative value: %g' % f.ddf(1))
    # stack operations
    ff = My_lambda(f)
    print(f'Function value:%g' % ff(1))
    print(f'Derivative value: %g' % ff.df(1))
    print(f'Second derivative value: %g' % ff.ddf(1))