english_to_spanish = {
    'hello': ' hola',
    'goodbye': 'adios',
    'cat': 'gato',
    'dog': 'perro',
    'food': 'comida'
}

def translate_to_spanish(word):
    if word in english_to_spanish:
        return english_to_spanish
    else:
        return 'Translation not found'
    
word_to_translate = input('Enter an English word to translate to Spanish > ')


transalation = translate_to_spanish(word_to_translate.lower())

print(f"The translation of {word_to_translate} is {transalation}")