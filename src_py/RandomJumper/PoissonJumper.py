import numpy as np
from scipy.integrate import quad
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

class PoissonJumper(object):
    def __init__(self, f_lambda, t, x):
        self.f_lambda = f_lambda
        self.position = np.array([[t,x]])
        
    def __call__(self,t,x):
        return self.f_lambda(t,x)
    
    def get_last_position(self):
        return self.position[-1]
        
    def get_homo_jump(self):
       return np.random.exponential(1)
   
    def get_integral(self, t, t0, x0):
        return quad(lambda z: self.f_lambda(z, x0), t0, t)[0]
    
    def get_inverse(self, val, tt0, xx0):
        return root_scalar(lambda z: self.get_integral(tt0+z,tt0,xx0)-val,
                           x0=0.9, fprime = lambda z: self.f_lambda(z,xx0),
                           bracket=[0,100], method='newton').root
    
    def jump(self):
        HJ = self.get_homo_jump()
        # print(f'Homo jump= {HJ}')
        # print(f'Position:{self.position[-1]}')
        tt=self.position[-1,0]
        xx=self.position[-1,1]
        NHJ = self.get_inverse(HJ, tt, xx)
        # print(f'Non-homo jump:{NHJ}\n----')
        self.position=np.vstack((self.position, np.array([tt+NHJ, xx])))
        return 0

        
if __name__ == "__main__":
    print("..:: Test PoissonJumper ::..")
    
    PJ = PoissonJumper(lambda t, x: np.exp(-t/1000)+.01, 0., 10.)
    print(PJ.position[-1])
    print(PJ(1,1))
    print(f'Homo jump: {PJ.get_homo_jump()}')
    print(f'Example integral: {PJ.get_integral(t=10,t0=2,x0=1)}')
    print(20*'~')
    print(PJ.get_inverse(8,0,0))
    for i in range(1000):
        PJ.jump()
    x=PJ.position[:,0]
    y=(x[1:]-x[:-1])
    plt.hist(y, bins=100)
    plt.show()
    
