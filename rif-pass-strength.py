import tkinter as tk
from tkinter import simpledialog, messagebox

def evaluate_password(password):
    # Define the set of special characters
    special_characters = {'!', '@', '#', '$', '%', '&', '*'}

    # Initialize counters
    number_count = 0
    special_count = 0
    upper_count = 0
    lower_count = 0
    consecutive_count = 0
    max_consecutive = 0
    last_char = ''

    # Check the length of the password
    if len(password) < 10:
        return 'Weak: Password must be at least 10 characters long.'

    # Iterate through each character in the password
    for char in password:
        if char.isdigit():
            number_count += 1
        elif char in special_characters:
            special_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

        # Check for consecutive characters
        if char == last_char:
            consecutive_count += 1
        else:
            consecutive_count = 1
        last_char = char
        max_consecutive = max(max_consecutive, consecutive_count)

    # Check the conditions for a strong password
    if number_count >= 1 and special_count >= 1 and upper_count >= 1 and lower_count >= 1 and max_consecutive < 3:
        return 'Strong'
    else:
        feedback = []
        if number_count < 1:
            feedback.append('at least one digit')
        if special_count < 1:
            feedback.append('at least one special character')
        if upper_count < 1:
            feedback.append('at least one uppercase letter')
        if lower_count < 1:
            feedback.append('at least one lowercase letter')
        if max_consecutive >= 3:
            feedback.append('no more than two consecutive identical characters')
        return 'Weak: ' + ', '.join(feedback)

# Create a simple GUI for password input
root = tk.Tk()
root.withdraw()  # Hide the main window

input_password = simpledialog.askstring("Password Input", "Enter a password to evaluate:")

# Evaluate the password
result = evaluate_password(input_password)

# Show the result in a message box
messagebox.showinfo("Password Strength", result)
