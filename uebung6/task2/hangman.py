import words
import random
import hangman


def main() -> None:
    wrds = words.wordlist.get_words(method="url", src="https://codeberg.org/davidak/wortliste/raw/branch/master/wortliste.txt")
    secret = random.choice(wrds)
    # print("Spoiler Alert: {}".format(secret))
    hangman.game.start(secret, 10)


if __name__ == "__main__":
    main()
