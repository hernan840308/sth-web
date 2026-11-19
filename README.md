# Web de Soporte Tecnológico Hernández

Sitio estático de una página para presentar **Soporte Tecnológico Hernández** y sus
apps **STH Cam** y **STH Cam Premium**. No incluye enlaces de descarga de
aplicaciones ni enlaces a tiendas.

## Contenido

```
index.html                 Página completa (HTML, CSS y JS en un solo archivo)
assets/                    Emblema STH y icono de STH Cam
tools/gen_assets.py        Regenera los recursos desde el logo del cliente
```

## Publicar en GitHub Pages

1. El repositorio debe ser **público** (GitHub Pages gratuito no sirve repos
   privados).
2. En GitHub: **Settings → Pages → Build and deployment**.
3. Origen: **Deploy from a branch**, rama `main`, carpeta `/ (root)`.
4. La web quedará en `https://<usuario>.github.io/sth-web/`.

No hace falta compilar nada: `index.html` y `assets/` son la web completa.

## Editar el contenido

- Los textos están directamente en `index.html`.
- Los colores, tipografías y el tema claro/oscuro se controlan con las variables
  CSS de `:root`.
- Para cambiar el emblema o los iconos: `python3 tools/gen_assets.py`.

## Pendiente

La web no muestra teléfono, WhatsApp, correo ni dirección porque todavía no se
han proporcionado. Cuando estén disponibles, se añaden en una sección de
contacto y en el pie de página.
