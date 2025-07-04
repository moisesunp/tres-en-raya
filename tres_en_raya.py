#!/usr/bin/env python3
"""
Juego de Tres en Raya (Tic-Tac-Toe)
Un juego clásico implementado en Python para dos jugadores.
"""

import os
import sys
import time

class TresEnRaya:
    def __init__(self):
        """Inicializa el juego con un tablero vacío."""
        self.tablero = [' ' for _ in range(9)]
        self.jugador_actual = 'X'
        self.juego_terminado = False
        self.ganador = None
    
    def mostrar_tablero(self):
        """Muestra el tablero actual del juego."""
        print("\n" + "="*25)
        print("      TRES EN RAYA")
        print("="*25)
        print("\n📋 Tablero actual:")
        print("┌───┬───┬───┐")
        print(f"│ {self.tablero[0] if self.tablero[0] != ' ' else '·'} │ {self.tablero[1] if self.tablero[1] != ' ' else '·'} │ {self.tablero[2] if self.tablero[2] != ' ' else '·'} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tablero[3] if self.tablero[3] != ' ' else '·'} │ {self.tablero[4] if self.tablero[4] != ' ' else '·'} │ {self.tablero[5] if self.tablero[5] != ' ' else '·'} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tablero[6] if self.tablero[6] != ' ' else '·'} │ {self.tablero[7] if self.tablero[7] != ' ' else '·'} │ {self.tablero[8] if self.tablero[8] != ' ' else '·'} │")
        print("└───┴───┴───┘")
        print("\n📍 Posiciones:")
        print("┌───┬───┬───┐")
        print("│ 1 │ 2 │ 3 │")
        print("├───┼───┼───┤")
        print("│ 4 │ 5 │ 6 │")
        print("├───┼───┼───┤")
        print("│ 7 │ 8 │ 9 │")
        print("└───┴───┴───┘")
    
    def movimiento_valido(self, posicion):
        """Verifica si un movimiento es válido."""
        return 0 <= posicion <= 8 and self.tablero[posicion] == ' '
    
    def hacer_movimiento(self, posicion):
        """Realiza un movimiento en el tablero."""
        if self.movimiento_valido(posicion):
            self.tablero[posicion] = self.jugador_actual
            return True
        return False
    
    def verificar_ganador(self):
        """Verifica si hay un ganador."""
        # Definir las combinaciones ganadoras
        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        
        for combo in combinaciones_ganadoras:
            if (self.tablero[combo[0]] == self.tablero[combo[1]] == 
                self.tablero[combo[2]] != ' '):
                self.ganador = self.tablero[combo[0]]
                return True
        return False
    
    def tablero_lleno(self):
        """Verifica si el tablero está lleno."""
        return ' ' not in self.tablero
    
    def cambiar_jugador(self):
        """Cambia el turno al siguiente jugador."""
        self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
    
    def obtener_movimiento(self):
        """Obtiene el movimiento del jugador actual."""
        while True:
            try:
                print(f"\n🎮 Turno del jugador {self.jugador_actual}")
                entrada = input("📍 Elige una posición (1-9) o 'q' para salir: ")
                
                if entrada.lower() == 'q':
                    return None
                
                posicion = int(entrada) - 1
                
                if not (0 <= posicion <= 8):
                    print("❌ Posición inválida. Elige un número entre 1 y 9.")
                    continue
                
                if not self.movimiento_valido(posicion):
                    print("❌ Esa posición ya está ocupada. Elige otra.")
                    continue
                
                return posicion
                
            except ValueError:
                print("❌ Entrada inválida. Ingresa un número entre 1 y 9.")
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_movimiento_realizado(self, posicion):
        """Muestra el movimiento que se acaba de realizar."""
        print(f"\n✅ Jugador {self.jugador_actual} colocó su ficha en la posición {posicion + 1}")
        time.sleep(1)  # Pausa breve para que se vea el movimiento
    
    def jugar(self):
        """Método principal para ejecutar el juego."""
        self.limpiar_pantalla()
        print("🎯 ¡Bienvenido al juego de Tres en Raya!")
        print("👥 El jugador X siempre comienza.")
        print("💡 Ingresa 'q' en cualquier momento para salir del juego.")
        print("\n" + "="*40)
        
        while not self.juego_terminado:
            self.mostrar_tablero()
            
            movimiento = self.obtener_movimiento()
            if movimiento is None:
                print("\n👋 ¡Gracias por jugar!")
                return
            
            if self.hacer_movimiento(movimiento):
                self.mostrar_movimiento_realizado(movimiento)
                
                if self.verificar_ganador():
                    self.limpiar_pantalla()
                    self.mostrar_tablero()
                    print(f"\n🎉 ¡El jugador {self.ganador} ha ganado!")
                    self.juego_terminado = True
                elif self.tablero_lleno():
                    self.limpiar_pantalla()
                    self.mostrar_tablero()
                    print("\n🤝 ¡Es un empate!")
                    self.juego_terminado = True
                else:
                    self.cambiar_jugador()
                    self.limpiar_pantalla()
    
    def reiniciar_juego(self):
        """Reinicia el juego para una nueva partida."""
        self.tablero = [' ' for _ in range(9)]
        self.jugador_actual = 'X'
        self.juego_terminado = False
        self.ganador = None


def main():
    """Función principal del programa."""
    while True:
        juego = TresEnRaya()
        juego.jugar()
        
        if not juego.juego_terminado:
            break
        
        print("\n🔄 ¿Quieres jugar otra partida?")
        respuesta = input("📝 Ingresa 's' para sí o cualquier otra tecla para salir: ")
        
        if respuesta.lower() != 's':
            print("\n👋 ¡Gracias por jugar!")
            break
        
        juego.limpiar_pantalla()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Juego interrumpido!")
        sys.exit(0)
