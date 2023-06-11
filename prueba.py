
from math import pi, tan, cos, sin
from math import radians
import numpy as np
import matplotlib.pyplot as plt

while True:  #bucle while que se repite aste que el usuario ingrese una velocidad inicial valida
   try: #instrucción para intentar convertir el valor ingresado por el usuario en un numero de punto flotante utilizando la función float
       vi = float(input("Introduzca la velocidad inicial en (m/s) : ")) #cuando se ingresa un valor valido se asigna este valor a la variable vi
       break #instruccion para salir del bucle 
   except ValueError: #en caso de que se ingresen valores no validos como una letra se producira este error y con la funcion except se mostrara un mensaje en pantalla
       print("Cantidad Incorrecta") #mensaje del error tipo ValueError
print("m/s =",vi) #se muestra en pantalla el valor de la velocidad inicial ingresada por el usuario

while True: #bucle que se repite asta que se ingrese un angulo de lanzamiento del proyectil valido (en grados)
   try: #instruccion que intenta convertir el valor ingresado por el usuario en un numero entero utilizando la funcion int
       angulo = int(input("Introduzca el ángulo en grados: ")) #si el usuario ingresa un valor valido se asigna este valor a la variable angulo
       break #instruccion para salir del bucle
   except ValueError: #en caso de que se ingresen valores no validos como una letra se producira este error y con la funcion except se mostrara un mensaje en pantalla
       print("\nCantidad Incorrecta\n") #mensaje del error tipo ValueError
print(angulo,"°")#no es necesario, lo uso para que vayamos viendo el resultado

while True: #bucle que se repite asta que el usuario ingrese el valor de la gravedad en metros por segundo al cuadrado
   try: #instrucción para intentar convertir el valor ingresado por el usuario en un numero de punto flotante utilizando la función float
       g = float(input("Introduzca el valor de gravedad en m/s^2: "))  #si el usuario ingresa un valor valido se asigna este valor a la variable g
       break #instruccion para salir del bucle
   except ValueError: #en caso de que se ingresen valores no validos como una letra se producira este error y con la funcion except se mostrara un mensaje en pantalla
       print("\nCantidad Incorrecta\n") #mensaje del error tipo ValueError
print("\ng =",g) #se muestra en pantalla el valor de la gravedad ingresado por el usuario

grados = ((angulo*pi)/180) #se convierte el angulo de lanzamiento del proyectil de grados a radianes
print ("\ngrados =",grados) #se muestra en la pantalla el valor del angulo en radianes

while True: #bucle que se repite asta que se ingrese un valor valido para la posicion inicial horizontal en el eje x
   try: #instruccion para intentar convertir el valor ingresado por el usuario en un número de punto flotante utilizando la función float
       xo = float(input("Posición horizontal inicial [x0]: ")) #si el valor ingresado es valido se asigna a la variable xo
       break #instruccion para salir del bucle
   except ValueError: #en caso de que se ingresen valores no validos como una letra se producira este error y con la funcion except se mostrara un mensaje en pantalla
       print("\nCantidad Incorrecta\n") #se muestra en pantalla un mensaje de error cuando el usuario ingresa un valor no válido

while True: #bucle que se repite asta que se ingrese un valor valido para la posicion inicial vertical en el eje y
   try: #instruccion para intentar convertir el valor ingresado por el usuario en un número de punto flotante utilizando la función float
       yo = float(input("Posición vertical inicial [y0]: ")) #si el valor ingresado es valido se asigna a la variable yo
       break #instruccion para salir del bucle
   except ValueError: #en caso de que se ingresen valores no validos como una letra se producira este error y con la funcion except se mostrara un mensaje en pantalla
       print("\nCantidad Incorrecta\n") #se muestra en pantalla un mensaje de error cuando el usuario ingresa un valor no válido


#Formulas
a = tan(grados) #se calcula la tangente del ángulo de lanzamiento del proyectil en radianes con la función tan
b = ((g)/((2*vi*2)*cos(grados)*2)) #se calcula el valor de b que es un parámetro utilizado en la ecuación de la trayectoria del proyectil
print()
ymax=(vi**2)*(np.sin(grados)*sin(grados))/(2*g) #se calcula la altura máxima alcanzada por el proyectil durante su trayectoria
xmax=(vi**2)*(np.sin(2*grados))/(g) #se calcula el alcance máximo horizontal del proyectil durante su trayectoria
vho = vi*(cos(radians(angulo))) #se calcula la velocidad horizontal inicial del proyectil
vver = vi*(sin(radians(angulo))) #se calcula la velocidad vertical inicial del proyectil


