import getpass

def check_pin():
    # Hard-coded PIN
    correct_pin = "1234"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        # Take input from the user without displaying it
        pin =input("Enter your PIN: ")

        # Check if the entered PIN matches the correct PIN
        if pin == correct_pin:
            print("PIN accepted. Access granted.")
            break  # Exit the loop if the PIN is correct
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Incorrect PIN. {remaining_attempts} attempts remaining.")

    if attempts == max_attempts:
        print("Maximum number of attempts reached. Access denied.")


# Call the function to start checking the PIN
check_pin()
