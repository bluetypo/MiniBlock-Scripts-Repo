from GlyphsApp import *

# Parámetros
umbral_x = 1000
umbral_y = 0

# Diccionario para almacenar los resultados por capa
resultados_por_capa = {}

for g in Glyphs.font.glyphs:
    for l in g.layers:
        if not l.paths:
            continue
        for path in l.paths:
            for node in path.nodes:
                if node.position.x > umbral_x and node.position.y == umbral_y:
                    capa_nombre = l.name
                    if capa_nombre not in resultados_por_capa:
                        resultados_por_capa[capa_nombre] = set()
                    resultados_por_capa[capa_nombre].add("/" + g.name)
                    break
            else:
                continue
            break  # salir de paths si ya se encontró en este layer

# Imprimir resultados agrupados por capa
print("🧭 Glifos con nodos en x > 1000 y y = 0 agrupados por capa:\n")
for capa in sorted(resultados_por_capa.keys()):
    glifos = sorted(resultados_por_capa[capa])
    glifos_str = " ".join(glifos)
    print(f"🔹 {capa}:")
    print(glifos_str + "\n")
