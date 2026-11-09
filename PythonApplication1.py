from dictionary import (
    load_dictionary,
    add_word,
    delete_word,
    find_word,
    change_translation,
    show_all_words
)


def show_menu():
    print("\n================================")
    print("    ENGLISH-FRENCH DICTIONARY")
    print("================================")
    print("1. Add word")
    print("2. Delete word")
    print("3. Find word")
    print("4. Change translation")
    print("5. Show all words")
    print("0. Exit")
    print("================================")


def main():
    dictionary = load_dictionary()

    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_word(dictionary)

        elif choice == "2":
            delete_word(dictionary)

        elif choice == "3":
            find_word(dictionary)

        elif choice == "4":
            change_translation(dictionary)

        elif choice == "5":
            show_all_words(dictionary)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()

