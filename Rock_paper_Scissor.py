import random
l=["ROCK","PAPER","SCISSOR"]
ccount=0
ucount=0


while True:
    uc=int(input('''Wanna Play...
1 YES
2 NO
              '''))
    if uc==1:
            for a in range(1,6):
               userinput=int(input('''
1 ROCK
2 PAPER
3 SCISSOR
                      '''))
             if userinput==1:
                 usechoice="ROCK"
             elif userinput==2:
                 userchoice="PAPER"
             elif userinput==3:
                 userchoice=="SCISSOR"
            cchoice=random.choice(l)
        
            if(cchoice==userchoice):
              print("computer choice",cchoice)
              print("your choice",userchoice)
              print("GAME DRAW")
              ccount=ccount+1
              ucount=ucount+1
           elif (userchoice=="ROCK" and cchoice=="SCISSOR")or(userchoice=="PAPAER" and
            cchoice=="ROCK")or(userchoice=="SCISSOR" and cchoice=="PAPER"):
             print("computer choice",cchoice)
             print("your choice",userchoice)
             print("YOU WON")
             ucount=ucount+1;
          else:
             print("computer choice",cchoice)
             print("your choice",userchoice)
             print("YOU LOSE")
            ccount=ccount+1
            
    if ucount==ccount:
       print("GAME DRAW")
    elif ucount>ccount:
       print("CONGRATS! YOU WON")
    else:
        print("HARD LUCK,TRY NEXT TIME")
        else:
        break

                 
