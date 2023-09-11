import socket

# create a TCP socket
# SOCK_STREAM -> TCP

ip = "10.0.2.7"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for port in range(1, 100):
    try:
        # her defasında yeniden socket olusturmak lazım.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5.0)
        s.connect((ip, port))
        response = s.recv(1024)

        print(str(port), "open : Banner: ", response.decode())
    except socket.timeout as t:
        if port == 80:
            http_message = "GET / HTTP/1.0\r\n\r\n"
            s.send(http_message.encode())
            http_recv = s.recv(1024)
            print(str(port), "open : Banner: ", http_recv.decode())
        else:
            print(str(port), "use different method")

    except Exception as e:
        pass
    finally:
        s.close()
