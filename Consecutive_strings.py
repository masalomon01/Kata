
def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''
    longest = index = 0
    for i in range(n - k + 1):
        length = sum([len(s) for s in strarr[i: i + k]])
        if length > longest:
            longest = length
            index = i
    return ''.join(strarr[index: index + k])




print longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) #, "abigailtheta")
print longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) #, "oocccffuucccjjjkkkjyyyeehh")
print longest_consec([], 3) # , "")
print longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) # , "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
print longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2) #, "wlwsasphmxxowiaxujylentrklctozmymu")
print longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) #, "")
print longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3) #, "ixoyx3452zzzzzzzzzzzz")
print longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15) #, "")
print longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0) #, "")
