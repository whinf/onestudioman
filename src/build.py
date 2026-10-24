"""Genera la web estática de One Studio Man en _site/ (es, ca, en). Solo stdlib.

py src/build.py
"""
import html
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
SITE = "https://onestudioman.horaverda.es"
LANGS = ["es", "ca", "en"]
LANG_NAMES = {"es": "Español", "ca": "Català", "en": "English"}
LOCALES = {"es": "es_ES", "ca": "ca_ES", "en": "en_GB"}

# Iconos simplificados (24x24, color de texto)
ICONS = {
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.3" fill="currentColor"/>',
    "youtube": '<rect x="2" y="5" width="20" height="14" rx="4" fill="currentColor"/><path d="M10 9v6l5-3z" fill="#c4302b"/>',
    "discord": '<path d="M5 6.5c2-1.3 4-1.8 4-1.8l.6 1.2a14 14 0 0 1 4.8 0l.6-1.2s2 .5 4 1.8c1.6 2.6 2.4 5.6 2.2 9.2-1.6 1.3-3.3 2-4.9 2.3l-1-1.6c-2.8.8-5.8.8-8.6 0l-1 1.6c-1.6-.3-3.3-1-4.9-2.3-.2-3.6.6-6.6 2.2-9.2z" fill="currentColor"/><circle cx="9" cy="12.5" r="1.6" fill="#5865f2"/><circle cx="15" cy="12.5" r="1.6" fill="#5865f2"/>',
    "facebook": '<path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21z" fill="currentColor"/>',
    "tiktok": '<path d="M14 3h3c.2 2 1.6 3.6 3.6 3.8v3a7 7 0 0 1-3.6-1.1V15a6 6 0 1 1-6-6v3.1a3 3 0 1 0 3 2.9z" fill="currentColor"/>',
}

NETWORKS = [
    # id, nombre, url, usuario, color de la marca
    ("youtube", "YouTube", "https://www.youtube.com/channel/UC20BiWd04bD34YqY7qNJyqw", "One Studio Man", "#c4302b"),
    ("discord", "Discord", "https://discord.gg/66u8zxG3XY", "discord.gg/66u8zxG3XY", "#5865f2"),
    ("instagram", "Instagram", "https://www.instagram.com/onestudioman/", "@onestudioman", "#c13584"),
    ("tiktok", "TikTok", "https://www.tiktok.com/@onestudioman", "@onestudioman", "#111111"),
    ("facebook", "Facebook", "https://www.facebook.com/profile.php?id=61594745101246", "One Studio Man", "#1877f2"),
]

