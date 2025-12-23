# Python Closure Վարժություններ

## 1. make_logger(prefix)

Գրել `make_logger(prefix)` ֆունկցիա, որը վերադարձնում է ֆունկցիա։

Վերադարձվող ֆունկցիան ընդունում է հաղորդագրություն (message) և տպում է այն՝ նախորդված prefix-ով։

**Օրինակ:**
```python
info = make_logger("INFO") 
error = make_logger("ERROR") 
info("Server started")   # INFO: Server started 
error("Connection lost") # ERROR: Connection lost
```

**Հուշում:** prefix-ը պահվում է closure-ում

---

## 2. make_limit_checker(limit)

Գրել `make_limit_checker(limit)` ֆունկցիա։

Վերադարձվող ֆունկցիան ընդունում է թիվ և վերադարձնում է `True`, եթե թիվը չի գերազանցում limit-ը, հակառակ դեպքում `False`։

**Օրինակ:**
```python
check10 = make_limit_checker(10) 
print(check10(5))   # True 
print(check10(10))  # True 
print(check10(15))  # False
```

---

## 3. make_bank_account(balance)

Գրել `make_bank_account(balance)` ֆունկցիա, որը վերադարձնում է 2 ֆունկցիա՝ `deposit(amount)` և `withdraw(amount)`։

- **deposit** → ավելացնում է գումարը
- **withdraw** → հանում է գումարը, եթե հնարավոր է

**Օրինակ:**
```python
deposit, withdraw = make_bank_account(100) 
deposit(50)    # Balance: 150 
withdraw(30)   # Balance: 120 
withdraw(200)  # Not enough money
```

---

## 4. make_once(func)

Գրել `make_once(func)` ֆունկցիա, որը վերադարձնում է նոր ֆունկցիա։

Այդ նոր ֆունկցիան պետք է միայն առաջին անգամ կանչի func-ը, իսկ մնացած անգամները ոչինչ չանի։

**Օրինակ:**
```python
def greet(): 
    print("Hello!") 

greet_once = make_once(greet) 
greet_once()  # Hello! 
greet_once()  # ոչինչ չի տպում 
greet_once()  # ոչինչ չի տպում
```

**Հուշում:** օգտագործիր boolean flag closure-ում

---

## 5. make_fibonacci()

Գրել `make_fibonacci()` ֆունկցիա, որը վերադարձնում է ֆունկցիա։

Յուրաքանչյուր կանչի ժամանակ վերադարձնում է հաջորդ Fibonacci թիվը։

**Օրինակ:**
```python
fib = make_fibonacci() 
print(fib()) # 0 
print(fib()) # 1 
print(fib()) # 1 
print(fib()) # 2 
print(fib()) # 3
```