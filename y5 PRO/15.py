def zluc_subory(m1,m2,m3):
    s1 = open(m1)
    s2 = open(m2)
    s3 = open(m3, 'w')
    r1 = s1.readline()
    r2 = s2.readline()

    while r1 != '' or r2 != '':
        if r1 != '':
            print(r1.strip())
            r1 = s1.readline
        if r2 != '':
            print(r1.strip())
            r2 = s2.readline()



zluc_subory("farby",'prvocisla','zlucene')