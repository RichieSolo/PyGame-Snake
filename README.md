# PyGame-Snake
Python Snake Pygame

Done-----------------------------------------------

*Randomized food spread:
When player touches food, food dissapears, new one will generate.
Solution: Using the Distance formula, calculated distance between player head and food. When player head touches food, the background is redrawn and the food's position is randomly generated again.

*Counter (Points) 
Solution: Counter changes according to each food eaten by player; calculated by checking when the head is 15 pixels away from the food, if so, add 1 to the Score counter

To do---------------------------------------------

*Movement (According to length) 
Snake head must point in direction of key press, remaining segments must follow
Segmentation

*Endgame conditions (2)
Death (Touch self, touch barrier)

Player Position Update
Program needs to know size of player model (It is currently a single point)
Array(s)

