import smtplib, ssl
from random import randint as rand
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import filedialog

######## set deck #########

'''

deck =['h2', 'h3', 'h4', 'h5','s2', 's3', 's4', 's5','c2', 'c3', 'c4', 'c5',]
cardValues = [2,3,4,5,2,3,4,5,2,3,4,5]

'''
#this deck is for testing
global deck

deck = ['h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'hT', 'hJ', 'hQ', 'hK', 'hA',
            's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'sT', 'sJ', 'sQ', 'sK', 'sA',
            'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'cT', 'cJ', 'cQ', 'cK', 'cA',
            'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'dT', 'dJ', 'dQ', 'dK' ,'dA', 'jJ', 'Jj']

global cardValues

cardValues= [2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,0,0]

#'''

########## functions ###########

class player:
    def __init__(self, email):
        self.email = email
        self.name = self.email.split('@')[0]
        self.hand = []
        self.score = 0
        self.totalscore = 0

    def getScore(self):
        global deck
        global cardValues
        score = 0
        for card in self.hand:
            score = score + cardValues[deck.index(card)]
        return score
        

    def refreshHand(self):  #refresh player's hand (send player's current hand to email of player)
        #email setitngs
        port = 465  # For SSL
        password = input("Type your password and press enter: ")
        sender_email = "letsplayfives@gmail.com"
        #receiver_email = "murrayemer1@gmail.com"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Your Hand"
        message["From"] = sender_email
        message["To"] = self.email

        #make HTML strings in diff colours 
        cardStringhtml = []
             
        for card in self.hand:
            if card[0] in ('d','h','j'):
             colour = '"color:rgba(255,0,0,0.8);"'
            else:
             colour = '"color:rgba(0,0,0,0.8);"'
            cardStringhtml.append('<span style='+colour+'><b>'+card+'</b></span>')

        cardStringhtml =" ".join(cardStringhtml)

        if self.getScore() < 6 :
            #score1 = '<b>'+str(self.getScore())+'</b>'
            score = '<span style = "colour:rgba(80,255,20,0.8);">'+str(self.getScore())+'</span>'
        else:
            score = str(self.getScore())
        
        html ="""
        <html>
         <body>
            """+cardStringhtml+"""<br>
           <span style = "color:rgba(20,80,255,0.8);">Score: """+score+"""</span><br>
         </body>
        </html>
        """

        #text for email
        text= " ".join(self.hand)+' Score: '+str(self.getScore())
        
        #send email
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("letsplayfives@gmail.com", password)
            server.sendmail(sender_email, self.email, message.as_string())


def shuffle():  #reshuffle when we run out of cards
    cardsLeft = deck.copy()
    shuffelies =['Every day Im shuffling...','Shuffling...','Shuffling..','Shuffling.....','Shuffle Shuffle..','SHUFFLE.']
    print('\n'+shuffelies[rand(0,(len(shuffelies)-1))])
    time.sleep(1)
    for player in players:     #remove the cards in people's hands from the cards left
     for card in player.hand:
      cardsLeft.remove(card)
    for card in faceUp[:-1]:          #remove the face up cards from the cards left. do this by checking for each char of faceUp plus the letter after. (covers scenario of one or more than one cards) one card and more than one card.
     if card+faceUp[faceUp.index(card)+1] in cardsLeft:    #if card in cardsleft, remove it. some combinations will not be as ever two char is checked.
      cardsLeft.remove(card+faceUp[faceUp.index(card)+1])
    return cardsLeft

#############start game###########

#Set players
players = []
#properly
"""
print('when finished adding players type: done')
playeremail = input('please enter player email:')
while playeremail != ('done', 'Done')
 playeremails.append(playeremail)

"""
#hardcoded
playeremails = #["email1@mail.com","email2@mail.com","email3@mail.com","email4@mail.com"]# insert player's emails here
for playeremail in playeremails:
    players.append(player(playeremail))

#initialise winner and playAgain to start the game
winner = players[rand(0,(len(players)-1))] #pick random 'winner' to start the game
playAgain = 'y'
                      

while playAgain == 'y':

'''
    root= tk.Tk()

canvas1 = tk.Canvas(root, width = 900, height = 600, bg = 'lightsteelblue')
canvas1.pack()
    
    
browseButton_Excel = tk.Button(text='Update Runways6 from latest AODB', command=runways6Update, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 100, window=browseButton_Excel)

browseButton_Excel = tk.Button(text='import Runways6', command=runwayUpdate, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 200, window=browseButton_Excel)

browseButton_Excel = tk.Button(text='remove all airfeilds execpt those in Airfeilds6', command=airfeildsUpdate, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 300, window=browseButton_Excel)

browseButton_Excel = tk.Button(text='Start save-clicker for TODC Calculation', command=startCalc, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 400, window=browseButton_Excel)

browseButton_Excel = tk.Button(text='Run All', command=runAll, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 500, window=browseButton_Excel)


root.mainloop()
'''

    cardsLeft = deck.copy()

    #deal
    for player in players:
        player.hand = []
        for i in range(5):
            card = cardsLeft[rand(0,(len(cardsLeft)-1))]
            cardsLeft.remove(card)
            player.hand.append(card)
            
    #start game
    player = players[((players.index(winner))+(len(players)-1))%len(players)] #initialise 'current player' as player before winner (so when play moves to 'next' player winner goes first)
    faceUp = cardsLeft[rand(0,(len(cardsLeft)-1))] #draw first card
    print('starting card: '+faceUp)
    cardsLeft.remove(faceUp)

    move = 'a' #anything but 'c'

    while move != 'c':                                      #keep playing until someone calls
      cardValid = 0
      player = players[((players.index(player)+1)%len(players))] #move player to next player 
      
      #remove for play
      print(player.hand) #for testing only
      #remove for play
      
      faceUpNew = input('\n\nYour move: '+player.name+'\n\nFace Up : '+faceUp+'\nPlay card or call (c):\n')
      #print('faceUpNew: '+faceUpNew)
      if faceUpNew != 'c':
          while cardValid == 0:     #check if the card is in someone's hand, if not, it's a mistake so ask for a new card
           for card in faceUpNew[:-1]: #fix, doesn't work with no spaces.h3 , 
            #print('each card '+card)
            for eachplayer in players:
             if card+faceUpNew[faceUpNew.index(card)+1] in eachplayer.hand:
              #print('in hand '+card+faceUpNew[faceUpNew.index(card)+1])
              eachplayer.hand.remove(card+faceUpNew[faceUpNew.index(card)+1])
              cardValid = 1
           if cardValid != 1:
            faceUpNew = input('card not valid. please play a valid card:\n')
           
      move = faceUpNew

      if move != 'c':
       move = input('\nWhat would you like to pick up? \n'
            'r (random)\n'
            'f (face up: '+faceUp+')\n')

      if move == 'r':
          faceUp = faceUpNew
          if cardsLeft == []:   #check there's cards to pull from. If not, reshuffle.
           cardsLeft = shuffle()
          drawnCard = cardsLeft[rand(0,(len(cardsLeft)-1))] #draw random card from pack
          cardsLeft.remove(drawnCard)                       #remove drawn card form remaining cards
          player.hand.append(drawnCard)#add card to player's hand
          player.refreshHand()

      if move == 'f':
          if len(faceUp) > 2:
           faceUp = input("Which card are you going to take?\n")
          player.hand.append(faceUp)
          faceUp = faceUpNew
          player.refreshHand()
        
      if move == 'c':
          print('\n\n\nCALL!!\n\n\n')
          print(player.name+" calls with: "+" ".join(player.hand))
          
          time.sleep(1)
          print('and the winner is...')
          time.sleep(2)

          #calculate winner
          scores = []
          winners = []
          for eachplayer in players:
              scores.append(eachplayer.getScore())
              eachplayer.totalscore = eachplayer.totalscore + eachplayer.getScore()

          if (scores.count(min(scores)) < 2):
              winners.append(players[scores.index(min(scores))])
              winners[0].totalscore = winners[0].totalscore - winners[0].getScore()
              print(winners[0].name)
              if (winners[0] != player):
                player.totalscore = player.totalscore +30
          else:
              for eachplayer in players:
                    if (eachplayer.getscore() == min(scores)) and (eachplayer != player):
                        winners.append(eachplayer)
                        eachplayer.totalscore = eachplayer.totalscore - eachplayer.getscore()
                        print(eachplayer.name)
                        player.totalscore = player.totalscore +30
                        time.sleep(1)
                        try:
                            winner = input('who will start?'+" ".join(winners[i].name) )
                        except exceptions as e:
                            print(e)

        
          playAgain = input('play again?\n')






























          

