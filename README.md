# 4160-Project1-PONG


pygame 2.1.2 

Win10 Pro Version	10.0.19045 Build 19045

Python 3.10.10

I chose pong due to its simplistic nature, and hope to create a 2 player pong controlled by WS and UpDown arrows. The left paddle moves via WS, and the right paddle by UpDown keys. There is currently no scoring mechanism. 

# mainView.py
mainView takes information from paddle.py to render the paddle on the screen, depending on the X,Y,size info contained in paddle.py

# gameScript.py
This file initalizes every other class, and contains the while loop running the game. 

# paddle.py
This file contains the render information for the paddle, including size,color,position. This file also contains move_rect(), which is called in the controller and moves the paddle. This function also handles the proper bounds for the paddle, ensuring it doesnt leave the screen. move_rect() acts identically regardless of which paddle is moving. setPlayer2() is used in mainView to determine which paddle is on the right side of the screen.

# controller.py
This file contains the mainController class, whos main purpose is to manage user inputs. userInput() is called in the gameScript loop, and passes movement information into the paddle to be executed. userInput() takes both paddle objects as arguements, and sends move signals appropiately depending on WS/UpDown entrances. 
