from callLimit import callLimit
@callLimit(3)
def f():
    print ("f()")
@callLimit(3)
def g():
    print ("g()")
for i in range(3):
    f()
    g()