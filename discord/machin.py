
def reduction(a,b):
    if a > 4:
        b = b-b*(15/100)
    if 2<=a<=4:
        b = b-b*(8/100)
    if a == 1:
        b = b-b*(1/100)
    if a == 0:
        b = "client pas venu"
    return a,b
print(reduction(5,54))