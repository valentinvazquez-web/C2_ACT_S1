def mostrar_atracciones(atraccion):
    print("Menu de Atracciones")
    print("1. Montaña Rusa")
    print("2. Carrusel")
    print("3. Casa del terror")
    seleccion_atracciones = int(input("Enumere cuantas atracciones desea visitar: "))
    for i in range(seleccion_atracciones):
        atraccion = int(input(f"Seleccione la atraccion a visitar {i+1}: "))
        atracciones += atraccion
    return atraccion

def puede_subir(edad, atraccion):
    print(f"Indicar su edad:{edad} ")
    print(f"Indicar atraccion a la que desea subir:{atraccion}")
    edad = int
    if atraccion == 1 and edad >= 12:
        return True
    elif atraccion == 2 and edad < 6:
        return True
    else:
        return False
    
def calcular_precio(atraccion):
    print(f"Indique atraccion seleccionada:{atraccion}")
    if atraccion == 1 :
       return print("Valor de entrada: $1500")
    elif atraccion == 2 :
        return print("Valor de entrada: $800")
    elif atraccion == 3 :
        return print("Valor de entrada: $1200")

def registrar_visita():
    print("Indique su nombre: ")
    print("Indique cantidad de atracciones que subio: ")
    print("Indique total de gastos: ")
    return 

def mostrar_resumen(resumen):
    print(f"Su resumen es:{resumen}")
    return resumen
    
