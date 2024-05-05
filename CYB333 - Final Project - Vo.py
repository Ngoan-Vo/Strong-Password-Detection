# Import the regular expression module
import re
# Define the function to check if password is strong
def strong_password(password):
# Check if password is at least eight characters long
    if len(password) < 8:
        return False
# Check if password contains at least one UPPERCASE letter
    if not re.search('[A-Z]', password):
        return False
# Check if password contains at least one lowercase letter
    if not re.search('[a-z]', password):
        return False
# Check if password contains at least one digit
    if not re.search('[0-9]', password):
        return False
# Check if password contains at least one special character
    if not re.search('[!@#$%^&*()_+{}|:"<>?]', password):
        return False
# If all checks pass, password is strong
    return True
# Ask user to try again until password is strong
while True:
# Ask user to enter a password
    user_password = input("\nPlease enter a password:" )
# Check if password entered is strong
    if strong_password(user_password):
        print("\nCongratulations! Password is strong.\n")
        break
    else:
        print("\nPassword is NOT strong. Please make sure that password is at least eight characters long and contains\nat least one UPPERCASE letter, one lowercase letter, one digit, and one special character.")
