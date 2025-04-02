from collections import Counter

def word_count_with_frequency(sentence):
    words = sentence.split()
    word_frequency = Counter(words)
    return len(words), word_frequency

# Test the function
sentence = input("Enter a sentence: ")
word_count, frequency = word_count_with_frequency(sentence)

print(f"\nThe number of words in the sentence is: {word_count}")
print("Word frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
