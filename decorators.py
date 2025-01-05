# python decorators take another fn as argument and return a new function . the new function is called "decorated" fn


def greet(fx):
    def dec():
        print("good morning")
        fx()
        print("good night")

    return dec


@greet
def hello():
    print("Hello")


def greetAdd(fn):
    def decfn(*args, **kwargs):
        fn(*args, **kwargs)
        print("we are printing something")

    return decfn


# when there are arguments
@greetAdd
def add(a, b):
    print(a + b)


hello()
add(3, 5)

# mostly used for logging something
