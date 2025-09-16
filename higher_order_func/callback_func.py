# A callback function is a function that you pass as an argument to another function,
# so that it can be called (exacution) later ,usually after some action is completed.

def button_clicked(callback):   # show_message
    print(" button is Clicked !")  # once its print got executed
    callback()

def show_message():
    print("hii sembiyan ,welcome !")

button_clicked(show_message)
