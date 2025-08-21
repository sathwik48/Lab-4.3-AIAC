import getpass

def collect_user_data():
    # Collect user data
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    # Ask for password (input hidden)
    password = getpass.getpass("Set a password to protect your data: ")

    print("\n--- Data Collected ---")
    print(f"Name: {name}")
    print(f"Age: {age}")

    # Hide the important part of the email (before @)
    if "@" in email:
        hidden_email = '*' * 5 + email[email.find('@'):]
    else:
        hidden_email = "Invalid email format"

    print(f"Email: {hidden_email}")

    # Note: Password is not displayed for security

# Run the function
if __name__ == "__main__":
    collect_user_data()