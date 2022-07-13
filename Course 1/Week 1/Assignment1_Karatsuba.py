def mul(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    n = max(len(str(x)), len(str(y)))
    nhalf = n // 2
    a = x // (10 ** nhalf)
    b = x % (10 ** nhalf)
    c = y // (10 ** nhalf)
    d = y % (10 ** nhalf)

    ac = mul(a, c)
    bd = mul(b, d)
    abcd = mul(a + b, c + d)
    result = (10 ** (2 * nhalf)) * ac + (10 ** nhalf) * (abcd - ac - bd) + bd
    return result


a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
c = mul(a, b)
print(int(c))