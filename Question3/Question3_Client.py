import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 4444))

    pressure_bar = float(input("Enter pressure in bar: "))

    # Send the pressure in bar to the server
    client_socket.send(str(pressure_bar).encode())

    pressure_atmosphere = client_socket.recv(8)
    pressure_atmosphere = float(pressure_atmosphere)

    print(f"Received converted pressure in atmosphere: {pressure_atmosphere}")

    client_socket.close()

if __name__ == "__main__":
    main()
