"""
Calcular la posicion de un objeto en el aire en una caida libre
Formulas:
• Velocidad final: v = v0 ± g ⋅ t
• Altura: \(y = y_0 + v_0 \cdot t \pm \frac{1}{2} g \cdot t^2\)
• Velocidad al cuadrado: v² = v₀² ± 2g(y - y₀)

y = y0 + (v0 * t) + (0.5 * g * (t ** 2))
y = altura final
y0 = altura inicial (metros) - altura_ inicial
v= velocidad final (metros/segundos)
v0= velocidad inicial (metros/segundos) - velocidad_final
t = tiempo (segundos) - tiempo
g = aceleracion de la gravedad (por defecto 9.81 m/s2) - GRAVEDAD
"""

#iniciar constantes
GRAVEDADES = {
    "Tierra": 9.81,
    "Marte": 3.7,
    "Luna": 1.62,
    "Jupiter": 24.79,
    "Sol": 274
}
VELOCIDAD_INICIAL = 0
UBICACION_POR_DEFECTO = "Tierra"



#pedir datos iniciales (altura, tiempo en el que queremos medir)
altura_inicial = float(input("Introduce la altura desde la que lo dejamos caer (cm):"))
tiempo = float(input ("¿En que momento quieres saber la posicion (segundos) ?"))
ubicacion = input("¿En que planeta estas? (Tierra, Luna, Marte, Jupiter, Sol)")
#pasamos a minusculas la ubicacion
ubicacion = ubicacion.lower()


#validamos que la ubicacion sea valida
if ubicacion in GRAVEDADES:
    #tenemos esta ubicacion
    GRAVEDAD = GRAVEDADES [ubicacion]
else:
    print("Ese sitio no existe, tarao, te pongo en la tierra")
    GRAVEDAD = GRAVEDADES [UBICACION_POR_DEFECTO]

#convertimos la funcion a python
#como recibo la altura en cm necesito pasarla a metros
altura_inicial /= 100  
altura_actual = altura_inicial + (VELOCIDAD_INICIAL * tiempo ) + ( 0.5 * GRAVEDAD * (tiempo ** 2))

# imprimimos la altura resultado
if altura_inicial <=0:
    print(f"El objeto esta en el suelo")
else:
    print (f"la altura en el segundo {tiempo} del objeto es {altura_actual} m.")