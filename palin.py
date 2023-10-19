#Palindrome reads same way left or right 
# BIB, nun, madam are some examples
# My thoughts are to create a loop to 

#droming = ['bib', 'fif', 'pup']
#print(droming)# using as a print test

#def isPalindrome(n):
 
   #str(n) ==str(n)[::1]
'''  pwords = list(n)
   isPalindrome = True

   for pword in pwords:
      if pword == pwords[-1]:
         pword.pop(-1)
      else:
         isPalindrome = False
         break
   
   return isPalindrome

print(isPalindrome(droming))'''

word = "pip"
is_palindrome = word.find(word[::-1])
print(is_palindrome)
    