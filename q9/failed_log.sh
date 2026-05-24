#!/bin/bash

# Step 1: Look for "Failed password" entries in auth.log
# Step 2: Show the last 10 attempts

grep "permission" /var/log/auth.log | tail -n 10
