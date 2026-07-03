import os
def count_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return len(lines)


def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)


def count_characters(filename):
    with open(filename, "r") as file:
        text = file.read()
        return len(text)


def copy_file(source, destination):
    with open(source, "r") as src:
        data = src.read()

    with open(destination, "w") as dest:
        dest.write(data)

    print("\n File copied successfully!")


def search_word(filename, word):
    with open(filename, "r") as file:
        text = file.read().lower()

    if word.lower() in text:
        print(f"\n '{word}' found in the file.")
    else:
        print(f"\n '{word}' not found.")



filename = "sample.txt"

if not os.path.exists(filename):
    print("File does not exist.")
else:
    print("FILE ANALYZER PROGRAM")

    print(f"\nNumber of Lines      : {count_lines(filename)}")
    print(f"Number of Words      : {count_words(filename)}")
    print(f"Number of Characters : {count_characters(filename)}")

    copy_file(filename, "copy_sample.txt")

    word = input("\nEnter word to search: ")
    search_word(filename, word)