def make_logger(prefix):
    def inner(message):
        print(f"{prefix}: {message}")
    return inner

info = make_logger("INFO")
info("ACCESS GRANTED")


def make_limit_checker(limit):
    def inner(num):
        if(num <= limit):
            return True
        return False
    return inner

check100 = make_limit_checker(100)
print(check100(100))
print(check100(10))
print(check100(101))



def make_bank_account(balance):
    def deposit(depo):
        nonlocal balance
        balance+=depo
        print(f"BALANCE: {balance}")

    def withdraw(witho):
        nonlocal balance
        if(balance<witho):
            print("Amaaan poxery prcav")
            return
        balance-=witho
        print(f"BALANCE: {balance}")

    return deposit, withdraw

deposit, withdraw = make_bank_account(100)

deposit(50)
withdraw(30)
withdraw(200)



def halo():
    print("halo")

def make_once(func):
    done = False
    def inner():
        nonlocal done
        if(done):
            return
        func()
        done = True
    return inner

halo_once = make_once(halo)

halo_once()
halo_once()
halo_once()





def fibonacci():
    one = 0
    dos = 1
    def inner():
        nonlocal one
        nonlocal dos
        temp = one
        one, dos = dos, one + dos
        return temp
    return inner


fib = fibonacci()

print(fib())
print(fib())
print(fib())
print(fib())
print(fib())
