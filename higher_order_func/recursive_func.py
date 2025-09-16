# A recrsive function is a function thats calls itself ,
# in order to solve a smaller version of the same problem

# it implements tree , algorithms , binary search , divide and concare

def factorial(n):
    if n==1:
        return 1
    return n * factorial( n - 1) # ---------> one function call in the same function ( recursive )

print(factorial(5))


# Eg 2
def countdown(n):
    if n == 0:
        print("........BoooooooooM.......... !")
        return 
    print(n)
    countdown (n-1)

print(countdown(5))