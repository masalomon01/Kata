# 5kyu
def to_camel_case(text):
    text_l = text.replace('-', '_').split('_')
    update_l = [text_l[0], ]
    for word in text_l[1:]:
        update_l.append( word.title() )
    return ''.join(update_l)




print to_camel_case('') # , '', "An empty string was provided but not returned")
print to_camel_case("the_stealth_warrior") # , "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
print to_camel_case("The-Stealth-Warrior") # , "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
print to_camel_case("A-B-C") # , "ABC", "to_camel_case('A-B-C') did not return correct value")