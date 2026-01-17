from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


@app.route('/resultado', methods=['POST'])
def resultado():
    nota1 = float(request.form['nota1'])
    nota2 = float(request.form['nota2'])
    nota3 = float(request.form['nota3'])
    asistencia = float(request.form['asistencia'])

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 40 and asistencia >= 75:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    return render_template(
        'resultado.html',
        promedio=round(promedio, 2),
        asistencia=asistencia,
        estado=estado
    )
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


@app.route('/resultado2', methods=['POST'])
def resultado2():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    nombres = [nombre1, nombre2, nombre3]

    nombre_mas_largo = max(nombres, key=len)
    cantidad_caracteres = len(nombre_mas_largo)

    return render_template(
        'resultado2.html',
        nombre=nombre_mas_largo,
        cantidad=cantidad_caracteres
    )



if __name__ == '__main__':
    app.run(debug=True)
