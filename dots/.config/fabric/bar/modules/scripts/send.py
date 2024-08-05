import sys
import socket

def main():
    if len(sys.argv) != 2:
        print("Uso: python enviar.py <mensaje>")
        sys.exit(1)

    host = 'localhost'
    port = 3142

    mensaje = sys.argv[1]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(mensaje.encode())
        print(f'Mensaje enviado: {mensaje}')

if __name__ == "__main__":
    main()
