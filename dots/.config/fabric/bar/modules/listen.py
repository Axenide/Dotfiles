import socket

def listen() -> str:
    host: str = 'localhost'
    port: int = 3142
    bufferSize: int = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                data: bytes = conn.recv(bufferSize)
                if not data:
                    break
                conn.sendall(data)
                conn.close()
                return data.decode()

if __name__ == "__main__":
    listen()
