import random
import time

phrases = [
    "Je calcule votre destinée... ou peut-être juste du vent.",
    "Chargement de l’intelligence artificielle en carton...",
    "99% inutile, 100% rigolo !",
    "Un bug par jour éloigne le développeur du bonheur.",
    "Pourquoi ce script ? Je me le demande aussi."
]

print("🔮 Lancement du script mystérieux...\n")
time.sleep(1)

for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)

print("\n\n🧠 Révélation du jour :")
print(random.choice(phrases))
