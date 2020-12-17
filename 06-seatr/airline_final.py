# Angelo Comeaux, Tsee Lee, and Jonathan Swotinsky
# Ethics and Computer Science
# Airline Seating Algorithm 
# Software Solution in Progress - Updated Documentation

# Next Steps:
# Figure out dynamic assignment

# Generate a dictionary to serve as a manifest of all passengers on the aircraft with each seat as a key, and the initial value for each key set to "Unsold":
manifest = {"1A":"Unsold","1B":"Unsold","1C":"Unsold","1D":"Unsold","1E":"Unsold","1F":"Unsold","2A":"Unsold","2B":"Unsold","2C":"Unsold","2D":"Unsold","2E":"Unsold","2F":"Unsold","3A":"Unsold","3B":"Unsold","3C":"Unsold","3D":"Unsold","3E":"Unsold","3F":"Unsold","4A":"Unsold","4B":"Unsold","4C":"Unsold","4D":"Unsold","4E":"Unsold","4F":"Unsold","5A":"Unsold","5B":"Unsold","5C":"Unsold","5D":"Unsold","5E":"Unsold","5F":"Unsold","6A":"Unsold","6B":"Unsold","6C":"Unsold","6D":"Unsold","6E":"Unsold","6F":"Unsold","7A":"Unsold","7B":"Unsold","7C":"Unsold","7D":"Unsold","7E":"Unsold","7F":"Unsold","8A":"Unsold","8B":"Unsold","8C":"Unsold","8D":"Unsold","8E":"Unsold","8F":"Unsold","9A":"Unsold","9B":"Unsold","9C":"Unsold","9D":"Unsold","9E":"Unsold","9F":"Unsold","10A":"Unsold","10B":"Unsold","10C":"Unsold","10D":"Unsold","10E":"Unsold","10F":"Unsold",}

# Print the current state of the manifest:
def displayManifest():
  print("1A\t",manifest["1A"])
  print("1B\t",manifest["1B"])
  print("1C\t",manifest["1C"])
  print("1D\t",manifest["1D"])
  print("1E\t",manifest["1E"])
  print("1F\t",manifest["1F"])
  print("2A\t",manifest["2A"])
  print("2B\t",manifest["2B"])
  print("2C\t",manifest["2C"])
  print("2D\t",manifest["2D"])
  print("2E\t",manifest["2E"])
  print("2F\t",manifest["2F"])
  print("3A\t",manifest["3A"])
  print("3B\t",manifest["3B"])
  print("3C\t",manifest["3C"])
  print("3D\t",manifest["3D"])
  print("3E\t",manifest["3E"])
  print("3F\t",manifest["3F"])
  print("4A\t",manifest["4A"])
  print("4B\t",manifest["4B"])
  print("4C\t",manifest["4C"])
  print("4D\t",manifest["4D"])
  print("4E\t",manifest["4E"])
  print("4F\t",manifest["4F"])
  print("5A\t",manifest["5A"])
  print("5B\t",manifest["5B"])
  print("5C\t",manifest["5C"])
  print("5D\t",manifest["5D"])
  print("5E\t",manifest["5E"])
  print("5F\t",manifest["5F"])
  print("6A\t",manifest["6A"])
  print("6B\t",manifest["6B"])
  print("6C\t",manifest["6C"])
  print("6D\t",manifest["6D"])
  print("7E\t",manifest["7E"])
  print("7F\t",manifest["7F"])
  print("8A\t",manifest["8A"])
  print("8B\t",manifest["8B"])
  print("8C\t",manifest["8C"])
  print("8D\t",manifest["8D"])
  print("8E\t",manifest["8E"])
  print("8F\t",manifest["8F"])
  print("9A\t",manifest["9A"])
  print("9B\t",manifest["9B"])
  print("9C\t",manifest["9C"])
  print("9D\t",manifest["9D"])
  print("9E\t",manifest["9E"])
  print("9F\t",manifest["9F"])
  print("10A\t",manifest["10A"])
  print("10B\t",manifest["10B"])
  print("10C\t",manifest["10C"])
  print("10D\t",manifest["10D"])
  print("10E\t",manifest["10E"])
  print("10F\t",manifest["10F"])

