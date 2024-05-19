import math
# Se asume que los panales pueden ocupar cualquier orientacion dentro del techo

# Funcion de calcula de Area de rectangulos
def Area_rect(x,y):
    result = x*y
    return result


# Funcion que Calcula el la cantiada de Paneles que caben en un techo
# a ancho, b largo medidas en metros de los paneles solares
# x ancho ,y largo medidas en metros del techo 
def Calculo_Paneles(a,b,x,y):
    if a > x and b > x: 
        return 0
    elif a > y and b > y:
        return 0 
    else:
        AreaTecho = Area_rect(x,y)
        AreaPanel = Area_rect(a,b)
        Cant_Paneles = math.floor(AreaTecho/AreaPanel)
        return Cant_Paneles


# Funcion que Calcula el la cantiada de Paneles que caben en un techo Triangular
# x ancho, y largo medidas en metros de los paneles solares
# b base ,h altura medidas en metros del techo 
def Calculo_Paneles_tri(x,y,b,h):
    if x > b and y > b: 
        return 0
    elif x > h and y > h:
        return 0 
    else:
        AreaTecho = Area_rect(b/2,h/2)
        AreaPanel = Area_rect(x,y)
        Cant_Paneles = math.floor(AreaTecho/AreaPanel)
        return Cant_Paneles



#- Paneles 1x2 y techo 2x4 ⇒ Caben 4
print(Calculo_Paneles(1,2,2,4))
#- Paneles 1x2 y techo 3x5 ⇒ Caben 7
print(Calculo_Paneles(1,2,3,5))
#- Paneles 2x2 y techo 1x10 ⇒ Caben 0
print(Calculo_Paneles(2,2,1,10))
#- Paneles 1x3 y techo 1x10 ⇒ Caben 0
print(Calculo_Paneles(3,1,1,10))

#- Paneles 3x2 y techo base 9 / altura 5 ⇒ caben 3
print(Calculo_Paneles_tri(3,2,9,5))