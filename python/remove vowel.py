def remove_vowel(s):
    new_str=" "
    for i in s:
        if i in "aeiouAEIOU" :
            pass
        else:
            new_str+=1
    print("The strint without vowel is ",new_str)
    
str=input("Enter the string")
remove_vowel(str)