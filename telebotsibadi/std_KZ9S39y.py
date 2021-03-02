a = input()
b = input()
c = input()
if b > a:
    if c > a:
        print(a, "min")
    elif c == a:
        print(a, c,  "min")
    else:
        print(c, "min")
elif b == a:
    if c > a:
        print(a, b , "min")
    elif c == a:
        print(a, b, c, "min")
    else:
        print(c, "min")
else:
    if c > b:
        print(b, " min")
    elif c == b:
        print(b, c,  "min")
    else:
        print(c, "min")