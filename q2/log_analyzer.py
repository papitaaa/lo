from collections import Counter

# Ask user for log file path
log_file = input("Enter path to log file: ")

total_requests = 0
errors_404 = 0
ip_counter = Counter()

try:
    with open(log_file, "r") as file:
        for line in file:
            total_requests += 1

            # Split line by spaces (common log format)
            parts = line.split()
            if len(parts) < 9:
                continue  # skip malformed lines

            ip = parts[0]
            status = parts[8]

            ip_counter[ip] += 1

            if status == "404":
                errors_404 += 1

    print(f"\nTotal Requests: {total_requests}")
    print(f"Number of 404 errors: {errors_404}")

    top_ips = ip_counter.most_common(3)
    print("\nTop 3 IP addresses:")
    for ip, count in top_ips:
        print(f"{ip} - {count} requests")

except FileNotFoundError:
    print("Log file not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")
