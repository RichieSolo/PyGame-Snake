# PyGame-Snake
Python Snake Pygame

Done-----------------------------------------------

*Randomized food spread:
When player touches food, food dissapears, new one will generate.
Solution: Using the Distance formula, calculated distance between player head and food. When player head touches food, the background is redrawn and the food's position is randomly generated again.

*Counter (Points):
Solution: Counter changes according to each food eaten by player; calculated by checking when the head is 15 pixels away from the food, if so, add 1 to the Score counter

*Movement (According to length): 
Snake head must point in direction of key press, remaining segments must follow
Solution: Movement is constant in one direction, must press a key again to change direction. 

To do---------------------------------------------

*Segmentation:
Snake must gain one rectangle of same size as head and follow the head according to movement.
Idea: Create some type of function that recognizes the head and adds a new segment when the food is eaten.

*Endgame conditions:
Death (Touch self, touch barrier)
Idea: When either the distance between head to body or head to boundary is equal to some int, write function called player_death() that ends game.

*Restart button
Idea: Create simple "restart" button that resets game to default setting.

