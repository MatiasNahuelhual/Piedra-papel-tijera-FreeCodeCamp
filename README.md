# Piedra Papel o Tijeras

This is the boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

# Descripción

Para este reto, crearás un programa para jugar a Piedra, Papel o Tijera. Un programa que elige al azar suele ganar el 50% de las veces. Para superar este reto tu programa debe jugar partidos contra cuatro bots diferentes, ganando al menos el 60% de las partidas en cada partido.

En el archivo RPS.py se proporciona una función llamada player. La función toma un argumento que es una cadena que describe el último movimiento del oponente ("R", "P", o "S"). La función debe devolver una cadena que representa el siguiente movimiento que debe realizar ("R", "P", o "S").

Una función de jugador recibirá una cadena vacía como argumento para la primera partida de un partido, ya que no hay jugadas anteriores.

El archivo RPS.py muestra una función de ejemplo que necesitarás actualizar. La función de ejemplo se define con dos argumentos (player(prev_play, opponent_history = [])). La función nunca es llamada con un segundo argumento por lo que éste es completamente opcional. La razón por la que la función de ejemplo contiene un segundo argumento (opponent_history = []) es porque es la única forma de guardar el estado entre llamadas consecutivas de la función player. Sólo necesitas el argumento opponent_history si quieres guardar el estado de opponent_history.

Sugerencia: Para derrotar a los cuatro oponentes, su programa puede necesitar tener múltiples estrategias que cambien dependiendo de las jugadas del oponente.

Traducción realizada con la versión gratuita del traductor DeepL.com
