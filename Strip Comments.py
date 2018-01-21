# 4kyu

def solution(string, markers):
    lines = string.split('\n')
    for i, line in enumerate(lines):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        lines[i] = line.rstrip(' ')
    return '\n'.join(lines)


print solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) #, "apples, pears\ngrapes\nbananas")
print solution("a #b\nc\nd $e f g", ["#", "$"]) #, "a\nc\nd")