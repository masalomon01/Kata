# 4kyu

def validBraces(string):
    pairs, check = {"{":"}", "[":"]", "(":")", "}":"{", "]":"[", ")":"("}, []
    for i in string:
        if i in ["(","[","{"]:
            check.append(i)
        else:
            if len(check) == 0:
                return False
            elif pairs[i] == check[len(check)-1]:
                check.remove(pairs[i])
            else:
                return False
    if len(check) != 0:
        return False
    return True


print validBraces( "()" ) #, True);
print validBraces( "[(])" ) #, False);
print validBraces( "(){}[]" ) #, True);
print validBraces( "([{}])" ) #, True);
print validBraces( "(}" ) #, False);
print validBraces( "[(])" ) #, False);
print validBraces( "[({})](]" ) #, False);
