#implement an algorith to return a string, returns true if 
#has all unique characters, else false
def check_string(str2):
    count = 0
    x = True
    for i in range(len(str2) -1):
        for j in range(i+1, len(str2)):
            count = count + 1
            if str2[i] == str2[j]:
                x = False
    print(count)
    return x

def check_other(str2):
    frequencies = {}
    for i in str2:
        if i in frequencies:
            return False
        else: 
            frequencies[i] = ""
    return True

    
    
print(check_other("todayo"))

    

#start at 0
#for loop to check 0-len
#if repeating, stop.