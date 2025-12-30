import socket
import datetime

def start_honeypot(port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)

    print(f"[*] Kube-Trap active. Listening on port {port}...")

    while True:
        client_socket, addr = server.accept()
        print(f"[ALERT] Intrusion detected from IP: {addr[0]} at {datetime.datetime.now()}")

        client_socket.send(b"Error 403: Restricted Access. Your IP has been logged.\n")
        client_socket.close()

if __name__ == "__main__":
    start_honeypot()