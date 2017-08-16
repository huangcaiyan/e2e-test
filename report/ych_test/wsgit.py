from wsgiref.simple_server import make_server

#静态返回Hello world
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1>Hello world</h1>']

#动态返回Hello ****
def application1(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body = '<h1>Hello,%s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

def webServer():
    httpd = make_server('',8000,application1)
    print("Server HTTP on port 8000...........")
    httpd.serve_forever()

webServer()