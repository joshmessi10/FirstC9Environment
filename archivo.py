import os
import time
import random
from datetime import datetime

# ========= UTILIDADES =========

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausa():
    input("\nPresiona ENTER para continuar...")

def escribir_lento(texto, velocidad=0.03):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()

# ========= FUNCIONES =========

def mostrar_fecha():
    limpiar()
    ahora = datetime.now()
    escribir_lento("📅 Fecha y hora actual:")
    print(ahora.strftime("%d/%m/%Y %H:%M:%S"))
    pausa()

def juego_adivinar():
    limpiar()
    numero = random.randint(1, 10)
    intentos = 3

    escribir_lento("🎯 Bienvenido al juego: Adivina el número (1-10)")
    
    while intentos > 0:
        try:
            intento = int(input(f"\nTe quedan {intentos} intentos. Tu número: "))
            
            if intento == numero:
                escribir_lento("🎉 ¡Correcto! Eres un crack.")
                break
            else:
                escribir_lento("❌ Incorrecto...")
                intentos -= 1

        except ValueError:
            print("⚠️ Ingresa un número válido.")

    if intentos == 0:
        print(f"\n💀 Se acabaron los intentos. El número era {numero}")

    pausa()

def generador_frases():
    limpiar()
    frases = [
        "🔥 Hoy es un gran día para programar.",
        "🚀 El éxito es la suma de pequeños esfuerzos repetidos.",
        "💡 Cada error es una oportunidad para aprender.",
        "🐍 Python hace que todo sea más divertido."
    ]
    escribir_lento("✨ Frase motivadora del día:\n")
    print(random.choice(frases))
    pausa()

def modo_hacker():
    limpiar()
    escribir_lento("🟢 Iniciando modo hacker...\n", 0.05)
    
    for i in range(20):
        linea = "".join(random.choice("01") for _ in range(50))
        print(linea)
        time.sleep(0.05)
    
    escribir_lento("\n🔓 Acceso concedido.")
    pausa()

# ========= MENÚ PRINCIPAL =========

def menu():
    while True:
        limpiar()
        print("""
=====================================
        🚀 SUPER CONSOLA PYTHON
=====================================
1. Ver fecha y hora
2. Jugar a adivinar el número
3. Frase motivadora
4. Modo hacker
5. Salir
=====================================
        """)

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_fecha()
        elif opcion == "2":
            juego_adivinar()
        elif opcion == "3":
            generador_frases()
        elif opcion == "4":
            modo_hacker()
        elif opcion == "5":
            escribir_lento("👋 ¡Hasta luego, programador!")
            break
        else:
            print("⚠️ Opción no válida.")
            time.sleep(1)

# ========= EJECUCIÓN =========

if __name__ == "__main__":
    menu()

