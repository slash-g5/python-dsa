def simpleInts():
    a = 1
    b = a
    b = 2
    print(f"b: {b}")
    print(f"a: {a}")


def simple_arrays():
    a = []
    b = a
    b.append(5)
    print(f"b: {b}")
    print(f"a: {a}")


def operations_on_simple_array():
    a = []
    b = a
    b.append(5)
    print(f"b: {b}")
    print(f"a: {a}")
    b[0] = 9
    print(f"b: {b}")
    print(f"a: {a}")
    b = 9
    print(f"b: {b}")
    print(f"a: {a}")


if __name__ == "__main__":
    # integers are immutable objects in python, hence modifying b won't change a
    simpleInts()
    # For arrays the value will change for both a and b
    simple_arrays()
    # operations on simple array
    operations_on_simple_array()
