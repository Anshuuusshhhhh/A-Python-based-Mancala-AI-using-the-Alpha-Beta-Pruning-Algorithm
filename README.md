📌 Overview
This project implements the classic Mancala board game with an AI opponent that makes optimal moves using the Alpha-Beta Pruning algorithm. 
The AI evaluates possible moves and selects the best strategy to maximize its score while minimizing the opponent’s advantage.

🎯 Game Rules (Brief)
Mancala is a two-player turn-based game played on a board with 14 pits:
Each player has 6 pits to store stones.
Each player owns a Mancala (store pit) to collect captured stones.
Players take turns picking stones from one of their pits and distributing them counterclockwise.
If a player’s last stone lands in their Mancala, they get an extra turn.
The game ends when one player’s pits are empty. The remaining stones go to the other player’s Mancala.
The player with the most stones in their Mancala wins.

  🔥 Features
✅ Mancala Board Simulation – A dynamic representation of the game state.
✅ AI Move Prediction – Uses the Alpha-Beta pruning algorithm for efficient decision-making.
✅ Heuristic Evaluation – AI evaluates board positions for optimal move selection.
✅ Recursive Search – Looks ahead at possible future moves to make better choices.
✅ Customizable Depth – Adjust how many moves ahead the AI considers.

🚀 Implementation Details
Game Logic: The Mancala_Board class manages the game state and player moves.
Alpha-Beta Pruning Algorithm:
Recursively evaluates possible moves.
Uses minimax logic to select the best move.
Applies alpha-beta pruning to cut off unnecessary calculations, improving efficiency.
Heuristic Function: Evaluates board state to guide AI decision-making.

📦 Project Structure
📂 mancala-ai
│── mancala.py        # Mancala board and game logic
│── alphabeta.py      # AI move logic using Alpha-Beta pruning
│── main.py           # Game execution and AI vs. human mode
│── README.md         # Project description and instructions

🛠 How to Run
Install Python
Ensure you have Python 3.x installed.
Play Against AI
You can play as Player 1 or Player 2.
The AI will respond based on the Alpha-Beta algorithm.

⚡ Future Improvements
🔹 GUI Interface – Implement a graphical interface for a better user experience.
🔹 Adjustable AI Difficulty – Modify the depth search level for different difficulty settings.
🔹 Multiplayer Mode – Allow two human players to compete.

🤝 Contributing
Contributions are welcome! Feel free to:
  Improve AI efficiency.
  Add GUI support.
  Enhance the heuristic evaluation function.
  Fork the repo, make changes, and submit a pull request!

⭐ Show Some Love!
If you found this project useful, please star ⭐ the repository on GitHub!


