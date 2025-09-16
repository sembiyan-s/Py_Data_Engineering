#  A composed Function is when the output of one function becomes the input of another --> like f(g(x))

def add(x):
    return x + 2

def multi (x):
    return x * 2

def composed(x):
    return add(multi(x))    # ------->  f(g(x))


print(composed(4))


    