# SLAYER = int(input("Enter your guess for slayer: "))

def program(SLAYER):
    print("""Guess a six-digit number SLAYER so that the following equation is true,
          where each one of the letters stands for the digit in the position shown:
                           SLAYER + SLAYER + SLAYER = LAYERS""")

    digits_slayer = []
    for i in str(SLAYER):
        digits_slayer.append(int(i))

    S_slayer = digits_slayer[0]
    L_slayer = digits_slayer[1]
    A_slayer = digits_slayer[2]
    Y_slayer = digits_slayer[3]
    E_slayer = digits_slayer[4]
    R_slayer = digits_slayer[5]

    LAYERS = int(3 * SLAYER)
    digits_layers = []
    for i in str(LAYERS):
        digits_layers.append(int(i))

    L_layers = digits_layers[0]
    A_layers = digits_layers[1]
    Y_layers = digits_layers[2]
    E_layers = digits_layers[3]
    R_layers = digits_layers[4]
    S_layers = digits_layers[5]

    if S_slayer == S_layers and L_slayer == L_layers and A_slayer == A_layers and Y_slayer == Y_layers and E_slayer == E_layers and R_slayer == R_layers:
        print("Your guess is correct:")
        print(f"SLAYER + SLAYER + SLAYER = {LAYERS}")
        print(f"LAYERS = {LAYERS}")
        print("Thanks for playing.")
        check = "True"
        return check
    else:
        print("Your guess is incorrect")

if __name__ == '__main__':
    program(SLAYER)
