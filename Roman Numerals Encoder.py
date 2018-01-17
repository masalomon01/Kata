# 4kyu

roman_dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

def solution(n):
    roman = ''
    while n > 0:
        for dec, r in sorted(roman_dict.iteritems(), reverse=True):
            while n >= dec:
                roman += r
                n -= dec
    return roman
    

print solution(1) #,'I', "solution(1),'I'")
print solution(4) #,'IV', "solution(4),'IV'")
print solution(6) #,'VI', "solution(6),'VI'")
print solution(8) #,'VIII', "solution(6),'VIII'")
print solution(9) #,'IX', "solution(6),'IX'")
print solution(14) #,'XIV', "solution(23),'XIV'")
print solution(23) #,'XXIII', "solution(23),'XXIII'")
print solution(90) #,'XC', "solution(23),'XC'")
print solution(1990) #,'MCMXC', "solution(23),'MCMXC'")
print solution(1666) #,'MDCLXVI', "solution(23),'MDCLXVI'")
print solution(2008) #,'MMVIII', "solution(23),'MMVIII'")