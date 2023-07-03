def check_pin():
    # Hard-coded PIN
    correct_pin = "1234"

    while True:
        # Take input from the keyboard
        pin = input("Enter your PIN: ")

        # Check if the entered PIN matches the correct PIN
        if pin == correct_pin:
            print("PIN accepted. Access granted.")
            break  # Exit the loop if the PIN is correct
        else:
            print("Incorrect PIN. Please try again.")

# hi
# Call the function to start checking the PIN
check_pin()
