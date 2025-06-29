from GlyphsApp import *

# Umbrales verticales
limite_superior_y = 1000
limite_inferior_y = 0

# Diccionarios para almacenar resultados por capa
glifos_y_mayor_1000 = {}
glifos_y_menor_0 = {}

for g in Glyphs.font.glyphs:
    for l in g.layers:
        if not l.paths:
            continue
        nombre_capa = l.name
        nombre_glifo = "/" + g.name

        tiene_y_mayor = False
        tiene_y_menor = False

        for path in l.paths:
            for node in path.nodes:
                y = node.position.y

                if not tiene_y_mayor and y > limite_superior_y:
                    glifos_y_mayor_1000.setdefault(nombre_capa, set()).add(nombre_glifo)
                    tiene_y_mayor = True

                if not tiene_y_menor and y < limite_inferior_y:
                    glifos_y_menor_0.setdefault(nombre_capa, set()).add(nombre_glifo)
                    tiene_y_menor = True

                if tiene_y_mayor and tiene_y_menor:
                    break
            if tiene_y_mayor and tiene_y_menor:
                break

# Mostrar resultados agrupados por capa
print("Glifos con nodos fuera del rango vertical (Y < 0 o Y > 1000):\n")

todas_capas = sorted(set(glifos_y_mayor_1000.keys()).union(glifos_y_menor_0.keys()))

for capa in todas_capas:
    print(f"🔹 {capa}:")
    if capa in glifos_y_menor_0:
        print("  ➤ Nodos con Y < 0:")
        print("   ", " ".join(sorted(glifos_y_menor_0[capa])))
    if capa in glifos_y_mayor_1000:
        print("  ➤ Nodos con Y > 1000:")
        print("   ", " ".join(sorted(glifos_y_mayor_1000[capa])))
    print()
