#Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to Count all the Prime Numbers and create a new Python List which will contain all the Prime Numbers in it?
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

#DUmmy list to store the prime numbers
prime_numbers = []

#Loop to find prime number in the list by finding its remainder, if it is 1 then its a prime humber
for n in numbers:
    if n > 1:
        isprime = True
        for i in range(2, n):
            if n % i == 0:
                isprime = False
                break
        if isprime:
            prime_numbers.append(n)

print("Prime Numbers:", prime_numbers)
print("Count of Prime Numbers:", len(prime_numbers))