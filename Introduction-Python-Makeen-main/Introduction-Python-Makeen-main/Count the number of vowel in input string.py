#Count the number of vowel in input string
def countVowel(string):
    count=0
    
    for i in string:
        if (i in 'aeiou') or (i in 'AEIOU'):
            count=count+1
    return count

string_=input("Enter String:")
s=countVowel(string_)
print(s)