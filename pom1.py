def f(x):
    return x*x-1

def ff(x,h=0.0001):
    return (f(x+h)-f(x))/h

if __name__=='__main__':
    print("funkcja:",f(10))
    print("pochodna:",ff(10))