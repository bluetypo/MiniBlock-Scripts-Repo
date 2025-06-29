# MiniBlock — Font Info Settings

Este archivo documenta los parámetros clave definidos en el archivo `.glyphs` para la correcta exportación y consistencia técnica de la familia MiniBlock.

---

##  Font Info → Font

- **Family Name:** MiniBlock
- **Designer:** Bluetypo
- **Manufacturer:** Bluetypo
- **Vendor ID:** (vacío o personalizado si aplica)
- **Version:** 1.0
- **License URL:** (agregar si hay una licencia pública o personalizada)
- **Trademark:** MiniBlock is a trademark of Bluetypo.
- **Copyright Notice:** Copyright © 2025 Bluetypo.

---

##  Font Info → Masters

### Maestra principal
- **Name:** Regular (o Condensed/3D según estilo)
- **Ascender:** 1000
- **Descender:** 0
- **Cap Height:** (establecido si aplica)
- **x-Height:** (establecido si aplica)
- **Units per Em:** 1000
- **Interpolation Weight / Width:** según estilo
- **Italic Angle:** 0

---

## 🛠️ Custom Parameters por máster

| Parámetro         | Valor  |
|-------------------|--------|
| `typoAscender`    | 1000   |
| `typoDescender`   | 0      |
| `typoLineGap`     | 0      |
| `winAscent`       | 1000   |
| `winDescent`      | 50     |
| `hheaAscender`    | 1000   |
| `hheaDescender`   | 0      |
| `strikeoutSize`   | 50     |
| `strikeoutPosition` | 680 _(desactivado)_ |

>  *Nota: No hay letras descendentes; el valor de `winDescent` se ajusta a 50 para igualar la separación vertical a la horizontal.*

---

##  Features implementadas

- `calt` — Alternantes contextuales
- `dlig` — Ornamentos accesibles con combinaciones tipo `*01`, `*02`...
- `liga`, `kern` — Ligaduras y espaciado (si están activas en Glyphs)

---

##  Export Settings

- **Exportar como:** OTF / WOFF
- **Hinting:** Desactivado / automático (según preferencia)
- **Remove Overlap:** Activado
- **Autohint:** (según configuración por estilo)
