# def nbrpremier(nbr) :
 #      if nbr % 2 == 0 :
  #          print('le nombre est pair')
   #     elif nbr % 3 == 0 :
   #         print('le nombre est un multiple de 3')
    #    elif nbr % 5 == 0 :
    #        print ('le nombre est un nmultiple de 05')
     #   else :
     #       print('le nombre est un nombre Premier')

            

    #tab=[]
    #for i in range (1,1000) :
   #     if nbrpremier(i) :
   #         tab.append(i)
   # print(i)

#def facto(a) :
   # if a < 0 or a > 15 :
      #  return -1
    #else :
      #  fact = 1
        #cal = 1
       # while cal < a :
         #   fact = fact * (cal+1)
          #  cal = cal + 1
        #return fact
    
#print(facto(10))

class Tableau: 
  items = []
  def __init__(self, *args):
      for item in args:
          self.items.append(item)

  def at(self, index) :
      if index > len(self.items):
        return None
      return self.items[index]
  
  def conc(self , tab : list) :
     return
  
number = Tableau(1, 2, 3, 4, 5, 6)

print(number.at(10))

        
        
    

