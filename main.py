dictionary = {}    
n = int(input())
komandas = []
for i in range (n):
    komanda = input()
    komandas.append(komanda)
for i in range (len(komandas)):
    sadalits = komandas[i].split()
    if sadalits[0] == "add":
        dictionary [sadalits[1]] = sadalits[2]
    elif sadalits[0] == "del":
        if sadalits[1] in dictionary.keys():
            dictionary.pop(sadalits[1])
    elif sadalits[0] == "find":
        if sadalits[1] in dictionary.keys():
            print (dictionary.get(sadalits[1]))
        else:
            print ("not found")
