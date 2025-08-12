import random
import time
import os
import sys

simbolos = ["🍒", "🍋", "🍉", "⭐", "🔔", "💎"]

def rodar():
    return random.choice(simbolos), random.choice(simbolos), random.choice(simbolos)

# Clear screen and print static layout
os.system("cls" if os.name == "nt" else "clear")
print("Aperte Enter para jogar... (Ctrl+C para sair)")
print("Resultado:            ")
print("Mensagem:             ")

while True:
    input()

    # Animation in same spot (line 2)
    for _ in range(5):
        sys.stdout.write("\033[2;1H")  # move cursor to line 2, col 1
        sys.stdout.write("Resultado: " + " | ".join(random.choice(simbolos) for _ in range(3)) + "   ")
        sys.stdout.flush()
        time.sleep(0.2)

    # Final result
    r1, r2, r3 = rodar()
    sys.stdout.write("\033[2;1H")
    sys.stdout.write(f"Resultado: {r1} | {r2} | {r3}   ")
    sys.stdout.flush()

    # Message (line 3)
    if r1 == r2 == r3:
        msg = "3 iguais! Ganhou!"
    elif r1 == r2 or r2 == r3 or r1 == r3:
        msg = "2 iguais!"
    else:
        msg = "Nada."
    sys.stdout.write("\033[3;1H")
    sys.stdout.write(f"Mensagem: {msg}      ")
    sys.stdout.flush()
