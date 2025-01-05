# x = [1, 2, 3]
# print(dir(x))

# dir returns a list of all the attributes and methods
# for an object.

# d __dict__ return a dictionary of an object attributes


class myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"we are printing {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


x = myclass(10)
print(x.__dict__)


# help function is used to get help docs or an object
print(help(x))
