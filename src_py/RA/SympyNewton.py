import sympy
import numpy as np
import matplotlib.pyplot as plt


tol = 0.01
xk = 2

s_x = sympy.symbols("x")
s_f = sympy.exp(s_x)-np.exp(1)

f  = lambda x: sympy.lambdify(s_x,s_f,'numpy')(x)
fp = lambda x: sympy.lambdify(s_x,sympy.diff(s_f,s_x),'numpy')(x)

x = np.linspace(-1,2,1000)

fig, ax = plt.subplots(1, 1, figsize=(12, 4))
ax.plot(x, f(x))
ax.axhline(0, ls=':', color='k')
# plt.show()

n = 0
while f(xk) > tol:
    xk_new = xk - f(xk) / fp(xk)
    print("New x:", xk_new)
    ax.plot([xk, xk], [0, f(xk)], color='k', ls=':')
    ax.plot(xk, f(xk), 'ko')
    ax.text(xk, -.5, r'$x_%d$' % n, ha='center')
    ax.plot([xk, xk_new], [f(xk), 0], 'k-')

    xk = xk_new
    n += 1

    ax.plot(xk, f(xk), 'r*', markersize=15)


    ax.set_title("Newtown's method")
    ax.set_xticks([-1, 0, 1, 2])

ax.annotate("Root approximately at %.3f" % xk,
    fontsize=14, family="serif",
    xy=(xk, f(xk)), xycoords='data',
    xytext=(-150, +50), textcoords='offset points',
    arrowprops=dict(arrowstyle="->",\
    connectionstyle="arc3, rad=-.5"))
plt.show()