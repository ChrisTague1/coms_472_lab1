def get_next_states(state):
    states = []
    i = state.index(0)

    if i <= 5:
        next_state = state[:]
        next_state[i], next_state[i + 3] = next_state[i + 3], next_state[i]
        states.append((next_state, 'U'))
    if i >= 3:
        next_state = state[:]
        next_state[i], next_state[i - 3] = next_state[i - 3], next_state[i]
        states.append((next_state, 'D'))
    if i % 3 != 2:
        next_state = state[:]
        next_state[i], next_state[i + 1] = next_state[i + 1], next_state[i]
        states.append((next_state, 'L'))
    if i % 3 != 0:
        next_state = state[:]
        next_state[i], next_state[i - 1] = next_state[i - 1], next_state[i]
        states.append((next_state, 'R'))
    return states


def ids(initial, goal_state):
    visited = [initial]
    queue = [(initial, [])]

    while len(queue) > 0:
        state, path = queue.pop(-1)

        if state == goal_state:
            return

        for next_state, next_path in get_next_states(state):
            if next_state not in visited:
                visited.append(next_state)
                queue.append((next_state, path + [next_path]))