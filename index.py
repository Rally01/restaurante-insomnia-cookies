from flask import Flask, render_template, redirect
from flask.globals import request

app = Flask(__name__)


@app.route('/') #Ruta de inicio, pagina principal donde inicia la web
def inicio():
    return render_template('inicio.html')


@app.route('/ingreso/', methods = ('GET', 'POST')) #Validacion desde el formulario de ingreso
def ingreso():

    if(request.method=='POST'):
        cad=""
        
        cad = request.form['correoingreso']
        cad = cad + " - " + request.form['passwordingreso']

        return cad
        #return redirect('/menu/')

    #return render_template('menu.html')


@app.route('/registro/', methods = ('GET', 'POST')) #Validacion desde el formulario de registro
def registro():

    if(request.method=='POST'):
        cad=""
        
        cad = request.form['nombreregistro']
        cad = cad + " - " + request.form['correoregistro']

        return cad
        #return redirect('/menu/')

    #return render_template('menu.html')


@app.route('/menu/') #Ruta a la pagina del menu
def menu():
    return render_template('menu.html')



if __name__ == '__main__':
 app.run()