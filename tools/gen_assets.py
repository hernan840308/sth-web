#!/usr/bin/env python3
"""Genera los recursos gráficos de la web de STH a partir del logo del cliente.

Salidas:
    assets/sth-emblem.png   512x512  emblema sobre baldosa blanca redondeada
    assets/favicon.png       64x64   el mismo emblema para la pestaña
    assets/sthcam-icon.png  512x512  icono de la app STH Cam
"""
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SRC = Path("/root/work/Logo tecnológico de soporte y seguridad audiovisual (1).png")
APP_ICON = Path("/root/work/HernanTVPlay/app/src/play/res/drawable-nodpi/ic_launcher.png")
OUT = ROOT / "assets"


def load_emblem() -> Image.Image:
    im = Image.open(SRC).convert("RGB")
    return im.crop((90, 67, 1165, 606))


def emblem_tile(size: int) -> Image.Image:
    tile = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(tile).rounded_rectangle(
        [0, 0, size - 1, size - 1], radius=max(10, size // 7), fill=(255, 255, 255, 255)
    )
    em = load_emblem()
    pad = max(10, int(size * 0.075))
    ratio = min((size - pad * 2) / em.width, (size - pad * 2) / em.height)
    em = em.resize(
        (max(1, int(em.width * ratio)), max(1, int(em.height * ratio))),
        Image.LANCZOS,
    )
    tile.paste(em, ((size - em.width) // 2, (size - em.height) // 2))
    return tile


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    emblem_tile(512).save(OUT / "sth-emblem.png", optimize=True)
    emblem_tile(64).save(OUT / "favicon.png", optimize=True)

    icon = Image.open(APP_ICON).convert("RGBA")
    if icon.size != (512, 512):
        icon = icon.resize((512, 512), Image.LANCZOS)
    icon.save(OUT / "sthcam-icon.png", optimize=True)

    print("Recursos web generados en", OUT)


if __name__ == "__main__":
    main()
