from pom1 import *

def newton(x0=5,epsilon=0.0001):
    epsilon=abs(epsilon)
    z1=x0-1
    f0=f(x0)
    while(abs(x1-x0)>epsilon and (abs(f0)>epsilon)):
        x1=x0
        x0=


