def evaluate_password(password):
    # Define the set of special characters
    special_characters = {'!', '@', '#', '$', '%', '&', '*'}
    
    # Initialize counters
    number_count = 0
    special_count = 0
    
    # Check the length of the password
    if len(password) < 10:
        return 'Weak'
    
    # Iterate through each character in the password
    for char in password:
        if char.isdigit():
            number_count += 1
        elif char in special_characters:
            special_count += 1
    
    # Check the conditions for a strong password
    if number_count >= 1 and special_count >= 1:
        return 'Strong'
    else:
        return 'Weak'

# Prompt the user for input
input_password = input()

# Evaluate the password
result = evaluate_password(input_password)

# Print the output
print(result)