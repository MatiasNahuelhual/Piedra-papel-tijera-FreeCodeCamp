# La función de ejemplo siguiente realiza un seguimiento del historial del oponente y reproduce lo que el oponente jugó hace dos jugadas. 
# No es un muy buen jugador, por lo que deberás cambiar el código para superar el desafío.

#def player(prev_play, opponent_history=[]):
#    opponent_history.append(prev_play)
#
#    guess = "R"
#    if len(opponent_history) > 1:
#        guess = opponent_history[-1]
#
#    return guess


import random

# Inicialización de la Q-Table
Q_table = {('R', 'R'): 0, ('R', 'P'): 0, ('R', 'S'): 0,
           ('P', 'R'): 0, ('P', 'P'): 0, ('P', 'S'): 0,
           ('S', 'R'): 0, ('S', 'P'): 0, ('S', 'S'): 0}

# Parámetros de Q-learning
alpha = 0.4  # Tasa de aprendizaje
gamma = 0.6  # Factor de descuento // Mas cerca de 0 pienza a corto plazo

def player(prev_play, opponent_history=[]):
    if prev_play == '':
        # Primer movimiento
        guess = 'R'
    else:
        # Añadir el último movimiento del oponente al historial
        opponent_history.append(prev_play)
        
        # Seleccionar la acción con el mayor valor Q
        possible_actions = ['R', 'P', 'S']
        Q_values = [Q_table[(prev_play, a)] for a in possible_actions]
        max_Q = max(Q_values)
        
        # Si hay varias acciones con el mismo valor Q máximo, elegir una al azar
        actions_with_max_Q = [a for a in possible_actions if Q_table[(prev_play, a)] == max_Q]
        guess = random.choice(actions_with_max_Q)
        
        # Actualizar la Q-Table con la recompensa obtenida
        if len(opponent_history) > 1:
            last_state = (opponent_history[-2], opponent_history[-1])
            last_action = opponent_history[-1]
            reward = get_reward(last_action, prev_play)  # Función que define la recompensa
            Q_table[last_state] = Q_table[last_state] + alpha * (reward + gamma * max_Q - Q_table[last_state])

    return guess

def get_reward(player_action, opponent_action):
    # Definir la recompensa basada en el resultado del juego
    if (player_action == 'R' and opponent_action == 'S') or \
       (player_action == 'P' and opponent_action == 'R') or \
       (player_action == 'S' and opponent_action == 'P'):
        return 1  # Ganar
    elif player_action == opponent_action:
        return 0  # Empate
    else:
        return -1  # Perder
