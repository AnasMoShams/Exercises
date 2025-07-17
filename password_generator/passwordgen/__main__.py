import string
import random
import datetime

def generate_password(characters_number):
    # Created a random letter 
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    # Shuffle letters
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    # Calculate password parts
    part1 = round(characters_number * (30/100))
    part2 = round(characters_number * (20/100))

    password = []

    for i in range(part1):
        password.append(s1[i])
        password.append(s2[i])

    for n in range(part2):
        password.append(s3[n])
        password.append(s4[n])

    # Shuffle and join password
    random.shuffle(password)
    password = "".join(password[0:characters_number])

    return password


def main():
    while True:
        # Enter len(password)
        name_website = input("What is the name of the website for which you need a password? ")
        
        while True:
            try:
                characters_number = int(input("How many characters for the password:? "))
                if characters_number < 8:
                    print("You need at least 8 characters.")
                else:
                    break
            except ValueError:
                print("Please enter numbers only.")
        
        password = generate_password(characters_number)

        print(f"\nThe number password is => ({characters_number})\nYour password is => {password}\nFor website: {name_website}")

        # Save password
        file_path = r"E:\Python\password_generator\stored password.txt"
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        curent_minet = datetime.datetime.now().strftime("%H:%M")
        try:
            with open(file_path, "a") as file:
                file.write(f'The password you generated is: "{password}", for "{name_website}", date: {current_date}, time: {curent_minet}\n')
            print("\nPassword saved successfully.")
        except Exception as e:
            print(f"\nError writing to file: {e}")

        cont = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
