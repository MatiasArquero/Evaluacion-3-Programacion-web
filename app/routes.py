from app import app
from flask import render_template, request


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    asistencia = None

    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3

    return render_template('ejercicio1.html',p=promedio, a=asistencia)

@app.route('/ejercicio2',methods=['GET','POST'])
def ejercicio2():

    nombre_maximo = None
    largo_maximo = 0
    empates = []

    if request.method == 'POST':
        lista = [
            request.form.get('nombre1'),
            request.form.get('nombre2'),
            request.form.get('nombre3')
        ]



        #Consigo el nombre más grande de la lista
        #En formato int(tamaño) [largo_maximo]
        #Y en formato str(nombre) [nombre_maximo]
        for nombre in lista:
            largo_actual=len(nombre)

            if largo_actual>largo_maximo:
                largo_maximo=largo_actual
                nombre_maximo = nombre.capitalize()

        #Sabiendo el mayor compararé nuevamente
        #Asi sabré cuales tienen tamaños iguales.

        for nombre in lista:
            if len(nombre)==largo_maximo:
                empates.append(nombre.capitalize())
        #Si hay más de 2 nombre en la lista empates
        #Significa existen 2 nombres con len iguales

    return render_template(
        'ejercicio2.html',
        nombre_max=nombre_maximo,
        largo_max=largo_maximo,
        empates=empates
    )