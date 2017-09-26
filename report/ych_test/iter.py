class MyRange(object):
    def __init__(self,n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

#斐波那契数列
class Fibs(object):
    def __init__(self,max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration()

        self.a,self.b = self.b,self.a + self.b
        return fib

#斐波那契数列 yield
def fibs_yield(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a + b
        n = n + 1

#生成器方法 在开始运行后可以为生成器提供新的值，类似生成器与“外界”进行数据交流
def repeater(n):
    while True:
        n = (yield n)

if __name__ =='__main__':
    #自定义迭代
    # x = MyRange(7)
    # # print('x.next():' + str(x.__next__()))
    # # for i in x:
    # #     print(i)

    # print(list(x))
    # print(x.__next__())

    #斐波那契数列
    # fibs = Fibs(5)
    # print(list(fibs))

    #斐波那契数列 yield
    # ff = fibs_yield(5)
    # for i in ff:
    #     print(i)

    #生成器方法 send()方法必须在生成器运行后并挂起才能使用，即yield至少被执行一次
    r = repeater(3)
    # print(r.send(None))
    print(r.__next__())
    print(r.send('y'))
    r.close()
    

