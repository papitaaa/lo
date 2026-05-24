from collections import Counter
import re

# Log file path
log_file = "/var/log/auth.log"

# Counters
failed_logins = 0
ssh_failed_ips = Counter()
local_failed_users = Counter()

try:
    with open(log_file, "r") as file:
        for line in file:

            # --- SSH failed logins with IPs ---
            if "Failed password" in line:
                failed_logins += 1
                # Extract IP
                match_ip = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if match_ip:
                    ip = match_ip.group(1)
                    ssh_failed_ips[ip] += 1

            # --- Local login failures (GUI/console) ---
            elif "Failed login" in line or "password check failed" in line:
                failed_logins += 1
                # Extract username if available
                match_user = re.search(r"user \(?(.*?)\)?$", line.strip())
                if match_user:
                    user = match_user.group(1)
                    local_failed_users[user] += 1

    # --- Output Results ---
    print(f"\nTotal Failed Logins Detected: {failed_logins}\n")

    if ssh_failed_ips:
        print("Suspicious SSH IPs (>5 failed attempts):")
        for ip, count in ssh_failed_ips.items():
            if count > 5:
                print(f"  {ip} - {count} failed attempts")
    else:
        print("No suspicious SSH login attempts detected.")

    if local_failed_users:
        print("\nLocal login failures by username:")
        for user, count in local_failed_users.items():
            print(f"  {user} - {count} failed attempts")
    else:
        print("\nNo local login failures detected.")

except FileNotFoundError:
    print("Log file not found.")
except PermissionError:
    print("Permission denied. Try running with sudo.")
except Exception as e:
    print("Error:", e)
