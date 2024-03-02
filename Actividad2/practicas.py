

usuario = input("Usuario digite nombre y apellido: ")
accion = input("¿Qué quieres hacer? ")

while accion == "comprar": 

    cervezas = [
        {"nombre": "Heiniken", "precio": 200},
        {"nombre": "Corona", "precio": 250},
        {"nombre": "Pilsen", "precio": 300},
        {"nombre": "Aguila light", "precio": 220},
        {"nombre": "Club Colombia", "precio": 280}
        
    ]
    print("Opciones disponibles:")
    for cerveza in cervezas:
        print(cerveza["nombre"])
    eleccion = input("¿Qué quieres comprar? ")
    cantidad =int(input("Que cantidad quieres llevar? "))

    total= 0

    for cerveza in cervezas:
        if eleccion == cerveza["nombre"]:
            total += cerveza["precio"] * cantidad
            print("Vas a comprar", eleccion, "vale ${}".format(cerveza["precio"]))
            print(usuario)
            print("Total compra: ${}".format(total))
            print("¡Gracias por tu compra!")
            
            break
    else:
        print("La cerveza que elegiste no está disponible.")

    accion = input(" Digita *comprar* para hacer otra compra: ")

print("¡Gracias por tu compra!")
    



    

