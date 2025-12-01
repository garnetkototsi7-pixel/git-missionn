import bcrypt  # for secure password hashing
import os      # for file path checking
import re      # for regular expressions in validation

# define the file where user data is stored
USER_DATA_FILE = "users.txt"

def hash_password(plain_text_password):
    """Hashes the plain text password using bcrypt."""
    # converting password to bytes
    password_bytes = plain_text_password.encode('utf-8')
    # generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed = bcrypt.hashpw(password_bytes, salt)
    # Convert the hash from bytes to string
    hashed_str = hashed.decode('utf-8')
    return hashed_str

def verify_password(plain_text_password, hashed_password):
    """Verifies a plain text password against a stored bcrypt hash."""
    try:
        # Encode both the plaintext password and the stored hash to bytes
        password_bytes = plain_text_password.encode('utf-8')
        # The stored hash is already a string, so encode it
        stored_hash_bytes = hashed_password.encode('utf-8')
        # Verify using bcrypt
        return bcrypt.checkpw(password_bytes, stored_hash_bytes)
    except ValueError:
        # Catch errors if the hash is malformed or invalid
        return False


def user_exists(username):
    """Checks if a username already exists in the data file."""
    # Handle the case where the file doesn't exist yet
    if not os.path.exists(USER_DATA_FILE):
        return False

    # Read the file and check each line for the username
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            try:
                # Assuming format: username:hashed_password
                stored_username = line.strip().split(":")[0]
                if stored_username == username:
                    return True
            except IndexError:
                # Skip malformed lines
                continue
    return False 


def register_user(username, password):
    """Registers a new user by hashing the password and saving to file."""
    # Check for existing username (FIXED: Using user_exists function)
    if user_exists(username):
        print(f"Registration failed: Username '{username}' already exists.")
        return False
        
    # Hash the password
    hashed_password = hash_password(password)
    
    # Append the new user to the file (FIXED: Corrected logic and appended hash)
    # The file is opened in append mode ('a')
    try:
        with open(USER_DATA_FILE, 'a') as f:
            # Data is stored as: username:hashed_password\n
            f.write(f"{username}:{hashed_password}\n")
        print(f"Success: User '{username}' registered successfully!")
        return True
    except IOError:
        print("Error: Could not write to user data file.")
        return False


def login_user(username, password):
    """Logs in a user by verifying the password against the stored hash."""
    # Handle the case where no users are registered yet
    if not os.path.exists(USER_DATA_FILE):
        print("Error: No users registered yet.")
        return False
        
    # Search for the username in the file
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            try:
                # Format: stored_username:stored_hash
                stored_username, stored_hash = line.strip().split(":")
                
                # If username matches, verify the password
                if stored_username == username:
                    # Use verify_password with the stored HASH
                    if verify_password(password, stored_hash):
                        print(f"Success: Welcome, {username}!")
                        return True
                    else:
                        print("Error: Invalid password.") # Test 4
                        return False
            except IndexError:
                # Skip malformed lines
                continue 

    print("Error: Username not found.") # Test 5
    return False


def validate_username(username):
    """Validates username requirements."""
    # Check length
    if len(username) < 3:
        return (False, "Username must be at least 3 characters long.")

    # Allowed characters: letters, digits, underscore
    if not re.match(r"^[A-Za-z0-9_]+$", username):
        return (False, "Username can only contain letters, numbers, and underscores.")

    return (True, "")

def validate_password(password):
    """Validates password requirements."""
    if len(password) < 6:
        return (False, "Password must be at least 6 characters long.")

    if " " in password:
        return (False, "Password cannot contain spaces.")

    # At least a single letter
    if not any(c.isalpha() for c in password):
        return (False, "Password must contain at least one letter.")

    # At least a single digit
    if not any(c.isdigit() for c in password):
        return (False, "Password must contain at least one number.")

    return (True, "")

def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*50)
    print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print(" Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)

def main():
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()

            # Validate username
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            password = input("Enter a password: ").strip()

            # Validate password
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Confirm password
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

            # Register the user
            register_user(username, password)

        elif choice == '2':
            # Login flow
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Attempt login (The print messages for success/failure are now inside login_user)
            if login_user(username, password):
                # This code runs only if login_user returned True (successful login)
                print("\nYou are now logged in.")
                # The line below is kept as per your original structure
                print("(In a real application, you would now access the d)") 

                # Ask if they want to logout or exit
                input("\nPress Enter to return to main menu...")
            # If login_user returns False, the error message is already printed inside it

        elif choice == '3':
            # Exit
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break

        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    # Ensure the user data file exists on first run
    if not os.path.exists(USER_DATA_FILE):
        open(USER_DATA_FILE, 'w').close()
    main()