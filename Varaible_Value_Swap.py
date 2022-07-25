a = 10
b = 12

if b > a:
    b = (b - a)
    a = b + a
    b = a - b
    print(a)
    print(b)
elif a > b:
    b = (a - b)
    a = a - b
    b = b + a
    print(a)
    print(b)
