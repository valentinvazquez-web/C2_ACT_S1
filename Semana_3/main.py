total_ventas = 0 # acumulador (incrmenta por montos de venta)
cantidad_ventas = 0 #contador (cuenta la cantdad de ventas realizadas)
venta_mayor = None
venta_menor = None

while True:
   # (ENTRADA) Ingreso de ventas
   venta = float(input("Ingresar venta(Para finalizar ingresar 0): "))
   # crte de ciclo
   if venta == 0:
      break
   
   # (PROCESOS) Acuulamos ventas y contamos ventas
   total_ventas += venta
   cantidad_ventas += 1

   # (PROCESOS) Buscamos mayor y menor

   if cantidad_ventas == 1: # Condicional que inicia de base nuestras variables
      venta_mayor = venta
      venta_menor = venta
   else:
      # Condicional interno que compara mayores
      if venta > venta_mayor:
         venta_mayor = venta
      # Segundo condicional interno que compara menores
      if venta < venta_menor:
         venta_menor = venta

# (PROCESO)
promedio_ventas = total_ventas / cantidad_ventas

# (SALIDA) Se muestran los valores


print(f"Total de ventas relizadas: {cantidad_ventas} con un monto de: {total_ventas}")
if cantidad_ventas > 0:
   print(f"Venta mayor: {venta_mayor}")
   print(f"Venta menor: {venta_menor}")
   print(f"El promedio de ventas es:{promedio_ventas}")
else:
   print("No se registraron ventas....")