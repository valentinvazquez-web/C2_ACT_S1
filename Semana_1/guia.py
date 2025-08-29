def saludar(nombre: str)->None:
     print(f"Hola {nombre}")

def operar(a:int, b: int)->int:
     suma = a + b 
     resta = a - b
     multiplicacion = a * b
     return suma, resta, multiplicacion

def area_triangulo(a:float, b:float)->float:
     print(f"El area es de :{(a * b)/2}")

def buscar_mayor(a:int, b: int, c: int)->int:
     if a > b and a > c:
         return a
     elif b > a and b > c:
         return b
     else:
         return c
print(f"El mayor es:{buscar_mayor}")

