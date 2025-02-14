class CS313EException(Exception):
   pass

def f(n):
    x = {}
    if n == 2:
        assert False
    elif n == 3:
        raise CS313EException("CS313E Error Occurred")
    elif n == 4:
        x = int("Hello") # Will raise a ValueError
 
def g(n):
    try:
        print("try")
        f(n)
        print("body")
    except AssertionError:
        print("assertion")
    except CS313EException:
        print("CS313E")
    else:
        print("no exceptions")
    finally:
        print("clean up")
    print("end of g")
g(4)
