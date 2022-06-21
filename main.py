initialString = """
**********
Available Programs
0 - Exit Program
1 - Password Generator
**********
"""
print(initialString)
userTryCount = 3


def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())


while True:
    try:
        programToRun = int(input(
            "Program Select.\nWhich program would you like to run?\nEnter program number: "))
    except ValueError:
        userTryCount -= 1

        if userTryCount > 0:
            print(
                f"\nOnly numeric value can be entered for program select. Please try again. {userTryCount}/3 try left.\n")
            continue
        else:
            print(
                f"\nOnly numeric value can be entered for program select. {userTryCount}/3 try left. Program terminated\n")
            break
    else:
        userTryCount = 3

        if programToRun == 0:
            print("\n**********\nProgram terminated\n**********\n")
            break
        elif programToRun == 1:
            print("\n**********\nPassword Generated Selected\n**********\n")
            run("password-generator/PasswordGenerator.py")
        else:
            print(
                "\nThere is no available preogram in selected number. Program terminated.\n")
            break
