<img width="1831" height="1013" alt="output" src="https://github.com/user-attachments/assets/d0b8d8fd-cd3c-4e2c-b3fe-2a76d160d88a" /># CODSOFT AI Internship - Task 1

## Rule-Based Chatbot

This project is a simple rule-based chatbot developed as part of the CodSoft Artificial Intelligence Internship.

The chatbot interacts with users and provides predefined responses based on user input.

## Technologies Used

- Python
- If-Else Statements
- While Loop
- String Handling example-.lower(), .strip()

## Features

- Responds to greetings
- Answers basic questions
- Handles simple conversations
- Recognizes uppercase and lowercase input
- Provides responses using predefined rules
- Continues the conversation until the user exits

## How It Works

The chatbot takes input from the user and compares it with predefined rules using if-else statements.

For example:

- "hello" → Greeting response
- "how are you" → General response
- "what is your name" → Introduction
- "thank you" → Welcome response
- "bye" → Exit the chatbot

## How to Run

1. Install Python.
2. Download or clone this repository.
3. Open the project in VS Code.
4. Run `chatbot.py`.
5. Enter messages in the terminal.
6. Type `bye` or `exit` to stop the chatbot.

## Project Structure

```text
CODSOFT_TASKNO
│
├── chatbot.py
└── README.md
```
## Internship

This project was completed as part of the CodSoft Artificial Intelligence Internship.

### Task 1: Chatbot with Rule-Based Responses

The chatbot uses predefined rules and if-else statements to respond to user inputs and provide a basic conversational experience.

### Chatbot Output

![Chatbot Output](![Uploading output.png…])
)
# Task 2 - Tic-Tac-Toe AI

##  Project Description

This project is a Python-based Tic-Tac-Toe game in which a human player plays against an AI opponent.

The AI uses the **Minimax algorithm** to analyze possible moves and select an appropriate move during the game.

## Objective

The main objective of this project is to understand:

- Basic game development using Python
- AI decision-making
- Minimax algorithm
- Game-state evaluation
- Logical problem solving

##  Technologies Used

- **Python**
- **Minimax Algorithm**
- **VS Code**

##  How the Game Works

- The player uses **X**.
- The AI uses **O**.
- The player selects a position from **1 to 9**.
- The AI analyzes the available moves using Minimax.
- The game continues until a player wins or the game ends in a draw.

### Board Positions

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
# Movie Recommendation System

##About the Project
The Movie Recommendation System is a beginner-friendly Python project that recommends movies based on genre similarity. Users can select a movie from the available database and receive recommendations for other movies with similar genres.

This project demonstrates the basic concepts of Python programming, lists, dictionaries, functions, loops, and sorting.

##  Features
- Display all available movies.
- Search for a movie by its title.
- Recommend up to five similar movies.
- Display movie genres and ratings.
- Handle invalid menu choices and unknown movie titles.
- Simple command-line interface.

## Technologies Used
- Python 3
- Built-in Python libraries
- VS Code
- Git and GitHub

## 📂 Project Structure
```text
Movie-Recommendation-System/
├── movie_recommender.py
├── README.md
└── requirements.txt
```

## How to Run the Project

### Step 1: Install Python
Install Python 3 from https://www.python.org/downloads/

### Step 2: Download or Clone the Repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### Step 3: Open the Project
Open the project folder in Visual Studio Code.

### Step 4: Run the Program
Open the terminal and execute:

```bash
python movie_recommender.py
```

On some Windows installations, you may need to use:

```bash
py movie_recommender.py
```

## 💻 Sample Output

```text
========================================
   MOVIE RECOMMENDATION SYSTEM
========================================

1. View all movies
2. Get movie recommendations
3. Exit

Enter your choice (1-3): 2
Enter a movie name: Inception

Movies similar to 'Inception':
- Avengers: Endgame | Genre: Action, Sci-Fi | Rating: 8.4
- Iron Man | Genre: Action, Sci-Fi | Rating: 7.9
- Interstellar | Genre: Sci-Fi, Drama | Rating: 8.7
```

The actual recommendation order depends on the number of matching genres and the movie ratings.

##  How It Works
1. The system stores movie titles, genres, and ratings in a list of dictionaries.
2. The user enters a movie title.
3. The program searches for the selected movie.
4. It compares the selected movie's genres with the genres of other movies.
5. Movies sharing genres are ranked by genre matches and ratings.
6. The system displays up to five recommendations.

##  Concepts Used
- Lists and dictionaries
- Functions
- Loops and conditional statements
- String handling
- Sets and set intersection
- Sorting with a custom key
- Basic input validation

##  Future Improvements
- Add a graphical user interface.
- Use a larger movie dataset.
- Include user ratings and preferences.
- Integrate a movie database API.
- Implement content-based filtering with more detailed movie features.

##  Learning Outcome
This project helps beginners understand how a simple recommendation system works and how Python data structures can be used to compare items and generate useful suggestions.


