def formword(word, char_count):
    word_count = {}
    for char in word:
        if char not in word_count:
            word_count[char] = 0
        word_count[char] += 1
    
    for char, count in word_count.items():
        if char not in char_count or char_count[char] < count:
            return False
    return True

def probable_words(ref, ch):
    char_count = {}
    for char in ch:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    
    probable_words = []
    for word in ref:
        if formword(word, char_count):
            probable_words.append(word)
    
    return probable_words

ref = input().split(',')
ch = input().split(',')

probable_words = probable_words(ref, ch)

if probable_words:
    print('"' + '","'.join(probable_words) + '"')
else:
    print("No")
