# 6kyu

def to_weird_case_(string):
	new_string = ''
	string = string.lower()
	for each in string:
		index = string.index(each)
		print(each, index)
		if index % 2 == 0:
			new_string+=each.upper()
		else:
			new_string+=each
		string = string.replace(each, "%", 1)
	return new_string


def to_weird_case(string):
    ans = []
    string = string.split()
    for j in string:
        i = 0
        temp = ''
        while i < len(j):
            if i % 2 == 0:
                temp += j[i].upper()
            else:
                temp += j[i].lower()
            i += 1
        ans.append(temp)
    return ' '.join(ans)


# test.it('should return the correct value for a single word')
print(to_weird_case('This')) #, 'ThIs')
print(to_weird_case('is')) #, 'Is') 
print(to_weird_case('test')) #, 'TeSt') 

# test.it('should return the correct value for multiple words')
print(to_weird_case('This is a test')) #, 'ThIs Is A TeSt')

t 0
e 1
s 2
t 3
TeSt
t 0
h 1
i 2
s 3
  4
i 5