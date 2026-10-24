# One Studio Man

Página «sobre mí» de One Studio Man en https://onestudioman.horaverda.es (es / ca / en).

- Textos y enlaces: `src/build.py` (diccionario `T` y lista `NETWORKS`).
- Imágenes: `py tools/make_assets.py` regenera `static/img/` desde `D:\One Man Studio\img` (necesita Pillow; solo en local).
- Probar: `py src/build.py` y `py -m http.server 8002 -d _site`.
- Publicación: cada push a `main` despliega con GitHub Pages (Actions).

Efecto de orbe: «Arcane Magic Effect» de Cethiel, OpenGameArt, CC0.
