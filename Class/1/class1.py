def isPrime(x):
    for i in range(2, int(x/2)+1):
        if(x%i==0):
            return 0
    return 1

numbers=[5,12,18,7,25,4,30,9,101]
print(list(filter(lambda x: x>10, numbers)))
print(list(filter(lambda x: x%3==0, numbers)))
print(list(filter(lambda x: x>100, numbers)))
print(list(filter(lambda x: x>=10 and x<100 and x%2==0, numbers)))
print(list(filter(lambda x: x>100, numbers)))
print("prime. ",list(filter(isPrime, numbers)))
print("prime 3 digit. ",list(filter(isPrime, list(filter(lambda x: x>=100 and x<1000, numbers)))))



names=["James", "Abulik" , "table ", "Helloooo!!!", "Rob", "How are you??"]
print(list(filter(lambda x: x[0] in "Aa", names)))
print(list(filter(lambda x: "?" in x or "!" in x, names)))
print(list(filter(lambda x: len(x)%2==0, names)))
print(list(filter(lambda x: len(x)>5, names)))
print(list(filter(lambda x: x[-1]==" ", names)))


actual = [1,2,3,4,5]
expected = [1,1,3,0,5]
print(list(filter(lambda x: x[0]==x[1], zip(actual, expected))))


students = ["Anna", "Mark", "Diana", "John"]
scores = [48, 95, 72, 30]
print(list(filter(lambda x: x[1]>=60, zip(students, scores))))


ls=[1,2,3,4,5,7]
ls1=[0] + ls[:]
for i in list(zip(ls, ls1)):
    print(i[0]-i[1])

print(list(zip(ls, ls1)))