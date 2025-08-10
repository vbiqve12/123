#name greet app - basic
def greet(name):
    return "Hello, " + name + "! you're a badass and i love you :)"
user_name = input("Enter your name: ")
message = greet(user_name)
print(message)