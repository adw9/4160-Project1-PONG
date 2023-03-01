# 4160-Project1-PONG
![image](https://user-images.githubusercontent.com/92704425/222253801-9e4ac183-4546-4cc2-816c-f5cb7e3acf35.png)

# Program Versions
pygame 2.1.2 
Win10 Pro Version	10.0.19045 Build 19045
Python 3.10.10

# Reasoning
I chose pong due to its simple game mechanics, but a necessasity to have a basic working of collisions and game state. This pong game has 2 paddles, controlled by WS and UpDown, and delcares a winner at 5 points. Below, design decisions for every file can be explored. 

# mainView.py
mainView takes information from the paddle and ball objects, and renders them onscreen. mainView.viewUpdate refreshes the screen, and should be one of the last things to happen in the actual gameScript.

mainView acts as the VIEW for the game, serving little function outside of printing the data given to it by paddle.py,ball.py

# gameScript.py
This file imports all other files, creates the game objects, and then runs a continous loop. THIS IS THE FILE THAT SHOULD BE RUN FOR THE PROGRAM TO WORK!

gameScript acts as 1 part of the model and overall game state, as it handles the list of entities and directs each object to call other functions. This file manages most of the game state. 

# paddle.py
This file contains the render information for the paddle, including size,color,position. This file also contains move_rect(), which is called in the controller and moves the paddle. This function also handles the proper bounds for the paddle, ensuring it doesnt leave the screen. move_rect() acts identically regardless of which paddle is moving. setPlayer2() is used in mainView to determine which paddle is on the right side of the screen.

This file acts as part of the model, holding data for each player. This file is called by both the gameScript and the controller, and its data is manipulated by both. 

# controller.py
This file contains the mainController class, whos main purpose is to manage user inputs. userInput() is called in the gameScript loop, and passes movement information into the paddle to be executed. userInput() takes both paddle objects as arguements, and sends move signals appropiately depending on WS/UpDown entrances. 

mainController also contains the CollisionDetection() function, which should be run every single frame to determine if any collisions have occured. If a collision occurs, the ball will be propolled back if it hits a paddle. The ball will be reset and a point will be logged if the ball hits the left or right side of the screen.

mainController acts as the controller, managing user input and relaying that to the model, through move_rect() and collisionDetection(). 

# score.py
This file handles scoring for the players. In the future, it would be smart to optimize this into just being a part of paddle.py

This file is the only file that prints to the console, declaring when a player scores and when the game is over. When a player reaches the max score, detWinner will return True, telling gameScript to end the game.

score.py acts as a minor part of the model, but mostly exists as a relic of misinterpreted instructions.

# File Structure

# Future Work
In the future, the functionality of score.py should be incorporated into paddle.py, as score.py being its own class with functions is mostly redundant. A solution to better movement functionality would also be a strong future work item, as currently up/down arrows will overrride commands from WS. The paddles can not move simultaneously. 

# Generalization
gameScript can be easily updated to manage a different number of games, as it just calls other functions, without knowledge of their functionality. paddle.py can be generalized to just be a user controlled character, with the inclusion of a method to move on the X axis. ball.py cannot be generalized much, and would be useless in another game.

controller.py has the strongest amount of generalization possibilities, as it handles collisions with the screen bounds and objects. controller.py also handles user input, something that would require almost no changes for a game bigger than Pong. 
