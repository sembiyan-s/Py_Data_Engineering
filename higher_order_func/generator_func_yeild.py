# A generator function is a special type of a function that uses the yeild keyword,
# to return values onne by one ,instead of returning everything at once.

# if your memory is used your memory is efficient -- go for (Yeild)

# withoout using yeild
'''def get_numbers(n):
    return[i for i in range(n)]     # output  : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(get_numbers(10))'''

def get_number(n):
    for i in range(n):
        yield i             # store and iterate the value one by one , everything at once.

for gets in get_number(10):
    print(gets)