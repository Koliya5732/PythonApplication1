import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "dictionary.json"


def load_dictionary():
    if not FILE_PATH.exists():
        return {}

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Error loading dictionary!")
        return {}


def save_dictionary(dictionary):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)


def find_key(dictionary, word):
    for key in dictionary:
        if key.lower() == word.lower():
            return key

    return None


def add_word(dictionary):
    english = input("Enter English word: ").strip()
    french = input("Enter French translation: ").strip()

    if not english or not french:
        print("Words cannot be empty!")
        return

    if find_key(dictionary, english):
        print("This word already exists!")
        return

    dictionary[english] = french
    save_dictionary(dictionary)

    print("Word successfully added!")


def delete_word(dictionary):
    english = input("Enter English word to delete: ").strip()

    key = find_key(dictionary, english)

    if key is None:
        print("Word not found!")
        return

    del dictionary[key]
    save_dictionary(dictionary)

    print("Word successfully deleted!")


def find_word(dictionary):
    english = input("Enter English word to find: ").strip()

    key = find_key(dictionary, english)

    if key is None:
        print("Word not found!")
        return

    print(f"English: {key}")
    print(f"French: {dictionary[key]}")


def change_translation(dictionary):
    english = input("Enter English word: ").strip()

    key = find_key(dictionary, english)

    if key is None:
        print("Word not found!")
        return

    print(f"Current translation: {dictionary[key]}")

    new_translation = input("Enter new French translation: ").strip()

    if not new_translation:
        print("Translation cannot be empty!")
        return

    dictionary[key] = new_translation
    save_dictionary(dictionary)

    print("Translation successfully changed!")


def show_all_words(dictionary):
    if not dictionary:
        print("Dictionary is empty!")
        return

    print("\n========== DICTIONARY ==========")

    for english, french in sorted(dictionary.items()):
        print(f"{english:<20} - {french}")

    print("================================")
