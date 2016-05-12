list_of_primes = []
def  list_all_primes_below(limit):
    number = 2
    while number <= limit:
            is_prime(number)
            number += 1
    return list_of_primes

def  list_first_X_primes(X):
    number = 2
    while len(list_of_primes) < X:
            is_prime(number)
            number += 1
    return list_of_primes
def is_prime(number):
    for prime in list_of_primes:
        if number % prime == 0:
            #not prime
            return False
    store_prime(number)
    return True
def store_prime(prime):
    list_of_primes.append(prime)
def summation_of_list(list):
    sum = 0
    for number in list:
        sum += number
    return sum

if __name__ == "__main__":
    print summation_of_list(list_all_primes_below(2000000))
