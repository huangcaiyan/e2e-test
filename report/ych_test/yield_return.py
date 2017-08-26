def r_return(n):
    print('you taked me')
    while n > 0:
        print('before return')
        return n
        n -= 1
        print('after return')

# r_return(3)

def y_yield(n):
    print('you taked me')
    while n > 0:
        print('before return')
        yield n
        n -= 1
        print('after return')

yy = y_yield(3)
for i in yy:
    print(i)