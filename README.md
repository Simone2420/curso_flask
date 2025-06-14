# Proyecto Flask + TailwindCSS

Este proyecto es una plantilla básica de Flask que utiliza TailwindCSS para los estilos.

## Estructura del proyecto

```
curso_flask/
│
├── app.py
├── static/
│   └── css/
│       ├── input.css
│       └── output.css
├── templates/
│   └── base.html
├── tailwind.config.js
├── postcss.config.js
├── package.json
├── package-lock.json
├── .gitignore
└── README.md
```

## Instalación

### 1. Clona el repositorio

```sh
git clone https://github.com/tu-usuario/curso_flask.git
cd curso_flask
```

### 2. Instala las dependencias de Python

Instala Flask y cualquier otra dependencia que uses:

```sh
pip install flask
```

### 3. Instala las dependencias de Node.js (opcional, solo si quieres recompilar los estilos)

```sh
npm install
```

### 4. Ejecuta la aplicación Flask

```sh
python app.py
```

Abre tu navegador en [http://localhost:5000](http://localhost:5000).

---

## ¿Cómo modificar los estilos con TailwindCSS?

1. Edita el archivo `static/css/input.css` y/o tus archivos HTML en `templates/`.
2. Si cambias los estilos, ejecuta este comando para regenerar el CSS:

```sh
npm run build:css
```

Esto actualizará `static/css/output.css`, que es el archivo que Flask sirve a tus templates.

---

## Notas

- El archivo `static/css/output.css` ya está generado y listo para usarse.
- No es necesario instalar Node.js ni npm si solo quieres usar la app y los estilos ya generados.
- Si quieres personalizar los estilos con Tailwind, sí necesitas Node.js y npm.

---

## Créditos

Plantilla creada con [Flask](https://flask.palletsprojects.com/) y [TailwindCSS](https://tailwindcss.com/).
