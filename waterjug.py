from collections import deque
MAX_JUG_4 = 4
MAX_JUG_3 = 3
GOAL = 2
def print_solution(path):
    for step in path:
        print(f"4-gallon jug: {step[0]} gallons, 3-gallon jug: {step[1]} gallons")
    print("Solution achieved!\n")
def bfs():
    queue = deque([((0, 0), [])])
    visited = set()
    while queue:
        (jug4, jug3), path = queue.popleft()
        if jug4 == GOAL:
            print_solution(path + [(jug4, jug3)])
            return True
        if (jug4, jug3) in visited:
            continue
        visited.add((jug4, jug3))
        next_states = [
            (MAX_JUG_4, jug3),
            (jug4, MAX_JUG_3),
            (0, jug3),
            (jug4, 0),
            (jug4 - min(jug4, MAX_JUG_3 - jug3), jug3 + min(jug4, MAX_JUG_3 - jug3)),
            (jug4 + min(jug3, MAX_JUG_4 - jug4), jug3 - min(jug3, MAX_JUG_4 - jug4))
        ]
        for state in next_states:
            queue.append((state, path + [(jug4, jug3)]))
    print("No solution found.")
    return False 
bfs()
