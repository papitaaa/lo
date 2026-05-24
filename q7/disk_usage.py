import shutil
import datetime

# Step 1: Get disk usage for root partition
total, used, free = shutil.disk_usage("/")

# Step 2: Calculate percentage used
usage = (used / total) * 100

# Step 3: Check if usage > 80%
if usage > 0:
    log_message = f"{datetime.datetime.now()}: WARNING - Disk usage is at {usage:.2f}%\n"
    with open("/home/saksh/plment/q7/Newlogfile", "a") as log_file:
        log_file.write(log_message)

