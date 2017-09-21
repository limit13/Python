def hey(string):
    x=""
    string=string.strip()
    for i in string:
        if i.isalpha()==False and i.isdigit()==False and i not in ("?"):
            x=string.replace(i," ")
    y=""
    for i in x:
        if i.isalpha()==True:
            y=y+i
    if y.isupper()==True:
        return "Whoa, chill out!"
    elif x.endswith("?")==True:
        return "Sure."
    elif x=="":
        if string.isupper()==True:
            return "Whoa, chill out!"
        elif string.endswith("?")==True:
            return "Sure."
        else:
            return "Fine. Be that way!"
    else:
        return "Whatever."
