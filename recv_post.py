from urllib import request
from urllib import parse
import socket

def post_url(data):
    #发送的数据
    values = {
        'recv_data' : data,
    }
    #数据进行编码处理
    data = parse.urlencode(values)
    #数据应该为bytes
    data = data.encode('utf-8')
    #发起请求
    req = request.Request(url,data,headers)
    res = request.urlopen(req)
    print('request over')
    #请求返回的相应对象
    # with request.urlopen(req) as response:
    #     the_page = response.read()

if __name__ =='__main__':
    response = 'copy that'
    HOST = "127.0.0.1"
    POST = 8001
    BUFSIZ = 1024
    ADDR = (HOST, POST)

    url = "http://127.0.0.1:8000/recv_data/"
    User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    headers = {'User-Agent':User_Agent}

    sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sever.bind(ADDR)
    sever.listen(5)
    while True:
        print("waiting for connection...")
        conn, addr = sever.accept()
        while True:
            data = conn.recv(BUFSIZ)
            if not data:
                break
            print('recv: ',data)
            conn.send(response.encode('utf-8'))
            #post_url(data)
        conn.close()
    sever.close()
