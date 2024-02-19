def findBinary(decimal, result):
    if decimal == 0:
        return result
    result = str(decimal % 2) + result
    return findBinary(decimal // 2, result)

print(findBinary(100, ''))  # Output: '1010'
