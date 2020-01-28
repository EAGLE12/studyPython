def U_to_T(str1s):
    result = ''
    for str1 in str1s:
        if str1 == 'U':
          result = result + 'T'
        else:
            result = result + str1
    return result

print(U_to_T('AUGC'))