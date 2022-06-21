import string
import random

initialString = """
    **********
    This program is desiged to create randomly generated passwords according to user\'s desired characters.
    The program supports following characters for password. CTRL+C to terminate the program.

    - Uppercase and lowercase alphabetich characters (A/a...z/Z).
    - Numeric characters (1...9).
    - Special charcters (!@#$%^&*()-_=+-?<>.,).
    - Custom characters.
    **********
"""
print(initialString)

def generatePassword():
    # User can continue loop 3 times
    userTryCount = 3

    while True:
        # Characters to be used in the password.
        chars = []

        # Define the password generated.
        generatedPassword = []
        generatedPassword_str = ""

        # Get the password length from user and typecast into int.
        try:
            passLength = int(input("\nDesired password length: "))
        except ValueError:
            userTryCount -= 1

            if userTryCount > 0:
                print(
                    f"Password length can be only numeric value. Please try again. {userTryCount}/3 try left.\n")
                continue
            else:
                print(
                    f"Password length can be only numeric value. {userTryCount}/3 try left. Program is terminated.\n")
                break
        else:
            userTryCount = 3

        # Get the character type preference from the user.
        # Check if user wants uppercase characters.
        for i in range(4):
            uppercasePreference = input(
                "\nUppercase Preference\nWould you like to have uppercase alphabetic characters? (y/n): ")

            if uppercasePreference == "y":
                isUppercase = True
                break
            elif uppercasePreference == "n":
                isUppercase = False
                break
            else:
                userTryCount -= 1

                if userTryCount > 0:
                    print(
                        f"Uppercase preference can be only yes(y) or no(n). Please try again. {userTryCount} try left.\n")
                    continue
                else:
                    print(
                        f"Uppercase preference can be only yes(y) or no(n). {userTryCount} try left. Program is terminated.\n")
                    break

        if userTryCount == 0:
            break
        else:
            userTryCount = 3

        # Check if user wants lowercase characters
        for i in range(4):
            lowercasePreference = input(
                "\nLowercase Preference\nWould you like to have lovercase alphabetic characters? (y/n): ")

            if lowercasePreference == "y":
                isLowercase = True
                break
            elif lowercasePreference == "n":
                isLowercase = False
                break
            else:
                userTryCount -= 1

                if userTryCount > 0:
                    print(
                        f"Lowercase preference can be only yes(y) or no(n). Please try again. {userTryCount} try left.\n")
                    continue
                else:
                    print(
                        f"Lowercase preference can be only yes(y) or no(n). {userTryCount} try left. Program is terminated.\n")
                    break

        if userTryCount == 0:
            break
        else:
            userTryCount = 3

        # Check if user wants numeric characters.
        for i in range(4):
            digitPreference = input(
                "\nDigit Preference\nWould you like to have numeric characters? (y/n): ")

            if digitPreference == "y":
                isDigit = True
                break
            elif digitPreference == "n":
                isDigit = False
                break
            else:
                userTryCount -= 1

                if userTryCount > 0:
                    print(
                        f"Digit preference can be only yes(y) or no(n). Please try again. {userTryCount} try left./n")
                    continue
                else:
                    print(
                        f"Digit preference can be only yes(y) or no(n). {userTryCount} try left. Program is terminated.\n")
                    break

        if userTryCount == 0:
            break
        else:
            userTryCount = 3

        # Check if user wants special characters.
        for i in range(4):
            specialCharPreference = input(
                "\nSpecial Character Preference\nWould you like to have special characters (!@#$%^&*()-_=+-?<>.,)? (y/n): ")

            if specialCharPreference == "y":
                isSpecial = True
                break
            elif specialCharPreference == "n":
                isSpecial = False
                break
            else:
                userTryCount -= 1

                if userTryCount > 0:
                    print(
                        f"Special character preference can be only yes(y) or no(n). Please try again. {userTryCount} try left.\n")
                    continue
                else:
                    print(
                        f"Special character preference can be only yes(y) or no(n). {userTryCount} try left. Program is terminated.\n")
                    break

        if userTryCount == 0:
            break
        else:
            userTryCount = 3

        # Check if user wants custom characters.
        for i in range(4):
            customCharPreference = input(
                "\nCustom Character Preference\nWould you like to have custom characters? (y/n): ")

            if customCharPreference == "y":
                isCustom = True
                userDefinedCustomChars = input(
                    "\nEnter custom characters you would like to use (enter characters without any seperator): ")
                startOver = False
                exitProgram = False
                break
            elif customCharPreference == "n":

                if not isUppercase or not isLowercase or not isDigit or not isSpecial:
                    noPrefSelected_input = input(
                        "\nYou havent selected any character preference, at least one character preference should be selected.\nPress 'y' to start over or press any other key to terminate program: ")

                    if noPrefSelected_input == "y":
                        startOver = True
                        exitProgram = False
                        break
                    else:
                        startOver = False
                        exitProgram = True
                        break
                else:
                    isCustom = False
                    startOver = False
                    exitProgram = False
                    break
            else:
                userTryCount -= 1

                if userTryCount > 0:
                    print(
                        f"Custom character preference can be only yes(y) or no(n). Please try again. {userTryCount} try left.\n")
                    continue
                else:
                    print(
                        f"Custom character preference can be only yes(y) or no(n). {userTryCount} try left. Program is terminated.\n")
                    break

        if startOver:
            continue

        if userTryCount == 0 or exitProgram:
            break
        else:
            userTryCount = 3

        # Get the user's desire
        # chars = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()-_=+-?<>.,")

        if isUppercase:
            chars.extend(list(string.ascii_uppercase))
        if isLowercase:
            chars.extend(list(string.ascii_lowercase))
        if isDigit:
            chars.extend(list(string.digits))
        if isSpecial:
            chars.extend(list("!@#$%^&*()-_=+-?<>.,"))
        if isCustom:
            chars.extend(list(userDefinedCustomChars))

        # print(chars)

        # Shuffle chars randomly.
        random.shuffle(chars)

        # Pick random characters from chars and write into generatedPassword.
        for i in range(passLength):
            generatedPassword.append(random.choice(chars))

        # Shuffle the generatedPassword list.
        random.shuffle(generatedPassword)

        # Convert generatedPassword list into string.
        generatedPassword_str = generatedPassword_str.join(generatedPassword)

        # Print the generated password out.
        print(
            f"\nYour {passLength} character long password is: {generatedPassword_str}")

        for i in range(4):
            generateMore = input(
                "\nGenerate another password: 'y' | Terminate program: 'n' ")

            if generateMore == "n":
                exitProgram = True
                break
            elif generateMore == "y":
                exitProgram = False
                break
            else:
                userTryCount -= 1

                if userTryCount > 0:
                    print(
                        f"Please only use yes(y) or no(n) for the question. Please try again. {userTryCount} try left.\n")
                    continue
                else:
                    print(
                        f"Please only use yes(y) or no(n) for the question. {userTryCount} try left. Program is terminated.\n")
                    break

        if userTryCount == 0 or exitProgram:
            break
        else:
            userTryCount = 3


generatePassword()
