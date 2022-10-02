# Create a function that counts all words in a given input text

def word_counter(text):
    return f'Word count: {len(text.split())}'


text = input("Insert your text here: ")
print(word_counter(text))

# This function is not 100% accurate as string of numbers and symbols are still counted as words.
# Will revisit this in the future when a better solution is found.