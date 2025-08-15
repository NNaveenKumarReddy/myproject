def reverse(str):
    new_str=' '
    i=len(str)-1
    while i>=0:
        new_str+=str[i]
        i=i-1
    return new_str
    
str=input("\n Enter a string")
print("\n THe reversed string is:",reverse(str))