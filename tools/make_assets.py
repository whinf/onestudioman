"""Genera static/img/ a partir de los originales (requiere Pillow; se ejecuta en local).

py tools/make_assets.py
"""
from pathlib import Path
from PIL import Image

SRC = Path(r"D:\OneStudioMan\img")
FX = Path(r"M:\assets\biblioteca\effects\Arcane_Effect-e7d0f643\06")  # CC0, Cethiel (OpenGameArt)
OUT = Path(__file__).resolve().parent.parent / "static" / "img"
OUT.mkdir(parents=True, exist_ok=True)


def strip(sheet, cols, rows, h, name):
    """Recorta una hoja en celdas iguales y las pone en una tira horizontal de altura h."""
    im = Image.open(SRC / sheet).convert("RGBA")
    cw, ch = im.width // cols, im.height // rows
    w = round(cw * h / ch)
    out = Image.new("RGBA", (w * cols * rows, h))
    for i in range(cols * rows):
        r, c = divmod(i, cols)
        cell = im.crop((c * cw, r * ch, (c + 1) * cw, (r + 1) * ch)).resize((w, h), Image.LANCZOS)
        out.paste(cell, (i * w, 0))
    out.save(OUT / name, "WEBP", quality=88, method=6)
    print(name, out.size, w)


strip("OSMchar_flat03(walk).png", 4, 2, 300, "walk.webp")
strip("OSMchar_flat04(cast).png", 4, 2, 300, "cast.webp")

logo = Image.open(SRC / "OSM_logo.png").convert("RGBA")
logo.resize((360, 360), Image.LANCZOS).save(OUT / "logo.webp", "WEBP", quality=90, method=6)
logo.resize((64, 64), Image.LANCZOS).save(OUT / "icon-64.png", optimize=True)
logo.resize((180, 180), Image.LANCZOS).save(OUT / "apple-touch-icon.png", optimize=True)
for size in (192, 512):  # iconos del manifest (PWA); "maskable": el logo ocupa el 80 % centrado sobre fondo noche
    icon = Image.new("RGBA", (size, size), (16, 12, 30, 255))
    inner = logo.resize((round(size * 0.8), round(size * 0.8)), Image.LANCZOS)
    icon.alpha_composite(inner, (round(size * 0.1), round(size * 0.1)))
    icon.save(OUT / f"icon-{size}.png", optimize=True)

av = Image.open(SRC / "OMSavatar.png").convert("RGB")
av.resize((480, round(480 * av.height / av.width)), Image.LANCZOS).save(OUT / "avatar.webp", "WEBP", quality=84, method=6)
# Imagen para redes (og:image) 1200x630: avatar a la derecha, logo a la izquierda, fondo noche
og = Image.new("RGB", (1200, 630), (16, 12, 30))
a = av.resize((504, 630), Image.LANCZOS)
og.paste(a, (696, 0))
big = logo.resize((460, 460), Image.LANCZOS)
og.paste(big, (130, 85), big)
og.save(OUT / "og.jpg", quality=86, optimize=True)

frames = [Image.open(FX / f"Arcane_Effect_{i}.png").convert("RGBA") for i in range(1, 8)]
fw, fh = max(f.width for f in frames), max(f.height for f in frames)
orb = Image.new("RGBA", (fw * len(frames), fh))
for i, f in enumerate(frames):
    orb.paste(f, (i * fw + (fw - f.width) // 2, (fh - f.height) // 2))
orb.save(OUT / "orb.webp", "WEBP", quality=88, method=6)
print("orb", orb.size, fw)
