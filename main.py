import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    print("=== Generador de Contraseñas ===")
    try:
        longitud = int(input("¿De qué longitud deseas la contraseña? (mínimo 8): "))
        if longitud < 8:
            print("La longitud mínima es 8. Generando una de 8 caracteres...")
            longitud = 8
        
        contraseña = generar_contraseña(longitud)
        print(f"Contraseña generada: {contraseña}")
    except ValueError:
        print("Por favor, ingresa un número válido.")
