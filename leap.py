def is_leap_year(x):
    if(x%4==0):
        if(x%100!=0):
            return True
        elif(x%400==0):
            return True
    if(x%400==0):
        return True
    else:
        return False

 
    
        
