word = str(input('Enter a word > ')).upper()
print(f'INPUT: {word}')
word = word[::-1]
char = 'character' if len(word) == 1 else 'characters'
print(f'OUTPUT: {word} ({len(word)} {char})')

for character in range(len(word) - 1, -1, -1):
    print(f'OUTPUT: {character}', end='')