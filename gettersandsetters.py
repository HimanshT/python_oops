# Getters in Python are methods that are used to access the values of an object properties. Used to return the value of a specific property and typically
# defined by @property decorator.

# Getters cannot take any parameters and we cannot set the value through the getter method. Therefore,we use setters.


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


# Getter
# ukg = myclass(10)
# print(ukg.ten_value)

# setter
lkg = myclass(7)
lkg.ten_value = 89
print(lkg.ten_value)
lkg.show()

# you can use them for abstraction
# Getters are OOPs functions in python. Getters are functions used to retrieve the values of private attributes, while setters are functions used to modify or assign values to private attributes.
