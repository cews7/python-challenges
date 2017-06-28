#find all palindromes less than n
import pdb


def numdigs(x):
    numdigstring= str(x)
    count = 0
    for char in numdigstring:
        count = count+1
    return count

#digcount=numdigs(n)


def pali_n(n):
    palindromes=[]
    for i in range(n):
        string = str(i)
        palindrome = True
        for j in range(len(string)):
            if(string[j]!=string[-(j+1)]):
                palindrome = False
        if(palindrome):
            palindromes.append(i)

    return palindromes

def palindrome(n):
