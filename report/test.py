from urllib import request

def test():
    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    # data = f.read()
    # print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data:', data.decode('utf-8'))

test()