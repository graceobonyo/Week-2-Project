Guess the number game

This project is a python based number guessing game allowing users to randomly guess a number between a specific range 1-100 within a limited number of attempts at each different levels .The game includes different levels of difficulty ,a hint system to give you the headsup on the type of answer and a leaderboard for storing player scores in a text file in the order of playing.

# project 
https://github.com/graceobonyo/Guess-the-number/blob/main/guess_the_number.py
https://github.com/graceobonyo/Guess-the-number/blob/main/LICENSE
https://github.com/graceobonyo/Guess-the-number/blob/main/README.md


## core features
 
 * ** Difficulty levels
 There are 3 different level  with different number of attempts namely: 
 Easy -10 attempts
 Medium - 7 attempts
 Hard - 5 attempts
 Each diffiuclyty has a specific number of attempts for a player which decrease with an increase in level.

 * ** Random number generation
 A random between 1 and 100 is selected by the program.The player has the task to guess the randomly generated generated number in the maximum numbeer of attempts for each attempts to complete his game level.

 * ** Hint system
 After three consecutive incorrect attempts, a hint is provided indicating the potential secret number a s either an odd or even number

 * ** High score system
 The score of each player are stored  in a file titled 'highscores.txt'.This file stores player information which inludes username,level of difficulty and the the number of remaining attempts

 * ** Leaderboard display 
 All saved scores are displayed at the end of each game in the leaderboard display

 ### Prerequisites
  * Python 3 +


 #### Running the game 
 * Install python 3 + in your system
 * Save this file as guess_your_number.py
 * Open a terminal
 * Run the game using  python guess_the_number.py

GAME SAMPLE
Welcome to Guess the Number Game. Have fun!
Enter your username: Grace

Choose Difficulty Level:
1. Easy (10 tries)
2. Medium (7 tries)
3. Hard (5 tries)

Make a guess: 50
Too High!
Attempts remaining: 6

Hint: The number is even.

LICENSE
MIT License

Copyright (c) 2026 Grace Obonyo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Grace Obonyo



