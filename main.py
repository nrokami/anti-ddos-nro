import socket
import threading

# Configuration
THRESHOLD = 100  # number of requests
TIME_FRAME = 60  # in seconds
blacklist = set()
request_count = {}

# Function to handle incoming requests
def handle_request(ip):
    if ip in blacklist:
        print(f"Blocked request from: {ip}")
        return
    if ip not in request_count:
        request_count[ip] = 0
    request_count[ip] += 1
    
    # Check if the IP exceeds the threshold
    if request_count[ip] >= THRESHOLD:
        print(f"IP {ip} is exceeding request limits and has been blacklisted.")
        blacklist.add(ip)
        # Optionally block the IP address here
    
    # Reset the count after the time frame
    threading.Timer(TIME_FRAME, reset_count, [ip]).start()

# Reset request count for a specific IP
def reset_count(ip):
    if ip in request_count:
        request_count[ip] -= 1
        if request_count[ip] <= 0:
            del request_count[ip]

# Main function to simulate receiving requests
if __name__ == '__main__':
    # Simulate receiving requests
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(5)
    print("Listening for incoming requests...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Received request from: {addr}")
        handle_request(addr[0])
        client_socket.close()