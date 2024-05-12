# La función de ejemplo siguiente realiza un seguimiento del historial del oponente y reproduce lo que el oponente jugó hace dos jugadas. 
# No es un muy buen jugador, por lo que deberás cambiar el código para superar el desafío.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 1:
        guess = opponent_history[-1]

    return guess
