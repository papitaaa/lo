import hashlib

# Step 1: Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Step 2: Store a password (hashed)
stored_password_hash = hash_password("mypassword123")

# Step 3: Ask user to log in
login_input = input("Enter your password: ")

# Step 4: Verify login
if hash_password(login_input) == stored_password_hash:
    print("✅ Login successful!")
else:
    print("❌ Wrong password, try again.")

