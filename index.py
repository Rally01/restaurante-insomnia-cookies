from flask import Flask, render_template, redirect
from flask.globals import request
from db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)


@app.route('/') #Ruta de inicio, pagina principal donde inicia la web
def inicio():
    return render_template('inicio.html')

@app.route('/ingreso/', methods = ('GET', 'POST')) #Validacion desde el formulario de ingreso
def ingreso():
    if( request.method == 'POST'):
        
        correo = request.form['correoingreso']
        contraseña = request.form['passwordingreso']

        dataBase = get_db()

        #select * from Usuarios where correo = 'facorrales@uninorte.edu.co' and contraseña = '12345'
        ingreso = dataBase.execute('select * from Usuarios where correo = ? and contraseña = ?', (correo, contraseña)).fetchone()
        print(correo, contraseña)
        dataBase.commit()

        if ingreso is not None:
            print('Usuario Correcto')
            return redirect('/menu/')
        else:
            print('Usuario no registrado')
        
    return render_template('inicio.html')


@app.route('/registro/', methods = ('GET', 'POST')) #Validacion desde el formulario de registro
def registro():
    if( request.method == 'POST'):
        
        nombres = request.form['nombreregistro']
        apellidos = request.form['apellidoregistro']
        correo = request.form['correoregistro']
        contraseña = request.form['passwordregistro']
        valcontraseña = request.form['confirmpasswordregistro']

        if contraseña == valcontraseña:

            dataBase = get_db()

            valregistro = dataBase.execute('select * from Usuarios where correo = ?', (correo,)).fetchone()
            print(correo)
            dataBase.commit()
            
            if valregistro is not None:
                print('Usuario registrado anteriormente')
                return render_template('inicio.html')
            
            else:
                print('Usuario nuevo')
                #insert into Usuarios (id, nombres, apellidos, correo, contraseña) values('2', 'Mariana', 'Corrales', 'mariana@hotmail.com', '12345');
                dataBase.execute('insert into Usuarios (nombres, apellidos, correo, contraseña) values(?, ?, ?, ?);', (nombres, apellidos, correo, contraseña)).fetchone()
                print(nombres, apellidos, correo, contraseña)
                dataBase.commit()

                valregistro = dataBase.execute('select * from Usuarios where correo = ? and contraseña = ?', (correo, contraseña)).fetchone()
                dataBase.commit()
                if valregistro is not None:
                    print('Usuario registrado correctamente')
                    return redirect('/menu/')

        else:
            print('Las contraseñas no coinciden')
            return render_template('inicio.html')

    #return render_template('inicio.html')


@app.route('/menu/') #Ruta a la pagina del menu
def menu():
    return render_template('menu.html')



if __name__ == '__main__':
 app.run()