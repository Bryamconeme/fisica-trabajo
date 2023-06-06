import matplotlib.pyplot as plt
import numpy as np

def tiro_parabolico(v0, angulo, gravedad):
    # Convertir el ángulo de grados a radianes
    angulo_rad = np.radians(angulo)
    
    # Calcular las componentes horizontal y vertical de la velocidad inicial
    v0x = v0 * np.cos(angulo_rad)
    v0y = v0 * np.sin(angulo_rad)
    
    # Calcular el tiempo total de vuelo
    t_total = (2 * v0y) / gravedad
    
    # Crear un arreglo de tiempo desde 0 hasta t_total con pequeños incrementos
    t = np.linspace(0, t_total, num=100)
    
    # Calcular las posiciones horizontal y vertical en función del tiempo
    x = v0x * t
    y = v0y * t - 0.5 * gravedad * t**2
    
    return x, y

# Parámetros iniciales
velocidad_inicial = 10  # m/s
angulo_lanzamiento = 45  # grados
gravedad = 9.8  # m/s^2

# Obtener las posiciones x e y
x, y = tiro_parabolico(velocidad_inicial, angulo_lanzamiento, gravedad)

# Graficar la trayectoria del proyectil
plt.plot(x, y)
plt.xlabel('Distancia (m)')
plt.ylabel('Altura (m)')
plt.title('Tiro Parabólico')
plt.grid(True)
plt.show()
