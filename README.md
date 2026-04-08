Guess the number game

This project is a python based number guessing game allowing users to randomly guess a number between a specific range 1-100 within a limited number of attempts at each different levels .The game includes different levels of difficulty ,a hint system to give you the headsup on the type of answer and a leaderboard for storing player scores in a text file in the order of playing.

## Features
 
 * ** Difficulty levels:**There are 3 different levels to choose from namely:Easy, Medium, Hard modes.

 * ** Random number generation:**A random between 1 and 100 is selected by the program.The player has the task to guess the randomly generated generated number in the maximum numbeer of attempts for each attempts to complete his game level.

 * ** Hint system:**After three consecutive incorrect attempts, a hint is provided indicating the potential secret number a s either an odd or even number.

 * ** High score system:**The score of each player are stored  in a file titled 'highscores.txt'.This file stores player information which inludes username,level of difficulty and the the number of remaining attempts.

 * ** Leaderboard display:**All saved scores are displayed at the end of each game in the leaderboard display.

## Technical Stack
* ** Language : ** Python 3
* ** Modules:** random(Standard Library)
* ** Storage :** file system

### Prerequisites
* **  Install python on your machine.Check your version by running ''bash python --version

### Installation and setup
**Clone the Repository:**

    ```bash
git clone https://github.com/graceobonyo/Guess-the-number.git
cd guess-the-number
    ```

2.  **Run the Game:**
    No external dependencies are required. Simply execute the script:

    ```bash
    python main.py
    ```

## How to play

**Enter Username:** Provide your name for the leaderboard.

**Select Difficulty:**
      
      * **Easy:** 10 attempts
      * **Medium:** 7 attempts
      * **Hard:** 5 attempts

**Guess:** Input your numbers. The system will give you feedback stating whether  your guess is "Too High" or "Too Low."

**Win/Loss:** If you guess the secret number correctly, your remaining attempts are saved as your score. If you run out of tries, the secret number is revealed.

## Contributing

Contributions are what make the open-source community an excellent place to learn, inspire, and create. Any contributions you make are welcomed.

### How to Contribute

**Fork the Project**

**Create your Feature Branch**
    ```bash
    git checkout -b feature/AmazingFeature
    ```

**Commit your Changes**
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```

**Push to the Branch**
    ```bash
    git push origin feature/AmazingFeature
    ```

**Open a Pull Request**


### Areas for Improvement

  * Adding a "Play Again" loop so the game does not end after one round.
  * Implementing a scoring system based on total time taken to complete each round.
  
## Project Structure

```text
├── main.py            # Main game information
├── highscores.txt     # Local database for storing player scores (auto-generated)
└── README.md          # Project information
```

## License

This project is open-source and available under the [MIT License](https://github.com/graceobonyo/Guess-the-number/blob/main/LICENSE)