numTix = 0 # Set the initial value of numTix to 0.

# Display a seating chart of the plane (Available seats marked with their seat letter, seats sold to regular customers marked "R", sets sold to economy customers marked "Y")
def displaySeats():
  for i in range(1,len(plane)):
    print(i,"\t",plane[i])


# Determine whether or not a given seat is taken.  If it is taken, return True.  Otherwise, return false.
def seatTaken(row, seat):
  rowDict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5}
  seat = rowDict[seat]
  if plane[row][seat]=="R" or plane[row][seat]=="Y":
    return True
  else:
    return False


#Assign one seat to a regular customer and add the passenger's name to the manifest:
def sellSeatRegular(row,seat):
  rowDict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5}
  rowSeat = str(row)+seat.capitalize()
  seat = rowDict[seat]
  plane[row][seat]="R"
  manifest[rowSeat] = input("Please Enter your name: ")
  print("Thank You,", manifest[rowSeat],"You are seated in", rowSeat)

#Sell seats to a full party of regular customers.
def askRegular():
  displaySeats()
  numTixRegular = input("How many seats would you like to purchase (num)? ")
  if not numTixRegular.isnumeric():
    return 5
  else:
    numTixRegular = int(numTixRegular)
    
  for i in range(numTixRegular):
    taken = True
    while (taken):
      row = input("select a row (num): ")
      if not row.isnumeric():
        return 5
      else:
        row = int(row)

      seat = input("select a seat (letter): ")

      taken = seatTaken(row,seat)
      if (taken):
        print("Sorry, seat's taken")

    sellSeatRegular(row, seat)
    print("Congrats!")
    displaySeats()
  
#Sell seats to a full party of economy customers.
def askEconomy():
  numTix = input("How many (num)? ")
  if not numTix.isnumeric():
    return 5
  else:
    numTix = int(numTix)

  allocateSeats(numTix)

  displaySeats() 


# Assign seats to a party of economy customers.
def allocateSeats(numTix):
  # Search for consecutive <numTix> seats
  possibleGroup = True
  i = 10
  k = 0
  sold = False
  while i>0 and not sold:
    while k<6 and not sold:
      if freeSeatsAt(i,k) >= numTix:
        sellSeatEconomy(i,k,numTix)
        sold = True
      k += 1
    i -= 1
    k = 0

# Assign one seat to a single economy customer:
def sellSeatEconomy(row,seat,numTix):
  for i in range(numTix):
    plane[row][seat+i]="Y"
    print("You are seated in row ", row, "seat", seat+i)

# Check to determine whether or not a given seat has been reserved:
def isEmpty(row, seat):
  return (plane[row][seat] != "R" and plane[row][seat] != "Y")

# Check how many free consecutive seats are available in a row beginning at a given seat:
def freeSeatsAt(row,seat):
  n = 0
  while (seat<6 and isEmpty(row,seat)):
    n += 1
    seat += 1
  return n
 
# Construct a list to hold 10 rows of seats.
plane = [[]]

# Construct each row with 6 empty seats each.
for i in range(10):
  plane.append(["A","B","C","D","E","F"])

while True:
  customerStatus = input("\nEnter \"R\" for Regular, \"E\" for Economy,  \"M\" for Manifest: ")

  if customerStatus == "R" or customerStatus == "r":
    #displaySeats()
    askRegular()
    #ask for ticket info
    
    #Adjusts available seats - Creates a list of available seats?
    #Seat Selection Function - Displays available seats, customer selects a seat, seat removed from available seats, and assigned to customer.
  elif customerStatus == "E" or customerStatus == "e": 
    askEconomy()

  else:
    displayManifest()
