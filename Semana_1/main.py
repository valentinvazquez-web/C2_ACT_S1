import guia 


print("Bienvenidos/as")
nombre = input("Ingrese su nombre de usuario: ")

guia.saludar(nombre)

num_1 = int(input("Numero 1: "))
num_2 = int(input("Numero 2: "))

resultado_suma, resultado_resta, resultado_multiplicacion = guia.operar(num_1, num_2)

base_triangulo = float(input("Base del triangulo: "))
altura_triangulo = float(input("Altura del triangulo: "))

guia.area_triangulo(base_triangulo,altura_triangulo)

num_1 = int(input("Numero 1: "))
num_2 = int(input("Numero 2: "))
num_3 = int(input("Numero 3: "))

guia.buscar_mayor(num_1, num_2, num_3)
