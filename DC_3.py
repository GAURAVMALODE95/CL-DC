import random
import time
import threading

# Global variables to track servers
server_names = ["Server 1", "Server 2", "Server 3"]
server_connections = [0, 0, 0]  
round_robin_index = 0


print_lock = threading.Lock()

def handle_request(server_index):
    """Simulate a server handling a request"""
    server_name = server_names[server_index]
    
    # Increase active connections
    server_connections[server_index] += 1
    
    with print_lock:
        print(f"{server_name} is handling the request. Active connections: {server_connections[server_index]}")
    
    # Simulate processing time
    time.sleep(random.uniform(0.5, 1.5))
    
    # Decrease active connections
    server_connections[server_index] -= 1
    
    with print_lock:
        print(f"{server_name} has finished handling the request. Active connections: {server_connections[server_index]}")

def round_robin_distribution(client_id):
    """Round Robin algorithm: distribute requests in a circular manner"""
    global round_robin_index
    
    server_index = round_robin_index
    # Update the index for next request
    round_robin_index = (round_robin_index + 1) % len(server_names)
    
    with print_lock:
        print(f"Client {client_id} is sending a request to {server_names[server_index]} (Round Robin)")
    
    handle_request(server_index)

def least_connections_distribution(client_id):
    """Least Connections algorithm: send request to server with least active connections"""
    # Find server with least connections
    server_index = server_connections.index(min(server_connections))
    
    with print_lock:
        print(f"Client {client_id} is sending a request to {server_names[server_index]} (Least Connections)")
    
    handle_request(server_index)

def simulate_client_requests(client_id, algorithm):
    """Simulate a client sending multiple requests"""
    for _ in range(random.randint(3, 5)):  # Each client sends 3-5 requests
        if algorithm == 'round_robin':
            round_robin_distribution(client_id)
        else:  # least_connections
            least_connections_distribution(client_id)
        
        # Wait before sending the next request
        time.sleep(random.uniform(1, 3))

def main():
    # Choose the load balancing algorithm
    algorithm = 'least_connections'  # You can switch to 'round_robin'
    
    # Create and start client threads
    client_threads = []
    for i in range(5):  # 5 clients
        thread = threading.Thread(
            target=simulate_client_requests, 
            args=(i+1, algorithm)
        )
        client_threads.append(thread)
        thread.start()
    
    # Wait for all client threads to finish
    for thread in client_threads:
        thread.join()
    
    print("Simulation complete!")

if __name__ == "__main__":
    main()