def cycliccoding(code, n):
    output = ''
    print('code: ' + code)
    cutoff = code[0:n]
    rightshift = code[n:]
    output += rightshift + cutoff
    print('encrypt: ' + output)
    cycliccoding_decrypt(output, n)

def cycliccoding_decrypt(code, n):
    output = ''
    cutoff = code[-n:]
    reverseshift = code[0:-n]
    output += cutoff + reverseshift
    print('decrypt: ' + output)
    
cycliccoding('space wars', 3)
