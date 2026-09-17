import os
from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

# Obtiene la ruta exacta donde está guardado este archivo app.py
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(basedir, "static"),
    template_folder=os.path.join(basedir, "templates"),
)

# Lista con tus 3 gatitos
gatos = [
    {
        "nombre": "Gatito 1",
        "imagen": "gato1.jpeg",
        "edad": "1 mes",
        "caracteristica": "Tierno, juguetón y busca un hogar lleno de amor.",
    },
    {
        "nombre": "Gatito 2",
        "imagen": "gato2.jpeg",
        "edad": "1 mes",
        "caracteristica": "Muy curioso y le encanta acurrucarse.",
    },
    {
        "nombre": "Gatito 3",
        "imagen": "gato3.jpeg",
        "edad": "1 mes",
        "caracteristica": "Dormilón, tranquilo y muy dulce.",
    },
]


@app.route("/")
def index():
  return render_template("index.html", lista_gatos=gatos)


@app.route("/agregar", methods=["POST"])
def agregar_gato():
  nombre = request.form.get("nombre")
  edad = request.form.get("edad")
  caracteristica = request.form.get("caracteristica")

  if "imagen" in request.files:
    file = request.files["imagen"]
    if file.filename != "":
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.static_folder, filename))

      gatos.append({
          "nombre": nombre,
          "imagen": filename,
          "edad": edad,
          "caracteristica": caracteristica,
      })

  return redirect(url_for("index"))


if __name__ == "__main__":
  app.run(debug=True)