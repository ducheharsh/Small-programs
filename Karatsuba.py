def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y

    m = max(len(str(x)), len(str(y)))
    m2 = m // 2

    high1, low1 = divmod(x, 10**m2)
    high2, low2 = divmod(y, 10**m2)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**m2) + z0

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
result = karatsuba(x, y)
print(result)
