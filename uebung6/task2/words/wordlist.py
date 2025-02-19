# words/wordlist.py
import random
import urllib.request


def get_words(method = 'url', src: str = "https://raw.githubusercontent.com/taikuukaits/SimpleWordlists/refs/heads"
                                       "/master/Wordlist-Nouns-All.txt") -> list[str]:
    """
    Retrieves a list of words based on the specified method.

    Args:
        method (str): Source method to use ('simple', 'file', or 'url')
        src (str): Source location (file path or URL)

    Returns:
        list[str]: List of words

    Raises:
        ValueError: If an unknown method is specified
    """
    if method == 'simple':
        return _get_simple_word_list()

    elif method == 'file':
        return _load_from_file(src)

    elif method == 'url':
        return _fetch_from_url(src)

    else:
        raise ValueError("Unknown method.")


def _get_simple_word_list() -> list[str]:
    """
    Returns a hardcoded list of basic German words.

    Returns:
        list[str]: List of simple German words
    """
    return [
        'haus', 'baum', 'auto', 'katze',
        'hund', 'fisch', 'vogel', 'pferd',
        'schule', 'arzt', 'apotheke', 'hotel'
    ]


def _load_from_file(filename: str) -> list[str]:
    """
    Loads a list of words from a local file.

    Args:
        filename (str): Path to the word list file

    Returns:
        list[str]: List of words from the file

    Notes:
        - File must be encoded in UTF-8
        - Each word should be on a separate line
        - Returns empty list if file not found
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip().lower() for line in f]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


def _fetch_from_url(url: str) -> list[str]:
    """
    Downloads and parses a list of words from a remote URL.

    Args:
        url (str): URL containing the word list

    Returns:
        list[str]: List of words from the URL

    Notes:
        - URL should contain one word per line
        - Returns empty list on download failure
    """
    try:
        with urllib.request.urlopen(url) as response:
            return [line.decode('utf-8').strip().lower()
                    for line in response.readlines()]
    except Exception as e:
        print(f"Fehler beim Download: {e}")
        return []