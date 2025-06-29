# MiniBlock — Lista de Verificación de Exportación

Antes de exportar cualquier estilo de la familia MiniBlock, asegúrate de completar los siguientes pasos.

---

##  Revisión técnica

- [ ] No hay nodos fuera del grid
- [ ] No hay contornos con direcciones incorrectas
- [ ] No hay extremos flotantes (puntos que no tocan ejes cuando deberían)
- [ ] Los puntos están alineados donde se espera (no hay "semi-verticales" si no son intencionales)
- [ ] No hay paths duplicados
- [ ] No hay componentes huérfanos

---

##  Características OpenType

- [ ] Todas las features (`calt`, `dlig`, etc.) están sin errores
- [ ] Todas las ligaduras personalizadas están implementadas correctamente
- [ ] El archivo `.fea` compila sin advertencias
- [ ] Ornamentos `*01`–`*20` funcionan como esperado

---

##  Métricas y espaciado

- [ ] Las métricas están revisadas (Ascender, Descender, LineGap)
- [ ] El `kerning` está limpio y no hay pares redundantes
- [ ] No hay diferencias innecesarias entre masters si no son interpolables
- [ ] La alineación vertical/horizontal es coherente

---

##  Validaciones

- [ ] El archivo pasa **FontBakery** sin errores críticos
- [ ] Se han generado muestras PDF o capturas visuales
- [ ] Nombre de la fuente (PostScript, styleName) es correcto
- [ ] Verificado en Adobe Fonts Tester o aplicación de escritorio

---

##  Exportar

- [ ] Exportar como `.otf` y/o `.woff`
- [ ] Confirmar que los archivos exportados abren correctamente
- [ ] Empaquetar con EULA y ficha técnica si se comp
