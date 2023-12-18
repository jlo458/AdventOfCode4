file = open("card.txt", "r")

total = 0
for wholeLine in file: 
  wholeLine = wholeLine.split('|') 
  #print(wholeLine)
  winScores = (wholeLine[0][8:]).split()
  #print(winScores)
   
  actScores = (wholeLine[1]).split()
  thisTotal = 0
  #power = 0
  for i in actScores: 
    if i in winScores: 
      if thisTotal == 0: 
        thisTotal +=1 

      else: 
        thisTotal = thisTotal * 2

  total += thisTotal
  #print(actScores)


print(total)
file.close()