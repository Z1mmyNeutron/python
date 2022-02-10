a = []
b = []
c = []
def CartesianSum(set, set1, n, n1,a,b,c):
    for x in range(0,n):
        for y in range(0,n1):
            print("enter values for a, b, and c")
            a = input()
            b = input()
            c = input()
            print(set3[x],set[y])

set3 = [a]
set1 = [b]
set2 = [c]



n = len(set3)
n1 = len(set1)
n2 = len(set2)

CartesianSum(set3,set1,set2,n,n1,n2)