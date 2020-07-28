#code sourced from http://pythonfiddle.com/nim-game-prototype/ and edited


total =0
sticks = (13)

playerState = into(0)

#game mechancis 


while (sticks > 0):
   if (playerState %2 !=1):
      playerMove = int(raw_inut("Zoey,Please enter your move:"))
    if (playerMove > 0) and (playerMove < 5) and (playerMove <= sticks):
    		sticks = sticks - playerMove
      playerState +=1
      print sticks 
      print playerState
     else: 
        print "Wrong move, try again"
       else: 
          playerMove = int(raw_inut("Josh,Please enter your move:"))
             if (playerMove > 0) and (playerMove < 5) and (playerMove <= sticks):
      sticks = sticks - playerMove
      playerState +=1
      print sticks 
      print playerState

winner = int(playerState %2)

if (winner ! =1)
print ("Congrats Zoey!")
else:
  print ("Congrats Josh!")

    