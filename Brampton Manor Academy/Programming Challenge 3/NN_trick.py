number = int(input("Input a number 10-49: "))
player_number = int(input("Enter a number 50-99: "))

def calculation(number, player_number):
    factor = 99 - number
    new_number = player_number + factor
    new_number = new_number - 100 + 1
    guess_number = player_number - new_number
    print(f"I guessed the answer was {number} and the calculation result was {guess_number}")
    return guess_number

if __name__ == '__main__':
    calculation(number, player_number)
