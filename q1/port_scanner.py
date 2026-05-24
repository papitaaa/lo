import socket

# Ask user for target host
target = input("Enter hostname or IP address: ")

print(f"\nScanning {target}...\n")

# Scan ports from 1 to 1024
for port in range(1, 1025):
    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout so scan doesn't hang
        s.settimeout(0.5)

        # Try connecting to the port
        result = s.connect_ex((target, port))

        # If result is 0, port is open
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"

            print(f"Port {port} is OPEN ({service})")

        s.close()

    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        break

    except socket.gaierror:
        print("Hostname could not be resolved.")
        break

    except socket.error:
        print("Could not connect to server.")
        break
