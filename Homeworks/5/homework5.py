import time

# def N_evens(N):
#     return (i for i in range(2,N,2))

# for i in N_evens(10):
#     print(i)



# def reverse_list(ls):
#     for i in ls[::-1]:
#         yield i

# ls = [1,2,3,4,8,9,10,11]
# for i in reverse_list(ls):
#     print(i)




# def endless_fib():
#     first = 0
#     sec = 1
#     while(True):
#         yield first
#         temp = sec
#         sec = sec + first
#         first = temp

# for i in endless_fib():
#     print(i)
#     time.sleep(0.2)




# def even_digit(N):
#     yield from (x for x in range(N) if sum((int(a) for a in str(x)))%2==0)

##learnt yield from used with lists to yield the values 1 by 1

# def even_digit(N):
#     for i in range(N):
#         if(sum((int(a) for a in str(i)))%2==0):
#             yield i


# for i in even_digit(20):
#     print(i)





# def perfect_generator():
#     a = 1
#     while(True):
#         if(sum(x for x in range(1,a) if a%x==0)==a):
#             yield a
#         a+=1

# for i in perfect_generator():
#     print(i)
#     time.sleep(0.2)



# ls = [1,2,3,4,5,6,7,8]
# newls = list(l for l in ls if l%2==0)
# print(newls)



# ls = [1,2,3,4,5,6,7,8]
# newls = list(l*l for l in ls)
# print(newls)


# strls = ["ahhahaha", "bobo", "zigi", "zaga", "amnesia"]
# newstrls = list(i for i in strls if len(i)>5)
# print(newstrls)


# strls = ["ahhahaha", "bobo", "zigi", "zaga", "amnesia"]
# newstrls = list(l.upper() for l in strls)
# print(newstrls)


