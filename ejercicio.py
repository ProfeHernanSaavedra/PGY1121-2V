
import funciones as fn
  
op = 3

while op != 4:
    print("   MENU     ")
    print("*"*10)
    print("1. Calcular IVA")
    print("2. Descuento")
    print("3. Calculo IMC")
    print("4. Salir")
    op = int(input("Ingresar opción: (1-4): "))
    
    if op == 1:
        precio = int(input("Ingrese precio del producto: "))
        iva = fn.calcularIva(precio)
        print("El IVA del precio $:",precio,"es $",iva)
        
    if op == 2:
        precio = int(input("Ingrese precio del producto: "))
        descuento = int(input("Ingerse el % de descuento (0-100): "))
        fn.calculoDesc(precio,descuento)
    
    if op == 3:
        peso = float(input("Ingrese su peso en Kg: "))
        estatura = float(input("Ingrese estatura en metros: "))
        fn.calculoIMC(peso,estatura)