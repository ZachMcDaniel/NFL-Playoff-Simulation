"""
Created on Fri May  1 17:07:01 2020

@author: Zachary McDaniel, Erik Fisher, Andrew Huffman
"""

from bs4 import BeautifulSoup
import requests
import random 
import time

#Function 1: Collecting Teams and Rankings

rankings = 'https://www.espn.com/nfl/story/_/id/28954398/2020-nfl-power-rankings-1-32-poll-plus-where-team-stands-free-agency'
teams = []
def get_rankings():
    '''
    This function scraps data from the given url of NFL team rankings
    and returns a list of the rankings from 1 to 32
    '''
    url = rankings
    page = BeautifulSoup(requests.get(url).text, "html.parser")
    for headlines in page.find_all('h2', ):
        teams.append(headlines.text.strip())
    del teams[17:20] #teams 17:20 were not actually teams but irrelevant text
    
    return(teams)



#Function 2: Calculating Weights

team_dict = {}
def team_weights(): 
    '''
    This function writes the teams list into a dictionary and adds an appropriate 
    weight based on ranking.
    '''
    get_rankings()
    counter = 1 
    weight1=.85
    weight = .0 
    for i in teams:
        if teams[counter-1]:
            weight= weight1-(.0139*counter)
            weight = round (weight * 100,2)
        team_dict [counter] = [teams[counter - 1], weight]
        counter+=1
    return team_dict
team_weights()




#Function 3: Selecting 2 teams to play eachother

print(teams) #Provides a list of the team rankings for reference when selecting
print()
print('Here are the teams! The number before a team name is their rank!')
teampicks={}
cowlist=[]
def pick_teams():
    '''
    This fuction uses input to select 2 teams and writes their values into
    teampicks dictionary. 
    '''
    counterB = 1
    while counterB < 3:
        print("You get to pick 8 of these teams for a tournament!")
        cow = int(input('Enter team rank # to use that team: ')) 
        
        if cow not in cowlist : #makes sure that the value hasnt already been picked
            teampicks[counterB] = ((team_dict.get(cow)[0]), team_dict.get(cow)[1])
            counterB +=1
        else:
            cow = int( input ('team already picked! chose another rank: '))
            teampicks[counterB] = ((team_dict.get(cow)[0]), team_dict.get(cow)[1] )
            counterB +=1
        cowlist.append (cow)




#Function 4: The two teams play eachother and a winner is found
        
def game():
    '''
    This function takes the choosen teams and their respective weights
    and simulates a game and prints the winner and their odds of winning.
    '''
    pick_teams()
    home_team_odds= (teampicks.get(1)[1])+5#Home Team receives a home team advantage
    visiting_team_odds= teampicks.get(2)[1]
    if home_team_odds > visiting_team_odds:# higher ranked team must be first
        difference = home_team_odds-visiting_team_odds
        final_weight = difference + 50
        odds= random.randint(0,100)
        if odds < final_weight: #Higher weighted team has a higher % chance to win the game
             a =teampicks.get(1)
             return a  
        else:
             b = teampicks.get(2)
             return b         
    else:
        difference = visiting_team_odds-home_team_odds 
        final_weight = difference + 50
        odds= random.randint(0,100)
        if odds > final_weight:
            c =teampicks.get(1)
            return c
        else:
            d = teampicks.get(2)
            return d




# Function 5 runs a game for a new round   
            
def game2():
    home_team_odds= (round_one[1][1])+5#Home Team receives a home team advantage
    visiting_team_odds= round_one[2][1]
    difference = home_team_odds-visiting_team_odds
    final_weight = difference + 50
    odds= random.randint(0,100)
    if odds < final_weight:
        a =round_one[1]
        round_two[1]=list(a)
    else:
        b = round_one[2]
        round_two[1]=list(b)
    home_team_odds= (round_one[3][1])+5#Home Team receives a home team advantage
    visiting_team_odds= round_one[4][1]
    difference = home_team_odds-visiting_team_odds
    final_weight = difference + 50
    odds= random.randint(0,100)
    if odds < final_weight:
        c =round_one[3]
        round_two[2]=list(c)
    else:
        d = round_one[4]
        round_two[2]=list(d)
        
        
        
#Function 6 creates a championship round and declares a champion!
        
def game3():
    home_team_odds= (round_two[1][1])+5#Home Team receives a home team advantage
    visiting_team_odds= round_two[2][1]
    difference = home_team_odds-visiting_team_odds
    final_weight = difference + 50
    odds= random.randint(0,100)
    if odds < final_weight:
        a =round_two[1]
        round_three[1]=list(a)
    else:
        b = round_two[2]
        round_three[1]=list(b)
      

    



#Function 7 runs all prior code for a tournament

round_one={} #winning teams
round_two={}
round_three={}
def tournament():    
    print()
    print()
    time.sleep(1)#Wait functions are used for readability of final output
    round_one[1]=list((game()))
    round_one[2]=list((game()))
    round_one[3]=list((game()))
    round_one[4]=list((game()))
    print()
    print()
    print('The tournament has begun!' ) 
    time.sleep(3)
    print()
    print()
    print('These teams move on to round 2!')
    print(round_one[1][0],round_one[2][0],round_one[3][0],round_one[4][0])
    print()
    print()
    time.sleep(3)
    game2()#Uses winner from round_one
    print('These teams are going to the championship round!')
    print(round_two[1][0],round_two[2][0])
    print()
    print()
    time.sleep(3)
    game3()#Uses winners from round_2
    print('The '+str(round_three[1][0])+' have won the tournament!' )




