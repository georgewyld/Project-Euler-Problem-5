"""2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?"""

import sys, time, math

"""Online someone suggested that the same answer is achieved by multiplying
multiplying prime factors from 1-20, so copied and modified code from
prime factors task to get an answer within 0.07 seconds"""


def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else: return False
    return True

def get_prime_factors(num):
    factors1=[]
    factors2=[]
    primes=[]
    for i in range (1,math.ceil(num**0.5+1)):
        if (num%i==0):
            factors1.append(i)
    for i in factors1:
        factors2.append(num/i)
    factors=list(map(int,factors1+factors2))
    factors.sort()
    factors=list(set(factors))
    
    for y in factors:
        if is_prime_number(y):
            primes.append(y)       
    return primes

divisor=[7,11,12, 13, 16, 17, 18, 19, 20]
prime_factors=[]
num=1
start=time.time()
for i in divisor:
    prime_factors.append(get_prime_factors(i))

prime_factors  = [val for sublist in prime_factors for val in sublist]
prime_factors.sort()

for i in prime_factors:
    num*=i
print(num)
elapsed=(time.time()-start)
print(elapsed)
sys.exit()

"""Original way I calculated answer - takes 57 seconds
lots of loops, checks each number to see if divisible until it
gets to a number that all numbers from 1-20 are divisors"""
num=1
start=time.time()
while num%1==0:
    while num%2==0:
        while num%3==0:
            while num%4==0:
                while num%5==0:
                    while num%6==0:
                        while num%7==0:
                            while num%8==0:
                                while num%9==0:
                                    while num%10==0:
                                        while num%11==0:
                                            while num%12==0:
                                                while num%13==0:
                                                    while num%14==0:
                                                        while num%15==0:
                                                            while num%16==0:
                                                                while num%17==0:
                                                                    while num%18==0:
                                                                        while num%19==0:
                                                                            while num%20==0:
                                                                                print(num)
                                                                                elapsed=(time.time()-start)
                                                                                print(elapsed)
                                                                                sys.exit()
                                                                            num+=1
                                                                        num+=1
                                                                    num+=1
                                                                num+=1
                                                            num+=1
                                                        num+=1
                                                    num+=1
                                                num+=1
                                            num+=1
                                        num+=1
                                    num+=1
                                num+=1
                            num+=1
                        num+=1
                    num+=1
                num+=1
            num+=1
        num+=1
    num+=1
    
