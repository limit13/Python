def to_rna(x):
    for a in x:
        if(a!="G" and a!="C" and a!="T" and a!="A"):
            return ""
    na = {"G":"C","C":"G","T":"A","A":"U"}
    dna = ""
    for i in x:
        dna=dna+na[i]
    return dna
