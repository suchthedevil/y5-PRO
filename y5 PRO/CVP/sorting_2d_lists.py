list = [["asd", 2.0], ["b", 3.5], ["ca",1.47], ["dasa",1.9]]
#sort according to length of the first element in the lists inside the outer list
list.sort(key= lambda x: len(x[0]))
print(list)
