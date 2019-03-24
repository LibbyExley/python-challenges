"""
Write a program that takes a word, removes the vowels and displays the result.
"""

def disemvowel(word):
    vowels = ["A", "E", "I", "O", "U"]
    new_word = word
    for letter in word:
        if letter.upper() in vowels:
            new_word = new_word.replace(letter, "")
    return new_word
            
print(disemvowel('Hello'))