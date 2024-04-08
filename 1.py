def f():
    return [43,65,3]

# print(f())
def gef():
    for el in [43,65,3]:
        yield el
s = gef()
print(next(s))
_ = next(s)
print(next(s))
