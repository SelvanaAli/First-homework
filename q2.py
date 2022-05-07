decnum = int(input('enter a decimal number'))
i = 0
listsec=[]
while decnum != 0 :
    i = decnum%2
    decnum = decnum//2
    listsec = [i]+ listsec
for x in range(0,len(listsec)):
    print(listsec[x],end='')
