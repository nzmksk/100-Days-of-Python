# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013)
# Jaden is also known for some of his philosophy that he delivers via Twitter
# When writing on Twitter, he is known for almost always capitalizing every word
# For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below

# Your task is to convert strings to how they would be written by Jaden Smith
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them

# Example:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"


def jaden_case(string):
    # Split the string to word by word
    word_list = string.split()
    new_list = []
    # Uppercase the first letter for each word and lowercase the remaining letters
    for word in word_list:
        jaden_case = word.capitalize()
        new_list.append(jaden_case)
    # Join the words altogether in a single string
    return ' '.join(new_list)


quote = input("Enter your quote here: ")
print(jaden_case(quote))
