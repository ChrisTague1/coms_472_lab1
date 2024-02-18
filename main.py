import sys
from bfs import bfs
from display import display
from ids import ids


def parse_file(file_path):
    puzzle = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            row = [int(x) if x != '_' else 0 for x in line.split()]
            puzzle.extend(row)
    return puzzle


def is_solvable(state):
    inversions = 0
    for i, n in enumerate(state):
        for j in range(i + 1, 9):
            if state[j] == 0:
                continue
            if n > state[j]:
                inversions += 1
    return inversions % 2 == 0


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <file_path> <BFS|IDS|h1|h2|h3>")
        sys.exit(1)

    state = parse_file(sys.argv[1])

    if not is_solvable(state):
        display(state)
        print("Puzzle is not solvable")
        sys.exit(1)

    goal_state = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 0
    ]

    command = sys.argv[2]

    if command == "BFS":
        bfs(state, goal_state)
    elif command == "IDS":
        ids(state, goal_state)
    elif command == "h1":
        print('not implemented yet')
    elif command == "h2":
        print('not implemented yet')
    elif command == "h3":
        print('not implemented yet')
    else:
        print("Please provide valid command")
        print("Usage: python main.py <file_path> <BFS|IDS|h1|h2|h3>")


if __name__ == '__main__':
    main()
