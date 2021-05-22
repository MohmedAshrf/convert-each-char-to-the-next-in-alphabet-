def convert(string): 
    result = ""
    for i in string:
        i=ord(i)
        if (i >= 65 and i <= 90) or (i >= 97 and i <= 122): #indicates alphabet
            i+=1
            char = chr(i)
            if char in ('e', 'i', 'o', 'u'):
                char = char.upper()
            result += char
        else:
            result += chr(i)
    return(result)
    
print(convert(input("Enter a string to be manipulated")))
