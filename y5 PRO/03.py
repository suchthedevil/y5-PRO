def riadky_s_textom(meno_suboru, text):
    with open(meno_suboru,'r') as subor:
        for riadok in subor:
            if text in riadok:
                print(riadok)

riadky_s_textom('02.py','for')
