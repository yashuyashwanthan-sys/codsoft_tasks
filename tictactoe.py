# ============================================================
# TASK 2: TIC-TAC-TOE AI (with Minimax Algorithm)
# CodSoft AI Internship - Batch C19
# ============================================================
# WHAT THIS DOES:
# A Tic-Tac-Toe game where YOU play against an AI.
# The AI uses the "Minimax" algorithm — it thinks ahead
# and picks the best possible move every time.
# It is literally UNBEATABLE. Best you can do is draw!
# ============================================================

# ---------------------------------------------------------------
# STEP 1: Board Setup
# The board is a list of 9 spots (index 0 to 8)
# Visually it looks like:
#   0 | 1 | 2
#   ---------
#   3 | 4 | 5
#   ---------
#   6 | 7 | 8
# ---------------------------------------------------------------

def create_board():
    """Returns a fresh empty board (9 empty spaces)"""
    return [" "] * 9

def print_board(board):
    """Prints the board in a nice grid format"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# ---------------------------------------------------------------
# STEP 2: Game Logic
# Check for wins, draws, and available moves
# ---------------------------------------------------------------

# All possible winning combinations (rows, columns, diagonals)
WINNING_COMBOS = [
    [0, 1, 2],  # top row
    [3, 4, 5],  # middle row
    [6, 7, 8],  # bottom row
    [0, 3, 6],  # left column
    [1, 4, 7],  # middle column
    [2, 5, 8],  # right column
    [0, 4, 8],  # diagonal top-left to bottom-right
    [2, 4, 6],  # diagonal top-right to bottom-left
]

def check_winner(board, player):
    """Returns True if the given player ('X' or 'O') has won"""
    for combo in WINNING_COMBOS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_draw(board):
    """Returns True if the board is full and nobody won"""
    return " " not in board

def get_available_moves(board):
    """Returns a list of indexes where the board is still empty"""
    return [i for i, spot in enumerate(board) if spot == " "]

# ---------------------------------------------------------------
# STEP 3: The Minimax Algorithm (THE BRAIN OF THE AI)
# ---------------------------------------------------------------
# HOW MINIMAX WORKS (simple explanation):
# The AI imagines ALL possible future moves.
# - If AI wins in that future → score = +1 (good!)
# - If Human wins in that future → score = -1 (bad!)
# - If it's a draw → score = 0
# The AI always picks the move with the HIGHEST score.
# The human is assumed to play the BEST possible move too.
# ---------------------------------------------------------------

def minimax(board, is_ai_turn):
    """
    Recursively explores all possible game outcomes.
    Returns +1 if AI wins, -1 if human wins, 0 for draw.
    
    'is_ai_turn': True when it's the AI's turn to think
    """
    # Base cases — check if the game is already over
    if check_winner(board, "O"):  # AI is "O"
        return 1
    if check_winner(board, "X"):  # Human is "X"
        return -1
    if is_draw(board):
        return 0

    available = get_available_moves(board)

    if is_ai_turn:
        # AI wants to MAXIMIZE the score
        best_score = -float("inf")  # Start with worst possible score
        for move in available:
            board[move] = "O"                          # Try this move
            score = minimax(board, False)              # See what human does next
            board[move] = " "                          # Undo the move
            best_score = max(best_score, score)        # Keep the best score
        return best_score
    else:
        # Human wants to MINIMIZE the score (from AI's perspective)
        best_score = float("inf")   # Start with worst possible score
        for move in available:
            board[move] = "X"                          # Try this move
            score = minimax(board, True)               # See what AI does next
            board[move] = " "                          # Undo the move
            best_score = min(best_score, score)        # Keep the lowest score
        return best_score

def get_best_move(board):
    """
    Loops through all available moves, runs minimax on each,
    and returns the move with the highest score (best for AI).
    """
    best_score = -float("inf")
    best_move = None

    for move in get_available_moves(board):
        board[move] = "O"                          # Try this move
        score = minimax(board, False)              # Evaluate it
        board[move] = " "                          # Undo the move
        if score > best_score:
            best_score = score
            best_move = move

    return best_move

# ---------------------------------------------------------------
# STEP 4: Main Game Loop
# ---------------------------------------------------------------

def play_game():
    print("=" * 40)
    print("   TIC-TAC-TOE — You vs. AI 🤖")
    print("=" * 40)
    print("You are X | AI is O")
    print("Enter a position number (0-8):")
    print("\n  0 | 1 | 2")
    print("  ---+---+---")
    print("  3 | 4 | 5")
    print("  ---+---+---")
    print("  6 | 7 | 8\n")

    board = create_board()
    print_board(board)

    while True:
        # --- Human's Turn ---
        while True:
            try:
                move = int(input("Your move (0-8): "))
                if move < 0 or move > 8:
                    print("Please enter a number between 0 and 8.")
                elif board[move] != " ":
                    print("That spot is already taken! Choose another.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        board[move] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("🎉 You WIN! Congratulations!")
            break
        if is_draw(board):
            print("🤝 It's a DRAW! Well played!")
            break

        # --- AI's Turn ---
        print("AI is thinking... 🤔")
        ai_move = get_best_move(board)
        board[ai_move] = "O"
        print(f"AI chose position {ai_move}")
        print_board(board)

        if check_winner(board, "O"):
            print("🤖 AI WINS! Better luck next time!")
            break
        if is_draw(board):
            print("🤝 It's a DRAW! Well played!")
            break

    # Ask to play again
    again = input("Play again? (yes/no): ").lower()
    if again in ["yes", "y"]:
        play_game()
    else:
        print("Thanks for playing! 👋")

# ---------------------------------------------------------------
# Run the game
# ---------------------------------------------------------------
if __name__ == "__main__":
    play_game()
