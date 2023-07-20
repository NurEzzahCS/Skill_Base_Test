#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

// Function to generate a random number between 100 and 999
int getRandomNumber() {
    int num;
    int i;
    for (i = 0; i < 1; i++) {
        int num = (rand() % (999 - 100 + 1)) + 100;
        printf("%d ", num);
    }
    return num; 
}

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);

    // Create socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8443);

    // Bind the socket to a specific address and port
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Listen for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    while (1) {
        // Accept an incoming connection
        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
            perror("Accept failed");
            exit(EXIT_FAILURE);
        }

        // Generate the random number
        int random_number = getRandomNumber();
        char buffer[4]; // For storing the random number as a string

        // Convert the integer to a string
        printf(buffer, sizeof(buffer), "%d", random_number);

        // Send the random number to the client
        send(new_socket, buffer, strlen(buffer), 0);

        printf("Random number sent to client: %d\n", random_number);

        close(new_socket); // Close the client socket
    }

    return 0;
}
