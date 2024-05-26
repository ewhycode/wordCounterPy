
#install text blob package
from textblob import TextBlob
import re


#count words fn
def count_words(text):
    words = text.split()
    return len(words)




#count characters fn
def count_characters(text):
    return len(text)


#to count numbers
def count_numbers(text):
    numbers = re.findall(r'\d+', text)
    return len(numbers)



#to spell correct using textblob package(needs to be installed first)
def spell_correct(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text



#main including print characters, word count, mumber count, and corrected text detected
def main():
    text = input("Enter the text: ")

    word_count = count_words(text)
    character_count = count_characters(text)
    number_count = count_numbers(text)
    corrected_text = spell_correct(text)

    print(f"Word Count: {word_count}")
    print(f"Character Count: {character_count}")
    print(f"Number Count: {number_count}")
    print(f"Corrected Text: {corrected_text}")


if __name__ == "__main__":
    main()
