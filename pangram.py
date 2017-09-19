def is_pangram(sent):
    ten=sent.lower()
    p="abcdefghijklmnopqrstuvwxyz"
    for x in p:
        if (ten.count(x)==0):
            return False
    return True
        
