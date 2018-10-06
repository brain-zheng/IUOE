import socket
import time

HOST = "127.0.0.1"
POST = 8001
BUFSIZ = 1024
ADDR = (HOST, POST)
data_list = [
    '123A465V591W852C',
    '456A159V789W852C',
    '789A756V856W852C',
    '147A153V652W852C',
    '258A842V254W852C',
    '369A599V458W852C',
]



while True:
    client = socket.socket()
    client.connect(ADDR)
    for data in data_list:
        client.send(data.encode('utf-8'))
        time.sleep(2)
        data = client.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))

client.close()