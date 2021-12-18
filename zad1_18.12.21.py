#%%
# Napisz funkcje, ktora stwierdzi czy slowo (string)jest palindromem. Jezeli tak to funcja ma zwrocic true.

# function to check string is
# palindrome or not
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = input("Podaj slowo")
ans = isPalindrome(s)
 
if (ans):
    print("True")
else:
    print("False")

#%%
# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input("Podaj slowo")
print(s[::-1])
ans = isPalindrome(s)
 
if ans:
    print("True")
else:
    print("False")
#%%

# function to check string is
# palindrome or not
def isPalindrome(s):
     
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False
 
# main function
s = input("Podaj slowo")
print(isPalindrome(s))
 
#%%

def isPalindrome(s):
       
    #to change it the string is similar case
    s = s.lower()
    # length of s
    x= len(s)
     
    # if length is less than 2
    if x < 2:
        return True
 
    # If s[0] and s[x-1] are equal
    elif s[0] == s[x - 1]:
        print(s)
        
        # Call is pallindrome form substring(1,x-1)
        return isPalindrome(s[1: x - 1])
 
    else:
        return False
 
# Driver Code
s = input("Podaj slowo")
print(isPalindrome(s))

#%%

