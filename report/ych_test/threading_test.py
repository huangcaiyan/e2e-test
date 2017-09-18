from time import sleep,ctime
import threading

def music(musicName):
    for i in range(2):
        print('I was listening to %s! %s'%(musicName,ctime()))
        sleep(2)

def movie(moiveName,loop):
    for i in range(loop):
        print('I was at the %s! %s'%(moiveName,ctime()))
        sleep(5)

threads = []
# t1 = threading.Thread(target=music,args=('爱情买卖',2))
# threads.append(t1)
# t2 = threading.Thread(target=movie,args=('阿发达',2))
# threads.append(t2)
nameList = ['讲经说法的','收到了福建师范']
for name in nameList:
    t = threading.Thread(target=music,args=(name,))
    threads.append(t)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print('all end:%s'%ctime())