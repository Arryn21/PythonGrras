def out(k):
    def inn(a, b):
        a, b = b, a
        return k(a, b)

    return inn


@out
def div(a, b):
    c = a / b
    return c


print(div(4, 2))
