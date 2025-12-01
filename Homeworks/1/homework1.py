def enrollment_stats(ls):
    wage=[]
    stu=[]
    for i in ls:
        stu.append(i[1])
        wage.append(i[2])
    return stu, wage

def mean(ls):
    return sum(ls)/len(ls)

def median(ls):
    if(len(ls)%2==0):
        return (ls[len(ls)/2]+ls[(len(ls)/2)-1])/2
    else:
        return ls[int(len(ls)/2)]

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]



print(f"""******************************
Total students: {sum(enrollment_stats(universities)[0])}
Total tuition: $ {sum(enrollment_stats(universities)[1])}
Student mean: {mean(enrollment_stats(universities)[0])}
Student median: {median(enrollment_stats(universities)[0])}
Tuition mean: $ {mean(enrollment_stats(universities)[1])}
Tuition median: $ {median(enrollment_stats(universities)[1])}
******************************""")

