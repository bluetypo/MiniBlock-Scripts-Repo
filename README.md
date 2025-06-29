# MiniBlock Typeface — Scripts Repository

Este repositorio contiene herramientas, scripts y documentación utilizadas durante el desarrollo de la familia tipográfica **MiniBlock**, diseñada con un enfoque modular y experimental.

MiniBlock está compuesta por múltiples estilos —incluyendo versiones 3D, condensadas y ornamentales— y ha sido diseñada para su uso en contextos gráficos donde se requiere una tipografía llamativa, geométrica y de fuerte personalidad. Este repositorio acompaña el proceso de afinación técnica y distribución profesional de la familia, incluyendo tareas como exportación, revisión de nodos, validaciones con FontBakery y pruebas visuales.

---

## 📁 Estructura del Repositorio

MiniBlock-Typeface-Scripts-Repository/
├── scripts/ # Scripts para GlyphsApp, Python y OpenType features
│ ├── align_nodes.py
│ ├── ornaments_dlig.fea
│
├── tests/ # Reportes técnicos y validaciones
│ ├── fontbakery-reports/
│ └── screenshots/
│
├── proofs/ # Especímenes, pruebas tipográficas y composiciones
│ ├── PDF/
│
│
├── resources/ # Documentación técnica, licencias y parámetros
│ ├── documentation/
│ └── EULA/
│
├── LICENSE
└── README.md


---

## 🛠️ Scripts incluidos

Los scripts y archivos incluidos permiten automatizar tareas esenciales en el proceso de producción tipográfica:

- `align_nodes.py`: Alinea nodos que presentan desviaciones mínimas respecto a líneas verticales/horizontales, útil para resolver advertencias de FontBakery.
- `ornaments_dlig.fea`: Código OpenType para ligaduras de ornamentos accesibles con combinaciones tipo `*01`,
---

## 📊 Validaciones y pruebas

Incluye reportes generados con:

- **FontBakery**: Validación de la calidad técnica de los archivos OTF/TTF (revisión de nombres, métricas, curvas, tablas internas).
- **Capturas y muestras**: Screenshots y pruebas impresas para verificar consistencia visual.

---

## 📄 Recursos y documentación

- Documentos técnicos (`MiniBlock_TechSpecs.md`) con parámetros de exportación, métricas y configuraciones de `fontinfo`.
- Archivos de licencia tipográfica en formato `.txt` (EULA para distribución con derechos restringidos).

---

## 🔖 Licencia

El contenido de este repositorio (scripts, documentos, código de características OpenType) está disponible bajo la [Licencia MIT](LICENSE).  
**Nota:** Este repositorio **no incluye** los archivos maestros `.glyphs` ni fuentes exportadas. El uso de la tipografía MiniBlock está sujeto a su respectiva licencia comercial o institucional.

---

© Bluetypo y colaboradores de MiniBlock  
[www.bluetypo.com](https://www.bluetypo.com)
