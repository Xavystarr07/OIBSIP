import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generate a random password based on user-defined criteria.
    """
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    """
    Get user input for password criteria.
    """
    try:
        length = int(input("Enter the desired password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        return length, use_letters, use_numbers, use_symbols
    except ValueError:
        print("Please enter a valid numerical value for password length.")
        return get_user_input()

def main():
    print("StarrX Password Generator")
    print("-------------------")

    length, use_letters, use_numbers, use_symbols = get_user_input()
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()

