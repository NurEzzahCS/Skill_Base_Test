import socket
import requests

def connect_to_server():
    host = "izani.synology.me"
    port = 8443
    data_to_send = "2021609822"

    try:
        # Create a socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Send data to the server
        client_socket.sendall(data_to_send.encode())

        # Read the server's response
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

        # Close the socket connection
        client_socket.close()

        # Return the URL received from the server
        return response.strip()

    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    server_url = connect_to_server()
    if server_url:
        try:
            response = requests.get(server_url)
            print(response.text)
        except Exception as e:
            print("Error:", e)