T = {
    "es": {
        "title": "One Studio Man · Estudio de videojuegos de una sola persona",
        "desc": "One Studio Man es un estudio indie de una sola persona: videojuegos, personajes, sprites, vídeos y más. Sígueme en YouTube, Discord, Instagram, TikTok y Facebook.",
        "skip": "Saltar al contenido", "lang": "Idioma",
        "sister": "⚡ Del mismo autor: Hora Verda, el precio de la luz por horas",
        "hint": "Toca al mago para lanzar otro hechizo",
        "hero_label": "Personaje de One Studio Man: pulsa para lanzar un hechizo",
        "dialog": [
            "¡Hola, viajero! Bienvenido a One Studio Man.",
            "Aquí un solo creador hace de programador, artista, músico y narrador.",
            "Si te gustan los videojuegos hechos con cariño, acompáñame más abajo. ▼",
        ],
        "more": "Clic para seguir",
        "h1": "One Studio Man",
        "lede": "Un estudio de una sola persona: videojuegos, arte y más.",
        "about_h": "Sobre mí",
        "about": [
            "Soy el creador detrás de <strong>One Studio Man</strong>, un estudio independiente donde una sola persona hace todo el viaje: desde la primera idea hasta el último píxel.",
            "Diseño juegos, dibujo personajes y sprites como los de esta página, y comparto el proceso de creación en vídeos y en la comunidad. Además de videojuegos, también hago otros proyectos digitales, como esta misma web.",
        ],
        "alt_avatar": "Retrato del personaje de One Studio Man con un hechizo de cristales morados",
        "do_h": "Qué encontrarás",
        "do": [
            ("🎮 Videojuegos", "Juegos indie de principio a fin, hechos por una sola persona."),
            ("🧙 Personajes y sprites", "Diseño de personajes, animaciones y arte para juegos."),
            ("🎬 Vídeos y devlogs", "El proceso de creación, avances y pruebas."),
            ("💬 Comunidad", "Ideas, pruebas de juego y charla en Discord."),
        ],
        "links_h": "Sígueme",
        "links_lede": "Elige tu portal:",
        "go": "Ir ›", "join": "Unirse ›",
        "foot_sites": "Otros proyectos del autor:",
        "hv": "Hora Verda (precio de la luz)", "cer": "Cerdanyola Avui",
        "credits": "Efecto de orbe: «Arcane Magic Effect» de Cethiel (OpenGameArt, CC0). Personajes y logotipo: © One Studio Man.",
        "privacy": "Esta página no usa cookies ni analítica.",
    },
    "ca": {
        "title": "One Studio Man · Estudi de videojocs d'una sola persona",
        "desc": "One Studio Man és un estudi indie d'una sola persona: videojocs, personatges, sprites, vídeos i més. Segueix-me a YouTube, Discord, Instagram, TikTok i Facebook.",
        "skip": "Salta al contingut", "lang": "Idioma",
        "sister": "⚡ Del mateix autor: Hora Verda, el preu de la llum per hores",
        "hint": "Toca el mag per llançar un altre encanteri",
        "hero_label": "Personatge de One Studio Man: prem per llançar un encanteri",
        "dialog": [
            "Hola, viatger! Benvingut a One Studio Man.",
            "Aquí un sol creador fa de programador, artista, músic i narrador.",
            "Si t'agraden els videojocs fets amb estima, acompanya'm més avall. ▼",
        ],
        "more": "Clic per continuar",
        "h1": "One Studio Man",
        "lede": "Un estudi d'una sola persona: videojocs, art i més.",
        "about_h": "Sobre mi",
        "about": [
            "Soc el creador darrere de <strong>One Studio Man</strong>, un estudi independent on una sola persona fa tot el viatge: des de la primera idea fins a l'últim píxel.",
            "Dissenyo jocs, dibuixo personatges i sprites com els d'aquesta pàgina, i comparteixo el procés de creació en vídeos i a la comunitat. A més de videojocs, també faig altres projectes digitals, com aquesta mateixa web.",
        ],
        "alt_avatar": "Retrat del personatge de One Studio Man amb un encanteri de cristalls morats",
        "do_h": "Què hi trobaràs",
        "do": [
            ("🎮 Videojocs", "Jocs indie de principi a fi, fets per una sola persona."),
            ("🧙 Personatges i sprites", "Disseny de personatges, animacions i art per a jocs."),
            ("🎬 Vídeos i devlogs", "El procés de creació, avenços i proves."),
            ("💬 Comunitat", "Idees, proves de joc i xerrada a Discord."),
        ],
        "links_h": "Segueix-me",
        "links_lede": "Tria el teu portal:",
        "go": "Vés-hi ›", "join": "Uneix-t'hi ›",
        "foot_sites": "Altres projectes de l'autor:",
        "hv": "Hora Verda (preu de la llum)", "cer": "Cerdanyola Avui",
        "credits": "Efecte d'orbe: «Arcane Magic Effect» de Cethiel (OpenGameArt, CC0). Personatges i logotip: © One Studio Man.",
        "privacy": "Aquesta pàgina no fa servir galetes ni analítica.",
    },
    "en": {
        "title": "One Studio Man · A one-person game studio",
        "desc": "One Studio Man is a one-person indie studio: video games, characters, sprites, videos and more. Follow along on YouTube, Discord, Instagram, TikTok and Facebook.",
        "skip": "Skip to content", "lang": "Language",
        "sister": "⚡ Same author: Hora Verda, Spain's hourly electricity price",
        "hint": "Tap the mage to cast another spell",
        "hero_label": "One Studio Man character: press to cast a spell",
        "dialog": [
            "Hello, traveller! Welcome to One Studio Man.",
            "Here a single creator is the programmer, artist, musician and storyteller.",
            "If you like games made with care, follow me down below. ▼",
        ],
        "more": "Click to continue",
        "h1": "One Studio Man",
        "lede": "A one-person studio: video games, art and more.",
        "about_h": "About me",
        "about": [
            "I'm the creator behind <strong>One Studio Man</strong>, an independent studio where one person makes the whole journey: from the first idea to the last pixel.",
            "I design games, draw characters and sprites like the ones on this page, and share the making-of in videos and with the community. Besides games, I also build other digital projects, like this very website.",
        ],
        "alt_avatar": "Portrait of the One Studio Man character casting a purple crystal spell",
        "do_h": "What you'll find",
        "do": [
            ("🎮 Video games", "Indie games from start to finish, made by one person."),
            ("🧙 Characters & sprites", "Character design, animation and game art."),
            ("🎬 Videos & devlogs", "The making-of, progress and experiments."),
            ("💬 Community", "Ideas, playtests and chat on Discord."),
        ],
        "links_h": "Follow me",
        "links_lede": "Choose your portal:",
        "go": "Go ›", "join": "Join ›",
        "foot_sites": "Other projects by the author:",
        "hv": "Hora Verda (electricity price)", "cer": "Cerdanyola Avui",
        "credits": "Orb effect: “Arcane Magic Effect” by Cethiel (OpenGameArt, CC0). Characters and logo: © One Studio Man.",
        "privacy": "This page uses no cookies and no analytics.",
    },
}


