import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('127.0.0.1', 8888))

    # Receive the quote from the server
    quote = client_socket.recv(1024).decode()

    print("Quote received:")
    print(quote)

    client_socket.close()

if __name__ == "__main__":
    main()
