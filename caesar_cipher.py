# Caesar Cipher Encryption and Decryption Tool

print("=" * 45)
print("      CAESAR CIPHER ENCRYPTION TOOL")
print("=" * 45)

while True:

    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1" or choice == "2":

        message = input("Enter your message: ")

        try:
            shift = int(input("Enter shift value (1-25): "))

            shift = shift % 26

            # Reverse the shift for decryption
            if choice == "2":
                shift = -shift

            result = ""

            for character in message:

                if "A" <= character <= "Z":

                    position = ord(character) - ord("A")

                    new_position = (
                        position + shift
                    ) % 26

                    result += chr(
                        new_position + ord("A")
                    )

                elif "a" <= character <= "z":

                    position = ord(character) - ord("a")

                    new_position = (
                        position + shift
                    ) % 26

                    result += chr(
                        new_position + ord("a")
                    )

                else:
                    result += character

            if choice == "1":
                print("\nEncrypted Message:", result)

            else:
                print("\nDecrypted Message:", result)

        except ValueError:
            print("Please enter a valid shift number.")

    elif choice == "3":

        print("Exiting Caesar Cipher Tool.")
        break

    else:
        print("Invalid choice. Select 1, 2, or 3.")
