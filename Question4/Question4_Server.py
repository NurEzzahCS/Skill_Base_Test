import socket
import threading
import random

# List of quotes
quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "In a gentle way, you can shake the world. - Mahatma Gandhi",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson"
]

def handle_client(client_socket):
    # Get a random quote
    quote = random.choice(quotes)

    # Send the quote to the client
    client_socket.send(quote.encode())
    print(f"Sending the following quote to the client: {quote}")

    # Close the connection
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"\nConnection accepted from {client_address}")

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
