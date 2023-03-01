# 4160-Project1-PONG


pygame 2.1.2 

Win10 Pro Version	10.0.19045 Build 19045

Python 3.10.10

I chose pong due to its simple game mechanics, but a necessasity to have a basic working of collisions and game state. This pong game has 2 paddles, controlled by WS and UpDown, and delcares a winner at 5 points. 

# mainView.py
mainView takes information from the paddle and ball objects, and renders them onscreen. mainView.viewUpdate refreshes the screen, and should be one of the last things to happen in the actual gameScript.

# gameScript.py
This file imports all other files, creates the game objects, and then runs a continous loop. THIS IS THE FILE THAT SHOULD BE RUN FOR THE PROGRAM TO WORK!

# paddle.py
This file contains the render information for the paddle, including size,color,position. This file also contains move_rect(), which is called in the controller and moves the paddle. This function also handles the proper bounds for the paddle, ensuring it doesnt leave the screen. move_rect() acts identically regardless of which paddle is moving. setPlayer2() is used in mainView to determine which paddle is on the right side of the screen.

# controller.py
This file contains the mainController class, whos main purpose is to manage user inputs. userInput() is called in the gameScript loop, and passes movement information into the paddle to be executed. userInput() takes both paddle objects as arguements, and sends move signals appropiately depending on WS/UpDown entrances. 

mainController also contains the CollisionDetection() function, which should be run every single frame to determine if any collisions have occured. If a collision occurs, the ball will be propolled back if it hits a paddle. The ball will be reset and a point will be logged if the ball hits the left or right side of the screen.

# model.py
This file contains the model, which holds any scoring mechanisms. The max score can be adjusted here, and the individual scoring for each player can be adjusted by addScorep1 and addScorep2. 

This file is the only file that prints to the console, declaring when a player scores and when the game is over. When a player reaches the max score, detWinner will return True, telling gameScript to end the game.
