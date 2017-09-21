def word_count(x):
    from collections import Counter
    for i in x:
        if ((i.isalpha()==False) and (i.isdigit()==False)):
            x=x.replace(i," ")
    x=x.lower()
    return Counter(x.split())
