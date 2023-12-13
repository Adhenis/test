def caddies(n):
    a = 450
    b = 250
    c = 300
    i = 1
    while n >= i and c > 0.0:
        d = a * 0.12
        e = b * 0.12
        f = c * (2 / 100)
        a = a - d + e + f
        b = b - e
        c = c - c * (4 / 100)
        i += 1
    return a, b, c




def seuilcaddies(M):
    a = 450
    b = 250
    i = 0
    while caddies(i)[0] + caddies(i)[1] < M:
        i += 1
    return i

print(seuilcaddies(1000))


def zerocaddies():
    a = 450
    b = 250
    c = 300
    i = 0
    while c > 0:
        d = a * 0.12
        e = b * 0.12
        f = c * (2 / 100)
        a = a - d + e + f
        b = b - b * 0.12
        c = c - c * (4 / 100)
        i += 1
    return i