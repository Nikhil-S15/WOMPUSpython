import random

# Constants
GRID_SIZE = 5
AGENT = 'A'
WUMPUS = 'W'
PIT = 'P'
GOLD = 'G'
BREEZE = 'B'
STENCH = 'S'

# Initialize the grid
grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
agent_x, agent_y = 0, 0
grid[agent_x][agent_y] = AGENT

def place_randomly(symbol):
    while True:
        x, y = random.randrange(GRID_SIZE), random.randrange(GRID_SIZE)
        if grid[x][y] == ' ':
            grid[x][y] = symbol
            break

# Place Wumpus, Pit, and Gold randomly
place_randomly(WUMPUS)
place_randomly(PIT)
place_randomly(GOLD)

def print_grid():
    for row in grid:
        print(' '.join(row))
    print()

def is_valid_move(x, y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE

def agent_move(dx, dy):
    global agent_x, agent_y

    new_x, new_y = agent_x + dx, agent_y + dy

    if is_valid_move(new_x, new_y):
        if grid[new_x][new_y] == PIT:
            print("You fell into a pit and died! Game over.")
            return False
        elif grid[new_x][new_y] == WUMPUS:
            print("You encountered the wumpus and got eaten! Game over.")
            return False
        elif grid[new_x][new_y] == GOLD:
            print("Congratulations! You found the gold and won the game!")
            return False
        else:
            grid[agent_x][agent_y] = ' '
            agent_x, agent_y = new_x, new_y
            grid[agent_x][agent_y] = AGENT
            return True
    else:
        print("Invalid move. Please choose a valid direction.")
        return True

while True:
    print_grid()

    print("Enter your move (Use U, L, R, D to move UP,LEFT,RIGHT,DOWN, Q to quit):")
    move = input().strip().upper()

    if move == 'Q':
        print("You quit the game.")
        break
    elif move == 'U':
        if agent_move(-1, 0):
            print("You moved up.")
    elif move == 'L':
        if agent_move(0, -1):
            print("You moved left.")
    elif move == 'D':
        if agent_move(1, 0):
            print("You moved down.")
    elif move == 'R':
        if agent_move(0, 1):
            print("You moved right.")
    else:
        print("Invalid input. Use U, L, R, D to move UP,LEFT,RIGHT,DOWN or Q to quit.")

print_grid()  # Final grid display
