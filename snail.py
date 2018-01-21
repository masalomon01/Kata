# 4kyu

def snail(array):
    n_array, expected = array, []

    while len(n_array) >= 1:
        [expected.append(e) for e in n_array[0]]
        n_array.pop(0)
        try:
            for i in n_array:
                expected.append(i[-1])
                i.pop()
            rev = n_array[-1][::-1]
            [expected.append(e) for e in rev]
            n_array.pop()
            for i in reversed(n_array):
                expected.append(i[0])
                i.pop(0)
        except:
            break

    return expected
    


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print snail(array) #, expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print snail(array) #, expected)

array = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]
expected = [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8]
print snail(array) #, expected)
