# 5kyu
def valid_parentheses(string):
    l = []
    for elem in string:
        if elem == '(':
            l.append(elem)
        elif elem == ')' and len(l)>0:
            l.pop()
        elif elem == ')':
            return False
    if(len(l) == 0):
        return True
    else:
        return False



print valid_parentheses("  (") # False)
print valid_parentheses(")test") # False)
print valid_parentheses("") # True)
print valid_parentheses("hi())(") # False)
print valid_parentheses("hi(hi)()") # True)
print valid_parentheses("()" ) # true)
print valid_parentheses(")(()))") # false)
print valid_parentheses("("     ) # False)
print valid_parentheses("(())((()())())") # True)
