def lawltext(paragraph):
    words = paragraph.split()
    for index in range(len(words)):
        words[index] = lawl(words[index])
    
    return " ".join(words)

def lawl(word):
    word1 = directreplace(word)
    # nothing changed by directreplace, try replacing special sounds
    if word1 == word:
        return soundreplace(word)
    else:
        return word1
    
# tries to replace lvvv...c, where v denotes a vowel and c the next consonant,
# with 'lawl'
# returns original word if 'l' does not exist
def directreplace(word):
    startindex = word.find("l")
    if startindex == -1:
        return word
    nextindex = findNextConsonant(word,startindex)
    if nextindex == -1:
        nextindex = len(word)
    return word.replace(word[startindex:nextindex],"lawl")
    
# tries to match special sounds to replace
def soundreplace(word):
    sounds = ['ao','ar','aw','awl','ong']
    for sound in sounds:
        if sound in word:
            return word.replace(sound,'lawl')
    return word

# returns index next consonant after startindex
# (not including startindex) in word
# if none, returns -1
def findNextConsonant(word, startindex):
    length = len(word)
    vowels = ['a','e','i','o','u','y']
    isvowel = False
    for index in range(startindex+1, length):
        for vowel in vowels:
            if word[index]==vowel:
                isvowel = True
        if not isvowel:
            return index
        elif isvowel:
            isvowel = False #loop again
    return -1
                

if __name__ == "__main__":
    print lawl('galaucus')
    print lawl('arren')
    print lawltext('jinbao sucks at league of legends')
