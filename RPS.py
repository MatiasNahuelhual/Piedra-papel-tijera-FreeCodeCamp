def counter_move(move):
    if move == 'R':
        return 'P'
    elif move == 'P':
        return 'S'
    else:
        return 'R'

def player(prev_opponent_play, opponent_history=[], my_history=[],
           quincy_detected=False, kris_detected=False):
    quincy_cycle = ['R', 'R', 'P', 'P', 'S', 'S']
    
    if not prev_opponent_play:
        opponent_history.clear()
        my_history.clear()
        quincy_detected = False
        kris_detected = False
    else:
        opponent_history.append(prev_opponent_play)
    
    next_move = 'R'
    
    if not quincy_detected and len(opponent_history) >= 6:
        quincy_detected = True
        for i in range(len(opponent_history)):
            if opponent_history[i] != quincy_cycle[i % 6]:
                quincy_detected = False
                break
    
    if quincy_detected:
        next_index = len(opponent_history) % 6
        predicted_move = quincy_cycle[next_index]
        next_move = counter_move(predicted_move)
        my_history.append(next_move)
        return next_move
    
    if not kris_detected and len(my_history) >= 1 and len(opponent_history) >= 1:
        kris_detected = True
        for i in range(len(opponent_history)):
            if i >= len(my_history):
                break
            expected = counter_move(my_history[i])
            if opponent_history[i] != expected:
                kris_detected = False
                break
    
    if kris_detected:
        if my_history:
            predicted_move = counter_move(my_history[-1])
            next_move = counter_move(predicted_move)
        my_history.append(next_move)
        return next_move
    
    n = 2
    if len(opponent_history) >= n:
        transitions = {}
        for i in range(len(opponent_history) - n):
            state = tuple(opponent_history[i:i+n])
            next = opponent_history[i + n]
            if state not in transitions:
                transitions[state] = {'R': 0, 'P': 0, 'S': 0}
            transitions[state][next] += 1
        
        last_state = tuple(opponent_history[-n:])
        if last_state in transitions:
            next_counts = transitions[last_state]
            predicted_move = max(next_counts, key=next_counts.get)
        else:
            counts = {'R': 0, 'P': 0, 'S': 0}
            for move in opponent_history:
                counts[move] += 1
            predicted_move = max(counts, key=counts.get) if sum(counts.values()) > 0 else 'R'
        next_move = counter_move(predicted_move)
    else:
        if opponent_history:
            counts = {'R': 0, 'P': 0, 'S': 0}
            for move in opponent_history:
                counts[move] += 1
            predicted_move = max(counts, key=counts.get)
            next_move = counter_move(predicted_move)
        else:
            next_move = 'R'
    
    my_history.append(next_move)
    return next_move