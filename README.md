# cowboy_game
#README

1.Function:
A pygame called cowboy with dangerous. Is a flat 2d game which is positioned as a shooting game. One of the hero is controlled to shoot and dodge monsters.

2.Environment:
The platform is independent. It support systems of MacOs, Windows and linux. The implement on Anaconda python 3.7. User need to install pygame on python.
eg. input command line argument: “pip install pygame”.

3. Usage:
The usage of game is provided by menu screen. The arrow keys control the movement of the hero. The keys of “W,S,A,D” control the direction of shooting. The key of “R” can change a hero. The difficulty of the game increases with time. The player need focus on dodging any monster attack and approach. The game fails when the hero runs out of HP. The winning condition is survival within the time limit.

4. Structure:
|————————class——————————
|-class Hero()  # Two Hero
|-class Hero2(Hero) 
|-class Enemy1() # Three Monster
|-class Enemy2( Enemy1)
|-class Boss(Enemy1)
|-class Background()# Background Image 
|-class Weapon() # Two character weapon
|-class Weapon2(Weapon)
|-class Weapon3(Weapon)# Boss weapon
|-class timer()
|—————————————————————

|——————system function———————
|-def process() #draw the scenario
|-def show() #show HP, Time, Points
|-def show2() # show Text of “WIN” of “LOST”
|-def clean_screen() #clean for restart
|-def check_number_herobullets()
|-def objectupdated()
|————————————————————-

5. Process                                                       
screen1: click to begin the game 
-> screen2: run the game -> Run out of HP/Time out 
-> screen3: “FAILURE, press press space to restart”/ “WINNER, press space to restart”
-> screen1 / close window
                                                  






