import random
import colorama

# Initialize the library
colorama.init()

# Create a dictionary of Dusun numbers and English Counterparts
words_dict = {
    1: ['one', 'iso'],
    2: ['two', 'duo'],
    3: ['three', 'tolu'],
    4: ['four', 'apat'],
    5: ['five', 'lim'],
    6: ['six', 'onom'],
    7: ['seven', 'turu'],
    8: ['eight', 'walu'],
    9: ['nine', 'siam'],
    10: ['ten', 'opod'],
    11: ['eleven', 'opod om iso'],
    12: ['twelve', 'opod om duo'],
    13: ['thirteen', 'opod om tolu'],
    14: ['fourteen', 'opod om apat'],
    15: ['fifteen', 'opod om lim'],
    16: ['sixteen', 'opod om onom'],
    17: ['seventeen', 'opod on turu'],
    18: ['eighteen', 'opod om walu'],
    19: ['nineteen', 'opod om siam'],
    20: ['twenty', 'duo noopod']
}


# Prompt the user to select a difficulty level
difficulty = input(colorama.Fore.BLUE + "\nSelect a difficulty level (easy, medium, hard): " + colorama.Fore.WHITE)

while True:
  # Generate a random number based on the selected difficulty level
  if difficulty == "easy":
    selected_number = random.randint(1, 10)
  elif difficulty == "medium":
    selected_number = random.randint(1, 15)
  elif difficulty == "hard":
    selected_number = random.randint(1, 20)
  else:
    print(colorama.Fore.RED + "\nInvalid difficulty level. Please try again.")
    break

  # Print the random number
  print(colorama.Fore.GREEN + "\nNumber:", selected_number)

  # Prompt the user to enter the Dusun spelling and number of the word
  guess = input(colorama.Fore.BLUE + "Enter the Dusun word for this number (or type 'quit' to exit): " + colorama.Fore.WHITE)

  # Reset the color to the default
  print(colorama.Style.RESET_ALL, end='')

  # Check if the user wants to quit
  if guess.lower() == 'quit':
    break

  # Check if the guess is correct
  if guess.lower() in [word.lower() for word in words_dict[selected_number]]:
    print(colorama.Fore.GREEN + "\033[1m" + "Correct!")
  else:
    print(colorama.Fore.RED + "Incorrect. The correct spelling is", words_dict[selected_number])
