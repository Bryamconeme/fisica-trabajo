
from math import pi, tan, cos, sin
from math import radians
import numpy as np
import matplotlib.pyplot as plt

while True:
   try:
       vi = float(input("Introduzca la velocidad inicial en (m/s) : "))
       break
   except ValueError:
       print("Cantidad Incorrecta")
print("m/s =",vi)

while True:
   try:
       angulo = int(input("Introduzca el ángulo en grados: "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")
print(angulo,"°")#no es necesario, lo uso para que vayamos viendo el resultado

while True:
   try:
       g = float(input("Introduzca el valor de gravedad en m/s^2: "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")
print("\ng =",g)

grados = ((angulo*pi)/180)
print ("\ngrados =",grados)

while True:
   try:
       xo = float(input("Posición horizontal inicial [x0]: "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")

while True:
   try:
       yo = float(input("Posición vertical inicial [y0]: "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")


#Formulas
a = tan(grados)
b = ((g)/((2*vi*2)*cos(grados)*2))
print()
ymax=(vi**2)*(np.sin(grados)*sin(grados))/(2*g)
xmax=(vi**2)*(np.sin(2*grados))/(g)
vho = vi*(cos(radians(angulo)))
vver = vi*(sin(radians(angulo)))


print("Un proyectil lanzado con una velocidad inicial de Vo=",vi,"m/s y un ángulo de ?=",angulo,"°,")
print("iniciará su trayectoria con una velocidad horizontal de vxO: ",format(vho,".3f"),"m/s,")
print("y una velocidad vertical de vyO: ",format(vver,".3f"),"m/s.")
print()
print("Los parámetros más relevantes de su trayectoria son:")

tmax=(vi*sin(grados))/(g)
tv=2*(tmax)
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
def f(x):
   return(a*x-b*x**2)
x=np.linspace(0,xmax,500)

# añadimos el subtitulo
plt.suptitle("CINEMÁTICA",fontsize=20,color="red")

#añadimos las etiquetas de los ejes
plt.xlabel("xmax",fontsize=20,color="red")                                      
plt.ylabel("ymax",fontsize=20,color="blue")
#añadimos texto
plt.text(((np.argmax(f(x)))/2),np.max(f(x))+1,"vi=",fontsize=10)
plt.text(((np.argmax(f(x)))/2)+11,np.max(f(x))+1,(str(vi)+"m/s"),fontsize=10)

# Añadimos la rejilla en la gráfica
plt.grid(True)                                                              
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
# Añadimos los ejes
# plt.axis("tight")

# dibujamos y ponemos etiquetas a la gráfica
plt.text(3,1,angulo,fontsize=10)
plt.plot(x, f(x), "red", linewidth = 2, label = (str(angulo)+"º"))
plt.show()