def alternates():
    out = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}/{l}/">' for l in LANGS)
    return out + f'<link rel="alternate" hreflang="x-default" href="{SITE}/">'


def head(lang, t, url):
    e = html.escape
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{url}">
{alternates()}
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(t['title'])}">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/static/img/og.jpg">
<meta property="og:locale" content="{LOCALES[lang]}">
<meta property="og:site_name" content="One Studio Man">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#120d24">
<link rel="icon" href="/static/img/icon-64.png" type="image/png">
<link rel="apple-touch-icon" href="/static/img/apple-touch-icon.png">
<link rel="preload" href="/static/img/walk.webp" as="image">
<link rel="stylesheet" href="/static/style.css">
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Organization", "name": "One Studio Man", "url": "{SITE}/", "logo": "{SITE}/static/img/logo.webp", "description": "{e(t['desc'])}", "sameAs": [{", ".join(f'"{n[2]}"' for n in NETWORKS)}]}}</script>
<script src="/static/stage.js" defer></script>
</head>"""


def page(lang):
    t = T[lang]
    e = html.escape
    url = f"{SITE}/{lang}/"
    langs = " · ".join(
        f'<a href="/{l}/" hreflang="{l}" lang="{l}"' + (' aria-current="true"' if l == lang else "") + f">{LANG_NAMES[l]}</a>"
        for l in LANGS)
    dialog = "".join(f"<p>{e(s)}</p>" for s in t["dialog"])
    tiles = "".join(f'<div class="tile"><span class="k">{e(k)}</span><span class="u">{e(u)}</span></div>' for k, u in t["do"])
    links = "".join(
        f'<li><a href="{u}" rel="me noopener" style="--c:{c}"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[i]}</svg>'
        f'<span class="net">{n}</span><span class="h">{e(h)}</span>'
        f'<span class="go">{t["join"] if i == "discord" else t["go"]}</span></a></li>'
        for i, n, u, h, c in NETWORKS)
    about = "".join(f"<p>{p}</p>" for p in t["about"])
    return f"""{head(lang, t, url)}
