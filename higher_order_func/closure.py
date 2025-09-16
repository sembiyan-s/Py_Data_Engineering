# one inner func can refer outer func argument ------->  Closure

def outer(msg):
    def inner():
        return f'message is: {msg}' # ---------->  closure
    return inner

say_hi =outer("vanakkam da mapla !")
print(say_hi())