width = 40
with open("lists/subor1.txt","r", encoding="utf8") as sub:
    text = str(sub.read())
    odseky, slova = [],[]  
    while "\n\n" in text:
        odseky.append(text[:text.find("\n\n")])
        text = text[text.find("\n\n")+1:]
    odseky = [x for x in odseky if x != ""]
    for odsek in odseky:
        slova = []
        odsek = odsek.replace("\n"," ")
        odsek += " "
        while " " in odsek:
            if odsek[:odsek.find(" ")] != '':
                slova.append(odsek[:odsek.find(" ")])
            odsek = odsek[odsek.find(" ")+1:]
        slova_copy = slova[:]
        dlzka_slov = 0
        for slovo in slova:
            dlzka_slov += len(slova)
        while slova_copy:
            slova = slova_copy[:]
            if len(slova_copy) == 1:
                print(slova_copy[0])
                slova_copy.pop(0)
                break
            dlzka = 0
            to_print = []
            for slovo in slova:
                if dlzka + len(slovo) + len(to_print) > width:
                    break
                else:
                    dlzka += len(slovo)
                    to_print.append(slovo)
                    slova_copy.pop(0)
            medzery = (width-dlzka)//(len(to_print)-1)
            medzery_zvysok = (width-dlzka)%(len(to_print)-1)
            for slov in to_print:
                if medzery_zvysok:
                    print(slov+" "*medzery+" ",end="")
                    medzery_zvysok -= 1
                else:
                    print(slov+" "*medzery,end="")
            print()
        print()
                