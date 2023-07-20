import socket

# Function to convert pressure from bar to atmosphere
def convert_to_atmosphere(pressure_bar):
    return pressure_bar * 0.986923 # Conversion factor from bar to atmosphere

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 4444))
    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()

        pressure_bar = client_socket.recv(8)
        pressure_bar = float(pressure_bar)

        # Convert the pressure from bar to atmosphere
        pressure_atmosphere = convert_to_atmosphere(pressure_bar)

        # Send the converted pressure value back to the client
        client_socket.send(str(pressure_atmosphere).encode())

        client_socket.close()

if __name__ == "__main__":
    main()
