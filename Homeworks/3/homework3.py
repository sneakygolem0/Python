# NOTE: I will not read your hints for better understanding

def sum_digits(n):
    if(n<10):
        return n
    return n%10+sum_digits(n//10)

print(sum_digits(12091))


def filter_even(ls):
    if(ls==[]):
        return []
    if(ls[0]%2==0):
        return [ls[0]]+filter_even(ls[1:])
    return filter_even(ls[1:])
# Էս մեկը կարդացի, չէր ստացվում
print(filter_even([1, 4, 3, 6, 9, 2]))

def count_char(s, char):
    if(s==""):
        return 0
    if(s[0]==char):
        return 1+count_char(s[1:], char)
    return count_char(s[1:], char)

print(count_char("ahahhahahaha", "a"))

def is_palindrome(s):
    if(s==""):
        return True
    if(s[0]==s[-1]):
        return is_palindrome(s[2:-2])
    return False

print(is_palindrome("ahahahaha"))

def power(base, exponent):
    if(exponent==1):
        return base
    return base*(power(base,exponent-1))

print(power(2,4))

#