print("Un proyectil lanzado con una velocidad inicial de Vo=",vi,"m/s y un ángulo de ?=",angulo,"°,")
print("iniciará su trayectoria con una velocidad horizontal de vxO: ",format(vho,".3f"),"m/s,")
print("y una velocidad vertical de vyO: ",format(vver,".3f"),"m/s.")
print()
print("Los parámetros más relevantes de su trayectoria son:")

tmax=(vi*sin(grados))/(g)  #se calcula el tiempo máximo que el proyectil tarda en alcanzar la altura máxima durante su trayectoria
tv=2*(tmax) #se calcula el tiempo total de vuelo del proyectil
print()
print(str("La altura máxima  alcanzada por el proyectil es: Ymax")+" = "+str(ymax)+" m")
print()
print(str("El alcance máximo horizontal  del proyectil es: Xmax")+" = "+str(xmax)+" m")
print()
print("La altura máxima (m) alcanzada por el proyectil es: Ymax =",format(ymax,".2f"))
print()
print("El alcance máximo horizontal(m) del proyectil es: Xmax =",format(xmax," .2f"))
print()
print("El tiempo máximo t1max (s) que alcanza el proyectil para el ángulo ? es: t1max =",format(tmax,".2f"))
print()
print("El tiempo de vuelo t1v(s) que alcanza el proyectil para el angulo ? es: t1v =",format(tv,".2f"))
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")

# Definimos la ecuación de la trayectoria
def f(x):  #la función llamada f(x) representa la ecuación de la trayectoria del proyectil
   return(a*x-b*x**2) #la funcion toma como argumento un valor X y devuelve el valor correspondiente de Y en la trayectoria del proyectil
x=np.linspace(0,xmax,500) #se utiliza la función np.linspace para crear un conjunto de 500 valores para el eje x de la gráfica que van desde 0 hasta el valor de xmax

# añadimos el subtitulo
plt.suptitle("CINEMÁTICA",fontsize=20,color="red")  #la función plt.suptitle se utiliza para añadir un subtítulo a la gráfica tomando como argumentos el texto, fontsize y color

#añadimos las etiquetas de los ejes
plt.xlabel("xmax",fontsize=20,color="red")                                       #utilizamos la función plt.xlabel para añadir una etiqueta al eje x de la gráfica tomando como argumentos el texto de la etiqueta y los parámetros opcionales fontsize y color
plt.ylabel("ymax",fontsize=20,color="blue") #utilizamos la función plt.ylabel para añadir la etiqueta "ymax" al eje Y de la gráfica, mienas que el tamaño y el color del texto se especifican utilizando los parámetros opcionales fontsize y color
#añadimos texto
plt.text(((np.argmax(f(x)))/2),np.max(f(x))+1,"vi=",fontsize=10) #utiliza la función plt.text para añadir el texto "vi=" a la gráfica tomando como argumentos las coordenadas X e Y donde se mostrará el texto, X e Y se calculan utilizando las funciones np.argmax() y np.max() y el tamaño del texto se especifica utilizando el parámetro fontsize
plt.text(((np.argmax(f(x)))/2)+11,np.max(f(x))+1,(str(vi)+"m/s"),fontsize=10) #

# Añadimos la rejilla en la gráfica
plt.grid(True)                #utilizamos la función plt.grid() para añadir una rejilla a la gráfica tomando como argumento el valor booleano True que indica si se debe mostrar o no la rejilla                                             
plt.grid(color = '0.5', linestyle = '--', linewidth = 1) #utilizamos la función plt.grid() para personalizar el aspecto de la rejilla en la gráfica usando los parámetros un color gris claro ('0.5'), un estilo de línea discontinua ('--') y un grosor de línea de 1 píxel
# Añadimos los ejes
# plt.axis("tight")

# dibujamos y ponemos etiquetas a la gráfica
plt.text(3,1,angulo,fontsize=10) #utilizamos la función plt.text() para añadir el texto el "valor del ángulo de lanzamiento ingresado por el usuario a la gráfica", tomando como argumentos las coordenadas X (3) e Y (1) donde se mostrará el texto y el tamaño del texto con el parámetro fontsize (10)
plt.plot(x, f(x), "red", linewidth = 2, label = (str(angulo)+"º")) #utilizamos la función plt.plot() para dibujar la gráfica de la trayectoria del proyectil tomando como argumentos los valores de X(x) e Y(f(x)) que se deben graficar, el color que es rojo ("red") y el grosor de la línea (2 píxeles) que representa la trayectoria y una etiqueta para la línea
plt.show() #utilizamos la función plt.show() para mostrar la gráfica en la pantalla