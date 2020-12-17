#Hello Pat, testing
import random
import copy 
#Board positions
Choices =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

#Properties of each cell
class StateCells(object):
    def __init__(self, affiliation, cellnumber, districtnumber, probability, name, used):
        self.affiliation = affiliation
        self.cellnumber = cellnumber
        self.districtnumber = districtnumber
        self.probability = probability
        self.name = name
        self.used = used


def Nextchoice(Array, k):
      #print ("Values inside the function: ", Array)
#      print("This is the randomly chosen INDEX, K: " + str(k))

      #Line below removes the randomly chosen cell number from the grid array
      #Why are we popping an element off the array???
      #Array.pop(k)
      if k == 0:
        A = [1,3]
      if k == 1:
        A = [0,2,4]
      if k == 2:
        A = [1,5]
      if k == 3:
        A = [0,4,6]
      if k == 4:
        A = [1,3,5,7]
      if k == 5:
        A = [2,4,8]
      if k == 6:
        A = [3,7,9]
      if k == 7:
        A = [4,6,8,10]
      if k == 8:
        A = [5,7,11]
      if k == 9:
        A = [6,10,12]
      if k == 10:
        A = [7,9,11,13]
      if k == 11:
        A = [8,10,14]
      if k == 12:
        A = [9,13,15]
      if k == 13:
        A = [10,12,14,16]
      if k == 14:
        A = [11,13,17]
      if k == 15:
        A = [12,16]
      if k == 16:
        A = [17,15,13]
      if k == 17:
        A = [16,14]
      while 0 < len(A):
#        print("This is A, the array of neighbors to K: " + str(A))
        random_num = random.choice(A) 
        A.remove(random_num)
#        print("This is the district number of the array: " + str(Array[random_num].districtnumber))
        #ERROR: "ARRAY" holds only 17 values, up to index 16
        if Array[random_num].districtnumber == 9:
#            print("This is the random number" + str(random_num))    
            return random_num
      else: #This is a While - Else loop. After the While no longer applies the Else does whatever is there to do.
        return 99
      
#####
#MAIN
#####
State_Cells = []
Yes =[]
for i in range(18):
    State_Cells.append(StateCells(random.randint(0,1),i,9,1,9,9))
    # def __init__(self, affiliation, cellnumber, districtnumber, probability, name, used):
#for x in range(18):
#    print("Cell" + str(x) + str(State_Cells[x].districtnumber))









good_maps = []
bigcount = 0
Yikes = 0
Success = 0
for x in range (10):
# Makes a Deep Copy which may be disposed of
# if need be without lasting effects on Original
    bigcount = bigcount +1
    district_number = 0
#    print("")
#    for x in range(18):
#       print("This is a State Cell" + str(x) + str(State_Cells[x].districtnumber))
 
    Temp_State = copy.deepcopy(State_Cells)
    cell_options = copy.deepcopy(Choices.copy())
    
    print("Fresh Start")
#    for x in range(18):
#       print("This is a Temp Cell" + str(x) + str(Temp_State[x].districtnumber))
    #Generate first random number and add cell to district(0)
    #Remove random number from cell_options

 
    for d in range(18):  # This should do it if we already pick one #                    before the for loop begins
      
        district_number = (d//3)
#        print(district_number)
#        print("This is d, the loop we are on: " + str(d))
#        print("This is the current district number we are trying to fill: " +str(district_number))
    
    
        if (d % 3 == 0 ):
#            print("First")
#            print("neighbor")
            randomnum = random.choice(cell_options)
            neighbor = randomnum
            print("","")
            print("neighbor #1 ", neighbor)
            cell_options.remove(randomnum)
            Temp_State[randomnum].districtnumber=(district_number)                    
            
        
        else:
            chosen_neighbor = Nextchoice(Temp_State,neighbor)
            if chosen_neighbor == 99:
                print("YIKES, We Hit 99")
                Yikes = Yikes +1
                break 
            else:
                print("2nd or 3rd neighbor ", chosen_neighbor)
                cell_options.remove(chosen_neighbor)
                Temp_State[chosen_neighbor].districtnumber=(district_number)
                neighbor = chosen_neighbor
        if d == 17:
#            print("We Made it")
            Yes.append(Temp_State)
            print("This is the map")
            for r in range(6):
                print("")
                count = r*3
                for c in range(3):
                    print("Cell #:", Temp_State[count].cellnumber, "\t", end ="")
                    count = count + 1
                print("")
                count = r*3
                for c in range(3):
                    print("Vote:  ", Temp_State[((r * 3) + c )].affiliation, end ="\t")
                print("")
                for c in range(3):
                    print("District:",Temp_State[((r * 3) + c )].districtnumber, end="\t")
                print("")
                print("")
            Success = Success + 1  
  
# Printing STATE
print("-----------------STATE---------------------")

print("Success =" , Success)
print("Yikes =", Yikes)
print(bigcount)

#if Success >= 1:
#    print(Yes[0])











   
