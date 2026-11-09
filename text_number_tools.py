# text_number_tools.py

def word_count(sentence):
    words = sentence.split()
    return len(words)


def longest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def reverse_sentence(sentence):
    return sentence[::-1]



def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True



def main():
    sentence = input("Enter a sentence: ")
    number = int(input("Enter a number: "))

    print("
--- Text Analysis ---")
    print(f"Word Count: {word_count(sentence)}")
    print(f"Longest Word: {longest_word(sentence)}")
    print(f"Reversed Sentence: {reverse_sentence(sentence)}")

    print("
--- Number Analysis ---")
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


if __name__ == "__main__":
    main()
