print("This code is by SimplePyCode\n\nArea Calculator v1.0\n\n")
anzahlRaeume = input("Wie viele Räume sollen berechnet werden? Anzahl: ")
# print(f"{anzahlRaeume} Räume sind zu berechnen!")
raeume = []
i = 1
z = 1
a = 0
b = 0
while i <= int(anzahlRaeume):
    laenge = input(f"\nLänge von Raum {i} (in cm): ")
    # Länge von Raum i wird angegeben
    breite = input(f"Breite von Raum {i} (in cm): ")
    # Breite von Raum i wird angegeben
    c = int(laenge) / 100
    d = int(breite) / 100
    r = int(c) * int(d)
    raeume.append(r)
    i += 1
else:
    while z <= int(anzahlRaeume):
        b = z - 1
        a += int(raeume[b])
        z += 1
    else:
        print(f"Insgesamt sind es {a}m² Wohnfläche!")