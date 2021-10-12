from flask import Flask, render_template
from flask.globals import request

app = Flask(__name__)

@app.route('/', methods = ('GET', 'POST'))
def inicio():

    if(request.method=='POST'):    

        if(request.form['correoingreso'] == True):
            name='ingreso'
            return name
        else:
            cad=""
        
            cad = request.form['correoregistro']
            cad = cad + " - " + request.form['passwordregistro']

            return cad

    return render_template('inicio.html')

@app.route('/menu/')
def menu():
    return render_template('menu.html')


if __name__ == '__main__':

 # Iniciamos la apicación en modo debug

 app.run(debug=True)