import socket

# Ask user for input (domain or IP)
user_input = input("Enter a domain name or IP address: ").strip()

try:
    # Check if input is an IP address
    parts = user_input.split(".")
    is_ip = len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

    if is_ip:
        # Reverse DNS lookup for IP
        try:
            hostname = socket.gethostbyaddr(user_input)[0]
            print(f"Reverse DNS for IP {user_input}: {hostname}")
        except socket.herror:
            print(f"Reverse DNS for IP {user_input}: Not available")
    else:
        # Domain → IP
        ip_address = socket.gethostbyname(user_input)
        print(f"IP address of {user_input}: {ip_address}")

        # Also do reverse DNS for this IP
        try:
            reverse_dns = socket.gethostbyaddr(ip_address)[0]
            print(f"Reverse DNS: {reverse_dns}")
        except socket.herror:
            print("Reverse DNS: Not available")

except socket.gaierror:
    print("Error: Domain name could not be resolved.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
