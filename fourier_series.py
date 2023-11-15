# Import sympy library
import sympy as sp
x = sp.Symbol('x')

# Main function
f = x **2

# iteration of fourier series
period = 10

#find the coefficient A
def calculateAk(k):
    fAk = f * sp.cos(k*x)
    #integrate between -pi and pi
    return sp.integrate(fAk, (x, -sp.pi, sp.pi))/sp.pi


#find the coefficient B
def calculateBk(k):
    fBk = f * sp.sin(k*x)
    #integrate between -pi and pi
    return sp.integrate(fBk, (x, -sp.pi, sp.pi))/sp.pi

# add A0/2 to final series
fourier_series = calculateAk(0)/2
# sum of the functions (using cos and sin)
for k in range(period+1):
    fourier_series += calculateAk(k+1)*sp.cos((k+1)*x)
    fourier_series += calculateBk(k+1)*sp.sin((k+1)*x)

# Plot the graph of f(x)
sp.plot(fourier_series, (x, -sp.pi, sp.pi), title='Fourier Series of f(x)', xlabel='x', ylabel='f(x)')
sp.plot(f, (x, -sp.pi, sp.pi), title='Real f(x)', xlabel='x', ylabel='f(x)')
