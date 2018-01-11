# Kata 6kyu
def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def namelist(names):
    s, namesl = "", []
    namesl = [each.get('name') for each in names]
    s = ', '.join(namesl) 
    return rreplace(s, ',', ' &', 1)



print namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]) #, 'Bart, Lisa, Maggie, Homer & Marge', "Must work with many names")
print namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]) #, 'Bart, Lisa & Maggie', "Must work with many names")
print namelist([{'name': 'Bart'},{'name': 'Lisa'}]) #, 'Bart & Lisa', "Must work with two names")
print namelist([{'name': 'Bart'}]) #, 'Bart', "Wrong output for a single name")
print namelist([]) #, '', "Must work with no names")