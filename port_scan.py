import socket
import threading
# this code find open ports on related IP
# create a TCP socket
# SOCK_STREAM -> TCP

open_port = []


def scan_port(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # her defasında yeniden socket olusturmak lazım.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # TCP connect?
        s.connect((ip, port))

        open_port.append(port)
        print("port: ", str(port), "open")

    except Exception as e:
        print(str(port), "closed", e)
    finally:
        s.close()


def main():
    ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()
        thread.join()

    print("Open port on IP:")
    print(open_port)


if __name__ == "__main__":
    main()
