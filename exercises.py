import time as t
import math as m
import numpy as np

def quadratic_fun(a,b,c):
    print(f"Looking for solutions of the equation {a}x^2 + {b}x + {c} = 0")
    if a == 0:
        print(f"The root is:{-b/x}")
        return
    d = b**2 - 4*a*c
    roots = []
    if d < 0:
        print("The solutions are not real!")
    else:
        roots = [(-b - d**0.5)/(2*a), (-b + d**0.5)/(2*a)]
        print("The solutions are:")
        for index,root in enumerate(roots):
            print(f"Root {index + 1}: {root}")
    return roots
def recaman(N):
    start = t.process_time()
    an = 0
    solution_list = [0]
    solution_set = set(solution_list)
    for n in range(1,N):
        an = solution_list[-1]
        condition = an - n
        if condition > 0 and condition not in solution_set:
            an = solution_list[-1] - n
        else:
            condition = solution_list[-1] + n
            solution_list.append(condition)
        solution_list.append(condition)
        solution_set.add(condition)
    end = t.process_time()
    print(f"Process t: {end - start} seconds")
    #print(solution_list)
    return solution_list
def reverse(list):
    solution = list[::-1]
    return solution
def intersection(list1,list2):
    lsol = []
    for x in list1 + list2:
        if x in list1 and x in list2:
            if x not in lsol:
                lsol.append(x)
    print(lsol)
    return lsol
def pairs(N):
    factors = []
    for n in range(1,int(N**0.5)+2):
        if N%n == 0:
            factors.append(n)
    result = [(x,int(N/x)) for x in factors if x <= N/x]
    return result
def comparing():
    start = t.process_time()
    list1 = []
    for i in range(0,1000):
        if i%3 == 0:
            list1.append(i)
    print(list1[1:10])
    end = t.process_time()
    print(f"Process t: {end - start} seconds")

    start = t.process_time()
    list2 = [x for x in range(0,1000) if x%3 == 0]
    print(list2[1:10])
    end = t.process_time()
    print(f"Process t: {end - start} seconds")

    start = t.process_time()
    list3 = list(filter(lambda x: x%3 == 0, range(0,1000)))
    print(list3[1:10])
    end = t.process_time()
    print(f"Process t: {end - start} seconds")

    start = t.process_time()
    list4 = list(range(0,999,3))
    print(list4[1:10])
def palindrome(word):
    print("Checking if the string is a palindrome!")
    print(f"Phrase: {word}")
    word = word.upper().replace(" ","")
    for index in range(len(word)):
        if word[index] != word[len(word)-1-index]:
            print("The string is not a palindrome!")
            return False
        else:
            print("The string is a palindrome!")
            return True
def maximum_occurences(string):
    print(f"Phrase is: {string}")
    string = string.replace(" ","")
    characters = set(string)
    string_count = {}
    for letter in characters:
        counter = 1
        for item in string:
            if item == letter:
                counter += 1
        string_count[letter] = counter
    #print(string_count)
    maxval = max(string_count.values())
    #print(maxval)
    for item in string_count:
        if string_count[item] == maxval:
            print(f"Character with max number of occu is '{item}': {maxval}")
    return maxval
def primes(N):
    array = dict(enumerate([True for x in range(2,N+1)],2))
    for i in range(2,int(N**0.5)+1):
        if array[i] == True:
            temp = [i*2 + x*i for x in range(N) if (i*2 + x*i)<=N]
            for j in temp:
                array[j] = False
    solution = [x for x in array if array[x] == True]
    return solution
