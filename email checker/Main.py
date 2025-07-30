from email_validator import validate_email, EmailNotValidError

email = input("Enter Email address: ")

try:
    # Validate and normalize the email
    valid = validate_email(email)
    email = valid.email

    # Check if it's a Gmail address
    if email.endswith("@gmail.com"):
        username = email[:-10]  # Extract username part
        if len(username) >= 6:
            print("✅ Valid Gmail address")
        else:
            print("❌ Gmail username must be at least 6 characters long")
    else:
        print("✅ Valid email, but not a Gmail address")

except EmailNotValidError as e:
    print(f"❌ Invalid email: {e}")

