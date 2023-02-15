def nbrpremier(nbr) :
    if nbr % 2 == 0 :
        print('le nombre est pair')
    elif nbr % 3 == 0 :
        print('le nombre est un multiple de 3')
    elif nbr % 5 == 0 :
        print ('le nombre est un nmultiple de 05')
    else :
        print('le nombre est un nombre Premier')

        

tab=[]
for i in range (1,1000) :
    if nbrpremier(i) :
        tab.append(i)
print(i)