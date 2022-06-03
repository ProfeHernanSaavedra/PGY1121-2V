def calcularIva(precio):
    precio = precio * 0.19
    return precio

def calculoDesc(precio,descuento):
    total = (precio - (precio * (descuento/100)))
    print("El total a pagar con un descuento del ",descuento,"% es: $",total)

def calculoIMC(peso, estatura):
    imc = (peso/(estatura**2))
    
    if imc < 18.5:
        print("Bajo peso")
    else:
        if imc >=18.5 and imc <= 24.9:
            print("Peso adecuado")
        else:
            if imc >= 25 and imc <= 29.9:
                print("Sobrepeso") 
            else:
                if imc >=30 and imc <=34.9:
                    print("Obesidad grado 1")
                else:
                    if imc >=35 and imc <= 39.9:
                        print("Obesidad grado 2")
                    else:
                        if imc >40 :
                            print("Obesidad grado 3")