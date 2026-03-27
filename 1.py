def count_vowels_consonants(sentence):
    '''Counts the number of vowels and consonants in a sentence'''
    vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
    consonants = set('бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ')

    vowel_count = 0
    consonant_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    print(f"Гласных: {vowel_count}")
    print(f"Согласных: {consonant_count}")


sentence = input("Предложение:")
count_vowels_consonants(sentence)
