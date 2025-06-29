from GlyphsApp import *

# Ajustes
tolerancia = 2  # tolerancia máxima para considerar que un segmento es "casi" vertical u horizontal
correcciones = 0

for g in Glyphs.font.glyphs:
    for l in g.layers:
        if not l.paths:
            continue
        for path in l.paths:
            nodes = path.nodes
            for i in range(len(nodes) - 1):
                n1 = nodes[i]
                n2 = nodes[i + 1]
                dx = abs(n1.position.x - n2.position.x)
                dy = abs(n1.position.y - n2.position.y)

                # Corregir si el segmento es casi vertical
                if dx != 0 and dx <= tolerancia and dy > tolerancia:
                    promedio_x = round((n1.position.x + n2.position.x) / 2)
                    n1.position = NSPoint(promedio_x, n1.position.y)
                    n2.position = NSPoint(promedio_x, n2.position.y)
                    print(f"🔧 {g.name} ({l.name}): alineado verticalmente en X={promedio_x}")
                    correcciones += 1

                # Corregir si el segmento es casi horizontal
                elif dy != 0 and dy <= tolerancia and dx > tolerancia:
                    promedio_y = round((n1.position.y + n2.position.y) / 2)
                    n1.position = NSPoint(n1.position.x, promedio_y)
                    n2.position = NSPoint(n2.position.x, promedio_y)
                    print(f"🔧 {g.name} ({l.name}): alineado horizontalmente en Y={promedio_y}")
                    correcciones += 1

print(f"\n✅ Total de nodos alineados: {correcciones}")
