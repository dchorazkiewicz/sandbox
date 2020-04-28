import numpy as np
from scipy import optimize
from scipy import integrate

class InverseFunction(object):
    def __init__(self,f):
        self.f = f

    def __call__(self, y):
        sol = optimize.root_scalar(lambda x: self.f(x)-y, bracket=[1, 1E5], method='brentq')
        print(sol)
        return sol.root

if __name__ == "__main__":
    
    invf = InverseFunction(lambda x: np.sqrt(x))
    
    print(invf(3))