# Create a function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(text):
    # Split the string into words using a single whitespace
    words_list = text.split(" ")
    reverse_words = [i[::-1] for i in words_list]
    # Join the words together after reversing it
    return ' '.join(reverse_words)
