#frekvencne tabulky sa vyuzivaju na komprimaciu dat

def dvojice(meno_suboru):
    with open(meno_suboru,"r") as f:
        text = f.read()
        slov = {}
        while len(text):
            dvojica = text[:2]
            slov[dvojica] = slov.get(dvojica,0) + 1
            text = text[1:]
        new = dict(sorted(slov.items(),key= lambda x : x[1],reverse= True)[:10])
        for key,value in new.items():
            print(f"{repr(key)}= {value}x")




dvojice("dictionaries/dobs.txt")