# Create a function that counts the vowels in a given input text

def vowel_count(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lowercase_text = text.lower()
    vowel_count = 0
    for i in lowercase_text:
        if i in vowels:
            vowel_count += 1
    return f'Vowel count: {vowel_count}'


text = input("Insert your text here: ")
print(vowel_count(text))
