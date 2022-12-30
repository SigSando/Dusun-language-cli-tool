import os
import colorama

#Iniialize
colorama.init()
# Create a dictionary of vowel and diphthong sounds and their corresponding IPA brackets
vowels_dict = {
    'a': '.aa(cat).',
    'e': '.e(hen).',
    'i': '.ei(pin).',
    'o': '.o(cot).',
    'u': '.uu(to).',
    'aa': '.ahh(car).',
    'ai': '.ai(mice).',
    'ii': '.ee(seed).',
    'oi': '.oe(oh e).',
    'uu': '.oo(moon).',
    'ng': '.nn(song).',
    'ngg': '.ng/g(ming-gisom).'
    
}

while True:
    # Prompt the user to enter a word
    word = input("Enter a word: ")

    # Initialize an empty string for the pronunciation
    pronunciation = ""

    # Iterate through the characters in the word
    for char in word:
        # Check if the character is in the vowels dictionary
        if char in vowels_dict:
            # Add the corresponding IPA bracket to the pronunciation string
            pronunciation += (colorama.Fore.WHITE) + f"{vowels_dict[char]}"
        else:
            # Add the character as is to the pronunciation string
            pronunciation += (colorama.Fore.RED) + f"{char}"
    # Reset the color to the default
    print(colorama.Style.RESET_ALL, end='')

    # Print the pronunciation of the word
    print("Pronunciation:", colorama.Fore.WHITE +  pronunciation)

    # Reset the color to the default
    print(colorama.Style.RESET_ALL, end='')

    # Prompt the user to enter a command
    command = input(colorama.Fore.BLUE + "Enter 'exit', 'clear', or Enter to Continue: ")

    # Check if the user wants to exit the program
    if command.lower() == 'exit':
        break
    # Check if the user wants to clear the output
    elif command.lower() == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
    
