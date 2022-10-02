# Create a function that counts all the letters in a given input text

def letter_counter(text):
    # Create a list ranging from a-z
    letters = list(map(chr, range(ord('a'), (ord('z') + 1))))
    lowercase_text = text.lower()
    count = 0
    for alphabet in lowercase_text:
        if alphabet in letters:
            count += 1
    return f'Letter count: {count}'


# Lowercase all letters
text = input("Insert your text here: ")
print(letter_counter(text))
