# Tres en Raya (Tic-Tac-Toe)

Un juego clásico de tres en raya implementado en Python.

## Descripción

Este proyecto implementa el juego tradicional de tres en raya donde dos jugadores se turnan para colocar sus marcas (X y O) en una cuadrícula de 3x3. El objetivo es ser el primero en conseguir tres marcas en línea (horizontal, vertical o diagonal).

## Características

- 🎮 Juego para dos jugadores
- 🎯 Interfaz de consola simple y clara
- 🏆 Detección automática de ganador
- 🔄 Opción de jugar múltiples partidas
- ✅ Validación de movimientos

## Requisitos

- Python 3.6 o superior

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/moisesunp/tres-en-raya.git
```

2. Navega al directorio del proyecto:
```bash
cd tres-en-raya
```

## Uso

Para jugar, simplemente ejecuta:

```bash
python tres_en_raya.py
```

## Cómo jugar

1. El juego mostrará una cuadrícula numerada del 1 al 9
2. Los jugadores se turnan para elegir una casilla ingresando el número correspondiente
3. El jugador X siempre comienza
4. El primer jugador en conseguir tres marcas en línea gana
5. Si se llenan todas las casillas sin ganador, es un empate

## Estructura del proyecto

```
tres-en-raya/
├── tres_en_raya.py      # Archivo principal del juego
├── README.md            # Este archivo
└── .gitignore          # Archivos ignorados por Git
```

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Añade nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

Tu nombre - tu.email@example.com

## Próximas mejoras

- [ ] Interfaz gráfica con tkinter
- [ ] Modo contra la computadora con IA
- [ ] Diferentes niveles de dificultad
- [ ] Estadísticas de partidas
- [ ] Modo online multijugador
