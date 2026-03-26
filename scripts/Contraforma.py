# MenuTitle: Abrir Contraforma (Con Tolerancia de 80px)

import GlyphsApp

# --- CONFIGURACIÓN ---
distancia = 30 
tolerancia = 80  # Rango de búsqueda desde el centro hacia los lados
indice_verde = 4 # Color verde en Glyphs 3

thisFont = Glyphs.font
if thisFont and thisFont.selectedLayers:
    layer = thisFont.selectedLayers[0]
    glyph = layer.parent

    # Guardamos valores originales para proteger el ancho total
    ancho_original = layer.width
    lsb_original = layer.LSB

    # 1. Encontrar los límites y el centro del dibujo
    puntos_x = [n.x for p in layer.paths for n in p.nodes]
    if puntos_x:
        min_x = min(puntos_x)
        max_x = max(puntos_x)
        centro_x = (min_x + max_x) / 2

        # 2. Desplazar nodos dentro del rango de tolerancia
        for path in layer.paths:
            for node in path.nodes:
                # OMITIR: Si el nodo es un borde exterior (con margen de 1 unidad)
                if abs(node.x - min_x) < 1 or abs(node.x - max_x) < 1:
                    continue
                
                # LÓGICA DE TOLERANCIA:
                # Solo movemos nodos que estén cerca del centro (dentro de los 80px)
                distancia_al_centro = abs(node.x - centro_x)
                
                if distancia_al_centro <= tolerancia:
                    if node.x < centro_x:
                        node.x -= distancia
                    else:
                        node.x += distancia

        # 3. Blindaje de métricas: restaurar LSB y Width
        layer.LSB = lsb_original
        layer.width = ancho_original

        # 4. Asignar color verde (Propiedad compatible con G3.41)
        glyph.color = indice_verde

        print(f"Éxito: {glyph.name} ajustado con tolerancia de {tolerancia}px.")
    else:
        print("El glifo no tiene nodos.")
else:
    print("Selecciona un glifo en la vista de edición.")
