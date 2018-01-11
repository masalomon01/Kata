
def duplicate_encode(word):
    dict, word, newword = {}, word.lower(), ""
    for letter in word:
        cnt =  word.count(letter)
        dict[letter] = cnt
    for letter in word:
        if dict.get(letter) == 1:
            newword+='('
        else:
            newword+=')'
    return newword

print duplicate_encode("din") # "(((")
print duplicate_encode("recede") # "()()()")
print duplicate_encode("Success") # ")())())","should ignore case")
print duplicate_encode("(( @") # "))((")