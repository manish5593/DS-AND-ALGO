def prod(a, b):
    output = a*b
    return output

def fact():
    i = 1
    n= i
    while True:
        output = prod(i, n)
        yield output
        i += 1
        n = output


manish = fact()
num = 5
for i in range(num):
    print(next(manish))




# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120
