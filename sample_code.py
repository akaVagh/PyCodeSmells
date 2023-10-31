class SampleClass:
    class_field_1 = "field"
    _class_field_2 = "private field"

    def __init__(self, param1, param2):
        self.instance_field_1 = param1
        self._instance_field_2 = param2

    def public_method(self, arg1, arg2, arg3):
        if arg1:
            print("Arg1 is true")
        elif arg2 and arg3:
            print("Arg2 and Arg3 are true")
        else:
            print("No arguments are true")

    def _private_method(self):
        for i in range(5):
            print(i)

    def complex_method(self, x):
        if x > 10:
            for i in range(x):
                if i % 2 == 0:
                    print(f"Even: {i}")
        else:
            while x > 0:
                print(x)
                x -= 1


def standalone_function(y):
    if y > 5:
        return y * 2
    return y + 2
