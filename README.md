# Numberlink  
Proyecto del curso *Análisis de Algoritmos* (PUJ – Bogotá)

Implementado por:
- Maria Fernanda Cruz Gutierrez
- Anton Patrignani

Este proyecto implementa un algoritmo que solucione un tablero de **Numberlink**, respetando todas las restricciones del juego y las limitaciones propuestas en el enunciado.

El programa recibe como entrada un archivo de texto con un tablero y determina si existe una solución válida conectando todas las parejas siguiendo caminos ortogonales sin cruces.


## Características del proyecto

- Implementación utilizando:
  - Backtracking
  - Verificaciones de alcanzabilidad
  - Heurísticas (parejas más restrictivas primero, vecinos más prometedores)
- Detecta:
  - Errores de formato
  - Símbolos repetidos más de dos veces
  - Tableros sin solución
- Imprime el tablero antes y después de resolverlo.