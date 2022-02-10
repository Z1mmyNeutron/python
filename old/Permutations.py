
def check_permutations(str1, str2):
    frequencies = {}
    frequencies2 = {}
    #step one build str1 frequency table
    for i in str1:
        if i in frequencies:
            frequencies[i] = frequencies[i] +1
        else:
            frequencies[i] = 1
    for i in str2:
        if i in frequencies2:
            frequencies2[i] = frequencies2[i] +1
        else:
            frequencies2[i] = 1
    return (frequencies == frequencies2)
    

print(check_permutations("google", "ooggle"))


 
