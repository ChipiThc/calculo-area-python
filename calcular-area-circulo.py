import math
#Solicatar al usario que ingrese el radio del circulo


radio = float(input("Por favor, Ingrese el area del circulo: "))

# Calcula el area del circulo 

area = math.pi * (radio**2)

# Mostrar a usuario el area calculada

print("El area del circulo con rapio", radio, "es:", area)