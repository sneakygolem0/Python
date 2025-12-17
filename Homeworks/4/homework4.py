def sumo(ls):
    if(ls==[]):
        return 0
    return ls[0]+sumo(ls[1:])

print(sumo([1,2,3]))


ls=[1,2,6,9,14,50]
def bin(target, ls, start=0, end=None):
    if(not end):
        end=len(ls)
    if(end-start<=1):
        return -1
    mid=(start+end)//2
    if(ls[mid]==target):
        return mid
    if(ls[mid]>target):
        return bin(target, ls, start, mid)
    return bin(target, ls, mid+1, end)

print(bin(9, ls))



def Hasik(ls):
    if(len(ls)==1):
        print(ls)
        return
    newls=[]
    for i in range(len(ls)-1):
        newls.append(ls[i]+ls[i+1])
    Hasik(newls)
    print(ls)

Hasik([1,2,3,4,5])