from string import punctuation


def pig_it(text):
    text_l = [word[1:]+word[0]+'ay' if word not in punctuation else word for word in text.split(" ")]
    return " ".join(text_l)


print pig_it('Pig latin is cool') # 'igPay atinlay siay oolcay')
print pig_it('This is my string') # 'hisTay siay ymay tringsay')
print pig_it('Hello world !')     # elloHay orldWay !