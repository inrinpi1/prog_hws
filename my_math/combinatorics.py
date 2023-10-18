def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def permutation(n):
    return factorial(n)

def combination(n, m):
    return factorial(n) / (factorial(n - m) * factorial(m))

def arrangement(n, m):
    return factorial(n) / factorial(n - m)


if __name__ == '__main__':
    print('Пожалуйста, запустите головной файл.')