<body>
<a class="skip" href="#main">{e(t['skip'])}</a>
<header class="top"><div class="wrap">
<a class="brand" href="/{lang}/"><img src="/static/img/icon-64.png" alt="" width="28" height="28"> One Studio Man</a>
<nav class="langs" aria-label="{e(t['lang'])}">{langs}</nav>
</div><div class="wrap sister-bar"><a class="sister" href="https://horaverda.es/{lang}/">{e(t['sister'])}</a></div></header>
<main id="main" class="wrap">
<div class="stage">
<div class="stars"></div><div class="ground"></div>
<span class="hp" aria-hidden="true">MP <i></i></span><span class="hint" aria-hidden="true">✦ {e(t['hint'])}</span>
<img class="logo" src="/static/img/logo.webp" alt="One Studio Man" width="210" height="210">
<button class="hero" type="button" aria-label="{e(t['hero_label'])}"></button>
</div>
<div class="dialog" aria-live="polite" title="{e(t['more'])}"><img src="/static/img/avatar.webp" alt="" width="62" height="62"><span class="who">One Studio Man</span>{dialog}<span class="next" aria-hidden="true">▼</span></div>
<h1>{e(t['h1'])}</h1>
<p class="lede">{e(t['lede'])}</p>
<section><h2>{e(t['about_h'])}</h2>
<div class="about"><img src="/static/img/avatar.webp" alt="{e(t['alt_avatar'])}" width="480" height="600" loading="lazy"><div>{about}</div></div>
</section>
<section><h2>{e(t['do_h'])}</h2><div class="tiles">{tiles}</div></section>
<section id="links"><h2>{e(t['links_h'])}</h2><p class="muted">{e(t['links_lede'])}</p><ul class="links">{links}</ul></section>
</main>
<footer class="foot"><div class="wrap">
<p>{e(t['foot_sites'])} <a href="https://horaverda.es/{lang}/">{e(t['hv'])}</a> · <a href="https://cerdanyola.horaverda.es/{lang}/">{e(t['cer'])}</a></p>
<p>{e(t['credits'])} {e(t['privacy'])}</p>
</div></footer>
</body>
</html>
"""


def root():
    items = "".join(f'<li><a href="/{l}/" hreflang="{l}" lang="{l}">{LANG_NAMES[l]} — {html.escape(T[l]["lede"])}</a></li>' for l in LANGS)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>One Studio Man</title>
<meta name="description" content="{html.escape(T['es']['desc'])}">
<link rel="canonical" href="{SITE}/">
{alternates()}
<link rel="icon" href="/static/img/icon-64.png" type="image/png">
<link rel="stylesheet" href="/static/style.css">
<script>
(function(){{var m={{ca:"ca",es:"es",gl:"es",eu:"es",en:"en"}};var l=(navigator.languages||[navigator.language||"es"]);
for(var i=0;i<l.length;i++){{var k=m[(l[i]||"").slice(0,2).toLowerCase()];if(k){{location.replace("/"+k+"/");return;}}}}
location.replace("/en/");}})();
</script>
</head>
<body><main class="wrap"><h1>One Studio Man</h1><p>Elige idioma · Tria l'idioma · Choose your language</p><ul>{items}</ul></main></body>
</html>
"""


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT / "static")
    for l in LANGS:
        (OUT / l).mkdir(parents=True)
        (OUT / l / "index.html").write_text(page(l), encoding="utf-8")
    (OUT / "index.html").write_text(root(), encoding="utf-8")
    (OUT / "404.html").write_text(root(), encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    urls = "".join(f"<url><loc>{SITE}/{l}/</loc></url>" for l in LANGS)
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8")
    print("ok", OUT)


if __name__ == "__main__":
    main()
