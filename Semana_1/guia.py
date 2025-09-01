def saludar(nombre: str)->None:
     print(f"Hola {nombre}")

def operar(a:int, b: int)->int:
     print(f"La suma da :{(a + b)}")
     print(f"La resta da :{(a - b)}")
     print(f"La multiplicacion da :{(a * b)}")
     

def area_triangulo(a:float, b:float)->float:
     print(f"El area es de :{(a * b)/2}")

def buscar_mayor(a:int, b: int, c: int)->int:
     if a > b and a > c:
         return a
     elif b > a and b > c:
         return b
     else:
         return c

def verificar_acceso(a:int)->int:
     if a >= 18 :
       return print("Es mayor de edad")

def calcular_edad(a: int)->int:
    2025 - a
    return(calcular_edad)

