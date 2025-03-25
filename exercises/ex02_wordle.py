__author__: str = "730678802"


def contains_char(ci: str, zimu: str) -> bool:
    """Find character in word. If found return True, return Flase otherwise"""
    assert len(zimu) == 1, f"len('{zimu}') is not 1"
    i = 0
    while i < len(ci):
        if zimu == ci[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    "This function emojifies the bool feedback."
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    assert len(guess) == len(secret), "Guess must be same length as secret"
    i = 0
    result = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def input_guess(length: int) -> str:
    user = input(f"Enter a {length} character word: ")
    if len(user) != length:
        print(f"That wasn't {length} chars! Try again: ")
        return input_guess(length)
    else:
        return user


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    max = 6
    now = 1
    correct_length = len(secret)

    while now <= max:
        print(f"=== Turn {now}/6 ===")
        guess = input_guess(correct_length)

        emoji = emojified(guess, secret)
        print(emoji)

        if guess == secret:
            print(f"You won in {now}/6 turns!")
            return

        now += 1
    print("X/6 - Sorry, try again tomorrow!")
