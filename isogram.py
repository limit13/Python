def is_isogram(string):
    if (type(string)!=str):
        return False
    elif (string==""):
        return True
    else:
        s=string.upper()
        for x in s:
            if x.isalpha():
                if(s.count(x)>1):
                    return False
        return True        
            
            
                
